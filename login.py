
# SPDX-License-Identifier: MIT
# --------------------------------------------------------------
#
#             Copyright 2023 - 2023, Amulya Paritosh
#
#     This File is part of Auto-Internet-Authentication
# It is not in any way or form part of Chandigarh University
#  itself and purly developed to just make the authentication
#  process easier. This does not involve a bypass of any type
# nor it is encouraged to do so. It uses basic webscrating and
#          scripted calls to achieve authentication.
#
# --------------------------------------------------------------


import argparse
from getpass import getpass

import requests
from bs4 import BeautifulSoup

AUTH_URL = "http://www.gstatic.com/generate_204"

with open(".credintials", "r") as f:
    UID = f.readline().split("=")[-1].strip()
    PASSWORD = f.readline().split("=")[-1].strip()

def connect(username, password) -> None:
	login_url: str = requests.get(AUTH_URL).url
	response = requests.get(login_url)
	soup = BeautifulSoup(response.text, "html.parser")
	authenticate = soup.find("input", {"name": "magic"})
	if authenticate is None:
		print("❗ Some error occured! Maybe you are already loggedin?")
		exit(1)

	login_data = {
		"4Tredir": AUTH_URL,
		"magic": authenticate["value"],
		"username": username,
		"password": password,
	}

	response = requests.post(login_url, data=login_data)

	if "Authentication failed" in response.text:
		print("❌ Authentication failed!")
		exit(1)
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
