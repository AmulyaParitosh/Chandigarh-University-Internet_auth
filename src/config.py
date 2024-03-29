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


from pathlib import Path


class Config:
    AUTH_URL = "http://www.gstatic.com/generate_204"
    APP_NAME = "CU Net Authenticator"
    NOTIFICATION_TIMEOUT = 5000

    credentials_path = Path(".credentials")
    auth_state_path = Path("src/auth")
