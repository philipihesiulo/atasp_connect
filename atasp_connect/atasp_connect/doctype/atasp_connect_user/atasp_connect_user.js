// Copyright (c) 2023, Philip Ihesiulo and contributors
// For license information, please see license.txt

frappe.ui.form.on('ATASP Connect User', {
	// refresh: function(frm) {

	// }

	user: async (frm) => {
		//Set the fullname to the name of the selected user
		let user_account = await frappe.db.get_doc('User', frm.doc.user)
		frm.set_value('full_name', user_account.full_name);
	}
});
