# Copyright (c) 2023, Philip Ihesiulo and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class ATASPConnectUser(Document):
	def before_save(self):
		new_user_account = frappe.get_doc('User', self.user)
		self.full_name = new_user_account.full_name
