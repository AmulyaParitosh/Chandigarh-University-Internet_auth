import argparse
from getpass import getpass

import requests
from bs4 import BeautifulSoup
from requests import Response

AUTH_URL = "http://www.gstatic.com/generate_204"

with open(".credintials", "r") as f:
    UID = f.readline().split("=")[-1].strip()
    PASSWORD = f.readline().split("=")[-1].strip()

def connect(username, password) -> None:
	login_url: str = requests.get(AUTH_URL).url
	response: Response = requests.get(login_url)
	soup = BeautifulSoup(response.text, "html.parser")
	authenticate = soup.find("input", {"name": "magic"})

	login_data = {
		"4Tredir": AUTH_URL,
		"magic": authenticate["value"],
		"username": username,
		"password": password,
	}

	response: Response = requests.post(login_url, data=login_data)

	if "Authentication failed" in response.text:
		print("❌ Authentication failed!")
	else:
		print("✔️ CU Internet Authentication successful!")


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-u", "--uid", type=str)
	parser.add_argument("-p", "--password", action="store_true")

	args = parser.parse_args()

	if args.uid:
		UID: str = args.uid.upper()

	try:
		if args.password:
			PASSWORD: str = getpass(prompt="CU Internet Password : ")

		connect(UID, PASSWORD)

	except KeyboardInterrupt:
		print("\n❗ Connection Interrupted")
