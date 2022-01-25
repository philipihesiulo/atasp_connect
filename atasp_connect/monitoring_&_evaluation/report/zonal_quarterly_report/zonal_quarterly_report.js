// Copyright (c) 2016, Philip Ihesiulo and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Zonal Quarterly Report"] = {
	"filters": [
		{
			"fieldname": "year",
			"fieldtype": "Link",
			"label": "Year",
			"mandatory": 1,
			"options": "Year",
			"wildcard_filter": 0
		},
		{
			"fieldname": "quarter",
			"fieldtype": "Select",
			"label": "Quarter",
			"mandatory": 1,
			"options": "First Quarter\nSecond Quarter\nThird Quarter\nFourth Quarter",
			"wildcard_filter": 0
		},
		{
			"fieldname": "zone",
			"fieldtype": "Link",
			"label": "Zone",
			"mandatory": 1,
			"options": "Zone",
			"wildcard_filter": 0
		}
	]
};
