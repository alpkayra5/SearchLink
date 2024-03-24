import requests
from urllib.parse import urlparse

def check_link(link):
    try:
        response = requests.get(link, timeout=5)
        if response.url.startswith('https://'):
            print('Link güvenli.')
        else:
            print('Link güvensiz.')
    except requests.exceptions.RequestException as e:
        print(f'Error: {e}')
    except Exception as e:
        print(f'Unexpected error: {e}')

def is_safe(link):
    try:
        response = requests.get(link, timeout=5)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException:
        return False

def main():
    link = input('Link giriniz: ')
    parsed_link = urlparse(link)
    if not parsed_link.scheme:
        print('Hatalı link verdiniz..')
        return
    if not is_safe(link):
        print('Link güvensiz.')
    else:
        check_link(link)

if __name__ == '__main__':
    main()
