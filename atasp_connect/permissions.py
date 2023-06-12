import frappe

def quarterly_performance_query(user):
    if not user:
        user = frappe.session.user
    if user != 'Administrator':
        atasp_connect_user = frappe.get_doc('ATASP Connect User', user)
        zone = atasp_connect_user.zone
        role = atasp_connect_user.role
        super_admin_roles = ['National Programme Coordinator', 'National M&E Officer']
        if role not in super_admin_roles:
            return "(`tabQuarterly Performance`.zone = {zone})".format(zone=frappe.db.escape(zone))


def zone_query(user):
    if not user:
        user = frappe.session.user
    if user != 'Administrator':
        atasp_connect_user = frappe.get_doc('ATASP Connect User', user)
        zone = atasp_connect_user.zone
        role = atasp_connect_user.role
        if role != 'National M&E Officer':
            return "(`tabZone`.zone_name = {zone})".format(zone=frappe.db.escape(zone))

def role_query(user):
    if not user:
        user = frappe.session.user
    if user != 'Administrator':
        is_custom = 1
        return "(`tabRole`.is_custom = {is_custom})".format(is_custom=frappe.db.escape(is_custom))