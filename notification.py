
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


from PyQt6.QtWidgets import QMessageBox


def notify(message: str) -> None:
	print(message)

	dlg = QMessageBox()
	dlg.setWindowTitle("CU-net-Authenticator INFO")
	dlg.setText(message)
	dlg.exec()
