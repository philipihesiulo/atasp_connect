// Copyright (c) 2023, Philip Ihesiulo and contributors
// For license information, please see license.txt
/* eslint-disable */

const d = new Date();
let current_year = d.getFullYear();


frappe.query_reports["Indicator Achievement Report"] = {
	'filters': [
		{
			fieldname: 'year',
			label: __('Year'),
			fieldtype: 'Link',
			options: 'Year',
			default: current_year
		},
		{
			fieldname: 'quarter',
			label: __('Quarter'),
			fieldtype: 'Link',
			options: 'Quarter',
		},
		{
			fieldname: 'zone',
			label: __('Zone'),
			fieldtype: 'Link',
			options: 'Zone',
		},

		{
			fieldname: 'indicator',
			label: __('Indicator'),
			fieldtype: 'Link',
			options: 'Indicator',
			mandatory: 1
		}
	]
}