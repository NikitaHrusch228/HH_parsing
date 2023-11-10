import json
import os
import time
from pathlib import Path

import requests

[f.unlink() for f in Path("C:/pythonProject1/pythonProject/pagination").glob("*") if f.is_file()]
[f.unlink() for f in Path("C:/pythonProject1/pythonProject/vacancies").glob("*") if f.is_file()]
[f.unlink() for f in Path("C:/pythonProject1/pythonProject/cur_emp").glob("*") if f.is_file()]


def getpagevacancies(page=0):
    params = {
        'text': 'NAME: Программист',  # Текст фильтра. В имени должно быть слово "Аналитик"
        'page': page,  # Индекс страницы поиска на HH
        'per_page': 100  # Кол-во вакансий на 1 странице
    }
    req = requests.get('https://api.hh.ru/vacancies', params)
    data = req.content.decode()
    req.close()
    return data


for page in range(0, 1):
    # Преобразуем текст ответа запроса в справочник Python
    jsObj = json.loads(getpagevacancies(page))

    # Определяем количество файлов в папке для сохранения документа с ответом запроса
    # Полученное значение используем для формирования имени документа
    nextFileName = 'C:/pythonProject1/pythonProject/pagination/{}.json'.format(
        len(os.listdir('C:/pythonProject1/pythonProject/pagination')))

    f = open(nextFileName, mode='w', encoding='utf8')
    f.write(json.dumps(jsObj, ensure_ascii=False))
    f.close()

    # Необязательная задержка, но чтобы не нагружать сервисы hh, оставим. 5 сек мы может подождать
    time.sleep(0.1)
print('Страницы поиска вакансий собраны')
