// Copyright (c) 2023, Philip Ihesiulo and contributors
// For license information, please see license.txt
/* eslint-disable */

const d = new Date();
let current_year = d.getFullYear();

const quarters = [] 
frappe.db.get_list('Quarter').then(quarter => console.log(quarters));



frappe.query_reports["Submission of Quarterly Performance"] = {
	"filters": [
		{
            fieldname: 'quarter',
            label: __('Quarter'),
            fieldtype: 'Select',
            options: [
				'All', 
				...quarters
			],
			default: 'All'
        },
		{
            fieldname: 'year',
            label: __('Year'),
            fieldtype: 'Link',
            options: 'Year',
			default: current_year
        },
	]
};
