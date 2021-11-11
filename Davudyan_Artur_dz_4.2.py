import requests


def currency_rates(currency_code):
    response = requests.get(r'http://www.cbr.ru/scripts/XML_daily.asp')
    content = response.content.decode(encoding=response.encoding)
    for el in content.split('<CharCode>')[1:]:
        char_code = el[:3]
        value = (el.split('<Value>')[1:][0].split('</Value>')[0])
        if currency_code.upper() == char_code:
            return f'Курс валюты: {value} рублей.'


if __name__ == '__main__':
    code_value = str(input('Введите код валюты: '))
    print(currency_rates(code_value))
