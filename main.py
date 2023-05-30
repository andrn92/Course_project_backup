import requests
import json
from vk_api import VkUser


class YaDisk:
    """Working with Yandex Disk"""

    host = 'https://cloud-api.yandex.net/'

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {'Content-Type': 'application/json', 'Authorization': 'OAuth {}'.format(self.token)}

    def create_folder(self, name_folder):
        url = self.host + 'v1/disk/resources/'
        params = {'path': name_folder}
        response = requests.put(url, headers=self.get_headers(), params=params)
        print(response.status_code)

    def upload_from_internet(self, file_url, disk_file_name):
        url = self.host + 'v1/disk/resources/upload/'
        params = {'path': '{}'.format(disk_file_name), 'url': file_url}
        response = requests.post(url, headers=self.get_headers(), params=params)
        print(response.status_code)
       

if __name__ == '__main__':
    vk = VkUser()
	user_id = input('Enter id user VKontakte: ')
    dict_urls = vk.get_photos(user_id)
    
    token_ya = input('Enter Yandex token: ')
    ya = YaDisk(token_ya)
    new_folder = '/photos_from_vk'
    ya.create_folder(new_folder)
    data_list = []
    for name, url in dict_urls.items():
        temp_dict = {}
        extention = url[1:].split('?')[0].split('/')[-1].split('.')[-1]
        size = url[0]
        name = name + '.' + extention
        ya.upload_from_internet(url[1:], '{}/{}'.format(new_folder, name))
        temp_dict['file_name'] = name
        temp_dict['size'] = size
        data_list.append(temp_dict)
    with open('info.json', 'w') as f:
                json.dump(data_list, f)



