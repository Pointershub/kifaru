import frappe
from frappe import _, throw
import erpnext


@frappe.whitelist(allow_guest=True)
def custom(data=None):
    d = frappe.request.data
    frappe.throw("{} <br> Check data {} <br>".format(data, d ))