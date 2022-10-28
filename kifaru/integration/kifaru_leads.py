import frappe
from frappe import _, throw
import erpnext
import urllib.parse


@frappe.whitelist(allow_guest=True)
def custom(random_string=""):
    x = str(frappe.request.data, 'utf-8')
    if x:
        data = urllib.parse.parse_qs(str(x))
        make_lead_from_website_checked(data)


def make_lead_from_website_checked(data):
    data_items = {"fullName": "", "email": "", "phone": "", "scheduleDate": "", "message": ""}
    for di in data:
        data_items[di] = data[di][0]

    site_visit = (" Site Visit on " + data_items["scheduleDate"]) if data_items["scheduleDate"] != "" else ""
    doc = frappe.new_doc("Lead")
    doc.first_name = data_items["fullName"]
    doc.lead_name = data_items["fullName"]
    doc.email_id = data_items["email"]
    doc.mobile_no = data_items["phone"]
    doc.lead_owner = ""
    doc.lead_request = data_items["message"] + site_visit
    doc.source = "Website"
    doc.insert(ignore_permissions=True, ignore_mandatory=True)
