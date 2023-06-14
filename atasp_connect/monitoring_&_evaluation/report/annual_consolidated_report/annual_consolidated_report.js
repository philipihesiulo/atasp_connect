// Copyright (c) 2023, Philip Ihesiulo and contributors
// For license information, please see license.txt
/* eslint-disable */

const d = new Date();
let current_year = d.getFullYear();

frappe.query_reports["Annual Consolidated Report"] = {
	"filters": [
		{
            fieldname: 'year',
            label: __('Year'),
            fieldtype: 'Link',
            options: 'Year',
            default: current_year
        },
	]
};
