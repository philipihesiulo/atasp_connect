// Copyright (c) 2023, Philip Ihesiulo and contributors
// For license information, please see license.txt

frappe.ui.form.on('ATASP Connect User', {
	refresh: function(frm) {
		frm.set_value('password', '');
	}
});
