// Copyright (c) 2023, Philip Ihesiulo and contributors
// For license information, please see license.txt
/* eslint-disable */

const d = new Date();
let current_year = d.getFullYear();

frappe.db.get_list('Quarter', {fields: ['name', 'code']}).then(db_quarters => {
	const quarters = db_quarters
		.sort(compare)
		.map(quarter => quarter.name);
	const filters =  [
		{
			fieldname: 'quarter',
			label: __('Quarter'),
			fieldtype: 'Select',
			options: ['All', ...quarters],
			default: 'All'
		},
		{
			fieldname: 'year',
			label: __('Year'),
			fieldtype: 'Link',
			options: 'Year',
			default: current_year
		},
	];
	frappe.query_reports["Submission of Quarterly Performance"]['filters'] = filters;
});


const compare = (prev, next ) => {
  if ( prev.code < next.code ){
    return -1;
  }
  if ( prev.code > next.code ){
    return 1;
  }
  return 0;
}