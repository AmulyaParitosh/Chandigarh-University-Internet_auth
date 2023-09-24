
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


from notify import notification
from .config import Config, Messg

def notify(msg: Messg) -> None:
	print(msg.summary)
	print(msg.description)
	notification(
		summary = msg.summary,
		message = msg.description,
		app_name = Config.APP_NAME,
		timeout = Config.NOTIFICATION_TIMEOUT,
	)
