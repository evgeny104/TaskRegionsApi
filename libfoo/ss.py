import json
import requests

def test_region_q():
    res = requests.get('https://regions-test.2gis.com/1.0/regions?q=тау')
    body = json.loads(res.text)
    assert (body["items"][0]["name"]) == "Актау"

test_region_q()