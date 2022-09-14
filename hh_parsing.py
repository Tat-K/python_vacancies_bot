import requests
import time
import json

vacancies_ids = set()

def get_page(page=0):


    params = {
        'name': 'python',  # Текст фильтра. В имени должно быть слово "Аналитик"
        'area': 1002,  # Поиск ощуществляется по вакансиям города Минск
        'experience': {'noExperience', 'between1And3'},
        'page': page,  # Индекс страницы поиска на HH
        'per_page': 100,  # Кол-во вакансий на 1 странице
        'period': 1
    }

    req = requests.get('https://api.hh.ru/vacancies', params=params)
    data = req.content.decode()
    req.close()
    return data

def parse_data():
    lst_objs, new_objs = [], []

    for i in range(11):
        json_data = get_page(i)
        jsObj = json.loads(json_data)
        lst_objs.extend(jsObj['items'])

        time.sleep(0.25)

    for obj in lst_objs:
        if obj['id'] not in vacancies_ids:
            new_objs.append(obj)
        vacancies_ids.add(obj['id'])

    return new_objs
