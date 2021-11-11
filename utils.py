import requests


def currency_rates():
    response = requests.get(r'http://www.cbr.ru/scripts/XML_daily.asp')
    content = response.content.decode(encoding=response.encoding)
    code_value = str(input('Введите код валюты: '))
    for el in content.split('<CharCode>')[1:]:
        char_code = el[:3]
        value = (el.split('<Value>')[1:][0].split('</Value>')[0])
        if code_value.upper() == char_code:
            return print(f'Курс валюты: {value} рублей.')


# if __name__ == '__main__':


# Код для импорта модуля
import utils

currency_rates()