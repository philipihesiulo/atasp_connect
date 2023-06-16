import frappe

@frappe.whitelist()
def get_total_targets_achieved():
    return {
        "value": 500,
        "fieldtype": "Int"
    }