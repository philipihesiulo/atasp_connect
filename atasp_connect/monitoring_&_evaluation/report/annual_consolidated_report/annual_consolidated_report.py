# Copyright (c) 2023, Philip Ihesiulo and contributors
# For license information, please see license.txt

import frappe
from frappe import _


# Render the report
def execute(filters=None):
	return get_columns(), get_data(filters)

# Get report Data
def get_data(filters):
	data_rows = []
	indicators = frappe.get_list('Indicator', fields=['name', 'code'])
	zones = frappe.get_list('Zone')
	for indicator in indicators:
		total_outcome = 0
		row = {
			'ind_code': indicator.code,
			'indicator': indicator.name,
		}

		for zone in zones:
			outcome_in_zone = get_annual_indicator_achievement(
				zone.name, 
				indicator.name, 
				filters
			)
			row[str(zone.name).lower()] = outcome_in_zone
			total_outcome += outcome_in_zone
		row['total'] = total_outcome
		data_rows.append(row)
	return data_rows
			
# Get the sum of the achievements for a zone for any Indicator provided
def get_annual_indicator_achievement(zone, indicator, filters):
	
	achievements = frappe.get_list('Quarterly Performance', 
			       filters = {
				       'zone': zone,
				       'indicator': indicator,
				       'year': filters.year
				   }, 
				   pluck='outcome'
				)
	achievements = map(lambda x: int(x), achievements)
	if achievements == []:
		return 0

	return sum(achievements)
	
# Get Report columns
def get_columns():
	default_columns = [
		{
            'fieldname': 'ind_code',
            'label': _('Ind. Code'),
            'fieldtype': 'Data',
        },
		{
            'fieldname': 'indicator',
            'label': _('Indicator'),
            'fieldtype': 'Link',
            'options': 'Indicator'
        },
	]

	total_column = [
		{
            'fieldname': 'total',
            'label': _('Total'),
            'fieldtype': 'Int',
        }
	]

	zone_columns = []
	zones = frappe.get_list('Zone')

	for zone in zones:
		zone_item = {
			'fieldname': str(zone.name).lower(),
            'label': _(str(zone.name)),
            'fieldtype': 'Int',
		}

		zone_columns.append(zone_item)
	return default_columns + zone_columns + total_column

