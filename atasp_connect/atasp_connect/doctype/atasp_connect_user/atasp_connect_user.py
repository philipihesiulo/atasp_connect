# Copyright (c) 2023, Philip Ihesiulo and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import validate_email_address


class ATASPConnectUser(Document):
	def before_insert(self):
		self.full_name = f"{self.first_name} {self.last_name}"
		if not frappe.db.exists('User', self.email):
			try:
				user = frappe.get_doc({
					'doctype': 'User',
					'first_name': self.first_name,
					'last_name': self.last_name,
					'email': self.email,
					'phone': self.phone,
					'role_profile_name': self.role,
					'new_password': self.password
				})
				user.insert()
			except Exception as e:
				frappe.msgprint(
					msg=str(e),
					title='Error Creating User',
				)
				raise e

	def before_save(self):
		self.full_name = f"{self.first_name} {self.last_name}"
		try:
			user = frappe.get_doc('User', self.email)
			user.first_name = self.first_name
			user.last_name = self.last_name
			user.phone = self.phone
			user.role_profile_name = self.role
			
			if self.password != "":
				user.new_password = self.password

			user.save()
		except Exception as e:
			frappe.msgprint(
				msg=str(e),
				title='Error Updating User',
			)
			raise e

	def on_trash(self):
		try:
			user = frappe.get_doc('User', self.email)
			user.delete()
		except Exception as e:
			frappe.msgprint(
				msg=str(e),
				title='Error Deleting User',
			)
			raise e


