import requests
from pprint import pprint


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return { 'Content-Type': 'application/json',
                 'Authorization': 'OAuth {}'.format(self.token)}


    def _get_upload_link(self, file_path):
        url_upload = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': file_path, 'overwrite': 'true'}
        response = requests.get(url_upload, headers = headers, params=params)
        return response.json()


    def upload(self, file_path, filename):
        result = self._get_upload_link(path_to_file)
        url = result['href']
        response = requests.put(url, data=open(filename, 'rb') )
        pprint(response.status_code)



if __name__ == '__main__':
    path_to_file = '/test/test.txt'
    token = 'y0_AgAAAAAA8wHXAADLWwAAAADbCiFJmRBQvIK8SqG0Uutis0VvAAphkq4'
    uploader = YaUploader(token)
    uploader.upload(path_to_file,'1.txt')
