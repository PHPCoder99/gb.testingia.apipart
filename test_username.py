import yaml
import requests

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)


def test_step1():
    url = "https://test-stand.gb.ru/api/posts" + str(testdata["userid"])
    headers = {
        "X-Auth-Token": testdata["userauthkey"]
    }
    assert requests.get(url, headers=headers).json()["username"] == testdata["username"]
