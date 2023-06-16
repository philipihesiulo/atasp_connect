# Copyright (c) 2023, Philip Ihesiulo and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import now

class QuarterlyPerformance(Document):

	def before_submit(self):
		# Set Date Submitted
		self.date_submitted = now()

		# Make sure the entry is unique
		filters = {
			'year': self.year,
			'quarter': self.quarter,
			'indicator': self.indicator,
			'zone': self.zone,
			'docstatus': 1
		}

		if frappe.db.exists('Quarterly Performance', filters):
			frappe.throw(f'Achievements for {self.indicator} has already been submitted for {self.quarter}, {self.year} in your zone.')
		else:
			print('Record does not exist')
	
