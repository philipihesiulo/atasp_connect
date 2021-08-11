from __future__ import unicode_literals

import frappe


@frappe.whitelist(allow_guest=True)
def sample(): 
    return "Reached"

@frappe.whitelist(allow_guest=True)
def login(usr,pwd):
    try:
        login_manager = frappe.auth.LoginManager()
        login_manager.authenticate(user=usr,pwd=pwd)
        login_manager.post_login()
    except frappe.exceptions.AuthenticationError:
        frappe.clear_messages()
        frappe.local.response["message"] =  {
            "success_key":0,
            "message":"Authentication Failed"
            }
        return

    api_generate=generate_keys(frappe.session.user)
    user = frappe.get_doc('User',frappe.session.user)
 
    frappe.response["message"] =	{
            "success_key": 1,
            "message":"Authentication Success",
            "sid": frappe.session.sid,
            "api_key":user.api_key,
            "api secret": api_generate
            }
    return

def generate_keys(user):
    user_details = frappe.get_doc('User', user)
    api_secret = frappe.generate_hash(length=15)
    # if api key is not set, generate api key
    if not user_details.api_key:
        api_key = frappe.generate_hash(length=15)
        user_details.api_key = api_key
    user_details.api_secret = api_secret
    user_details.save()
    return api_secret