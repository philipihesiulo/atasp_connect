import frappe
from frappe import _

def validate():
    logged_in_user = frappe.session.user
    error_message = ""
    if(not (logged_in_user == "Guest" or logged_in_user == "Administrator")):
        try:
            user_account = frappe.get_doc('User', logged_in_user)
            atasp_connect_user = frappe.get_doc('ATASP Connect User', logged_in_user)
            frappe.response["email"] = user_account.email
            frappe.response["zone"] = atasp_connect_user.zone
            role_profile = user_account.role_profile_name
        
            if role_profile == "" or role_profile == None:
                error_message = _("A role has not been set for your account")
                frappe.throw(error_message)
            else:
                frappe.response["role"] = role_profile
                
        except Exception as e:
            error_message = error_message if error_message != "" else _("Your ATASP Connect Account is not active")
            frappe.local.login_manager.logout()
            frappe.response.clear()
            frappe.response["message"] = error_message
            #frappe.throw(error_message)
            