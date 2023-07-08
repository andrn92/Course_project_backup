import requests


class VkUser:
    """Working with api VKontakte"""

    host = 'https://api.vk.com/method/'
    
    def __init__(self):
        with open('token_vk.txt', 'r') as f:
            token = f.readline().strip()
        self.params = {'access_token': token, 'v': '5.131'}

    def get_photos(self, user_id=None, album_id='profile', count=5):
        url = self.host + 'photos.get'
        params = {'count': count,'extended': 1, 'user_id': user_id, 'album_id': album_id}
        res = requests.get(url, params={**self.params, **params})
        items = res.json()['response']['items']
        
        dict_urls = {}
        for item in items:
            name_1 = item['likes']['count']
            name_2 = item['date']
            if str(name_1) not in dict_urls:
                name = str(name_1)
            else:
                name = str(name_1) + str(name_2)
            types_size = {}
            for image in item['sizes']:
                types_size[image['type']] = image['url']
            if 'w' in types_size:
                url_img = types_size['w']
                insert = 'w'
            elif 'z' in types_size:
                url_img = types_size['z']
                insert = 'z'
            elif 'y' in types_size:
                url_img = types_size['y']
                insert = 'y'
            elif 'x' in types_size:
                url_img = types_size['x']
                insert = 'x'
            elif 'r' in types_size:
                url_img = types_size['r']
                insert = 'r'
            elif 'q' in types_size:
                url_img = types_size['q']
                insert = 'q'
            elif 'p' in types_size:
                url_img = types_size['p']
                insert = 'p'
            elif 'm' in types_size:
                url_img = types_size['m']
                insert = 'm'
            elif 'o' in types_size:
                url_img = types_size['o']
                insert = 'o'
            elif 's' in types_size:
                url_img = types_size['s']
                insert = 's'
            dict_urls[name] = insert + url_img

        return dict_urls

                


