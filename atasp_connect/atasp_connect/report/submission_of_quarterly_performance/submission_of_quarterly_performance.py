# Copyright (c) 2023, Philip Ihesiulo and contributors
# For license information, please see license.txt

import frappe
from frappe import _

quarters = ['First Quarter', 'Second Quarter', 'Third Quarter', 'Forth Quarter']
to_valid_field_name = lambda text : text.strip().replace(' ', '-').lower()

def get_quarter_count(zone, quarter, year):
	return frappe.db.count('Quarterly Performance', 
			filters={
				'zone': zone, 
				'quarter': quarter, 
				'year': year,
				'docstatus': ['in', [1, 2]]
			},
		)

def execute(filters=None):
	return get_columns(filters), get_data(filters)

def get_data(filters):
	data = []
	zones = frappe.get_list('Zone')
	for zone in zones:
		total_sub = 0
		row = {
			'zone': zone.name,
			'total': get_quarter_count(zone.name, filters.quarter, filters.year)
		}

		if filters.quarter == 'All':
			for quarter in quarters:
				row[to_valid_field_name(quarter)] = get_quarter_count(zone.name, filters.quarter, filters.year)
				total_sub += get_quarter_count(zone.name, filters.quarter, filters.year)
		
		row['total'] = total_sub
		frappe.msgprint(str(row))
		data.append(row)
	return data
				


def get_columns(filters):
	zone_column = [
		 {
            'fieldname': 'zone',
            'label': _('Zone'),
            'fieldtype': 'Link',
            'options': 'Zone'
        }
	]

	total_column = [
		{
            'fieldname': 'total',
            'label': _('Total Submissions') if filters.quarter == 'All' else filters.quarter,
            'fieldtype': 'Int',
        }
	]

	quarters_columns = []


	if filters.quarter == 'All':
		for quarter in quarters:
			quarters_columns.append({
				'fieldname': quarter.strip().replace(' ', '-').lower(),
				'label': _(quarter.title()),
				'fieldtype': 'Int',
			})

	return zone_column + quarters_columns + total_column

frappe.msgprint(f"Count for Adanni-Omor is: {get_quarter_count(zone='Adanni-Omor', quarter='First Quarter', year='2023')}")
