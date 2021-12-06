import requests
import json
def get_advice():
    response = requests.get('https://api.adviceslip.com/advice')
    if response.status_code == 200:
        return response.json()['slip']['advice']
    else:
        return 'Something went wrong'


def main():
    print(get_advice())

if __name__ == '__main__':
    main()