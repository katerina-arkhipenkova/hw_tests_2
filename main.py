import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def new_folder(self, folder_name: str):
        disk_url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = self.get_headers()
        params = {'path': folder_name, 'overwrite': 'true'}
        response = requests.put(disk_url, headers=headers, params=params)
        return response.status_code

    def folders_exist(self, folder_name: str):
        disk_url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = self.get_headers()
        params = {'path': folder_name, 'overwrite': 'true'}
        response = requests.get(disk_url, headers=headers, params=params)
        return response.status_code


if __name__ == '__main__':
    with open('tokenYaD.txt', 'r') as file_object:
        tokenYaD = file_object.read().strip()

    uploader = YaUploader(tokenYaD)
    folder_name = 'NewFolder/'

    uploader.new_folder(folder_name)

