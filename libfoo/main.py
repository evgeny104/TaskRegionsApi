import json
import requests


def test_total_count():     # Функция проверяет -строку- "total", общее количество регионов в базе 22
    res = requests.get('https://regions-test.2gis.com/1.0/regions?page_size=5')
    body = json.loads(res.text)
    assert body["total"] == 22


def test_region_q():        # Функция проверяет поиск по наванию региона
    res = requests.get('https://regions-test.2gis.com/1.0/regions?q=тау')
    body = json.loads(res.text)
    assert (body["items"][0]["name"]) == "Актау"


def test_contre_code():     # Функция проверяет фильтр по региону из всех достуных стран
    res = requests.get('https://regions-test.2gis.com/1.0/regions?country_code=ru')
    body = json.loads(res.text)
    assert body["items"][5]["country"]["name"] == "Россия"
    assert body["items"][0]["country"]["code"] == "ru"


test_total_count()
test_region_q()
test_contre_code()
