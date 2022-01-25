
# Copyright (c) 2013, Philip Ihesiulo and contributors
# For license information, please see license.txt

import frappe

def execute(filters):
	return get_columns(), get_data(filters)


def get_columns():
	return [
		"Code:Data:80",
		"Indicators:Link/Indicator:400",
		"Unit:Data:80",
		"Baseline:Data:80",
		"Revised LOP Target:Data:150",
		"Achievement:Link/Zone:100"
	]

def get_data(filters):

	#print(filters)
	quarterly_data = frappe.db.get_all("Quarterly Performance Data", 
		filters = {
			"docstatus": 1,
			"zone": filters.zone,
			"year": filters.year,
			"quarter": filters.quarter
		}
	)

	report_data = []

	for data in quarterly_data:
		doc = frappe.get_doc("Quarterly Performance Data", data.name)
		indicators = doc.achievements
		for indicator in indicators:
			print(indicator)
	
	print(quarterly_data)
	

	return [
		["A1", "No of Direct Beneficiaries", "No.", "9980", "32000", "15550"],
		["A2", "No of Youths Trained", "No.", "5780", "12000", "235550"],
		["A1", "No of new Jobs Created", "No.", "2110", "1400", "12550"],
		["A1", "Food Productions", "No.", "80", "100", "550"],
		["A1", "Amount of Income Generated", "No.", "25780", "122000", "1750"],
	]