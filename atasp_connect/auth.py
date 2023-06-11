import frappe
from frappe import _

def validate():
    logged_in_user = frappe.session.user
    if(not (logged_in_user == "Guest" or logged_in_user == "Administrator")):
        try:
            user_account = frappe.get_doc('User', logged_in_user)
            atasp_connect_user = frappe.get_doc('ATASP Connect User', logged_in_user)
            frappe.response["email"] = user_account.email
            frappe.response["role"] = user_account.role_profile_name
            frappe.response["zone"] = atasp_connect_user.zone
        except Exception as e:
            error_message = _("Your ATASP Connect Account is not active")
            frappe.local.login_manager.logout()
            frappe.response.clear()
            frappe.response["error"] = error_message
            #frappe.throw(error_message)
            