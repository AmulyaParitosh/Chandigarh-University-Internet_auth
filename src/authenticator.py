# SPDX-License-Identifier: MIT
# --------------------------------------------------------------
#
#             Copyright 2023 - 2023, Amulya Paritosh
#
#     This File is part of Auto-Internet-Authentication
# It is not in any way or form part of Chandigarh University
#  itself and purely developed to just make the authentication
#  process easier. This does not involve a bypass of any type
# nor it is encouraged to do so. It uses basic webscraping and
#          scripted calls to achieve authentication.
#
# --------------------------------------------------------------


import argparse
from getpass import getpass

from .config import Config
from .notification import Notification
from .scripts import login, logout, status


def authenticate() -> None:
    with Config.credentials_path.open("r", encoding="utf-8") as file:
        UID = file.readline().split("=")[-1].strip()
        PASSWORD = file.readline().split("=")[-1].strip()

    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=("login", "logout", "status"))
    parser.add_argument("-u", "--uid", type=str)
    parser.add_argument("-p", "--password", action="store_true")

    args = parser.parse_args()

    if args.mode == "login":
        if args.uid:
            UID: str = args.uid.upper()

        if args.password:
            PASSWORD: str = getpass(prompt="CU Internet Password : ")

        try:
            login(UID, PASSWORD)

        except KeyboardInterrupt:
            Notification.interrupt()

    elif args.mode == "logout":
        logout()

    elif args.mode == "status":
        status()


if __name__ == "__main__":
    authenticate()
