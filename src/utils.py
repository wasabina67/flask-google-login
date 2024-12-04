import requests  # type: ignore


def get_openid_configuration(url):
    return requests.get(url).json()
