import argparse
from getpass import getpass

import requests
from bs4 import BeautifulSoup
from requests import Response

BASE_LOGIN_URL = "http://172.16.2.1:1000"
HEADER_KEY = "41665a725d5a5fb0"

with open(".credintials", "r") as f:
    UID = f.readline().split("=")[-1].strip()
    PASSWORD = f.readline().split("=")[-1].strip()

parser = argparse.ArgumentParser()

parser.add_argument("-u", "--uid", type=str)
parser.add_argument("-p", "--password", action="store_true")

login_url = BASE_LOGIN_URL + "/login?" + HEADER_KEY
response: Response = requests.get(login_url)
soup = BeautifulSoup(response.text, "html.parser")
authenticate = soup.find("input", {"name": "magic"})


def connect(username, password) -> None:
    login_data = {
        "4Tredir": login_url,
        "magic": authenticate["value"],
        "username": username,
        "password": password,
    }

    response: Response = requests.post(BASE_LOGIN_URL, data=login_data)

    if "Authentication failed" in response.text:
        print("❌ Authentication failed!")
    else:
        print("✔️ CU Internet Authentication successful!")


if __name__ == "__main__":
    args = parser.parse_args()

    if args.uid:
        UID: str = args.uid.upper()

    try:
        if args.password:
            PASSWORD: str = getpass(prompt="CU Internet Password : ")

        connect(UID, PASSWORD)

    except KeyboardInterrupt:
        print("\n❗ Connection Interrupted")
