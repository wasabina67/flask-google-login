import requests


def get_openid_configuration(url):
    return requests.get(url).json
