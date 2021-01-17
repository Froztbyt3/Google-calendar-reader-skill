import requests
import json


def main():
    location = 'xxxxx'
    key = 'xxxxx'
    response = requests.get(
        'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(location, key))
    print('Status:', response.status_code)
    data = response.json()
    print(data['main'].get('temp'))


if __name__ == '__main__':
    main()
