# Copyright (c) 2022, Pointershub and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class PropertyAllocation(Document):
    def before_submit(self):
        if self.unit_no:
            frappe.db.set_value('Property Unit', self.unit_no, {
                'allocated_to': self.customer,
                'allocation_date': self.posting_date,
                'allocation_no': self.name
            })

    def before_cancel(self):
        if self.unit_no:
            frappe.db.set_value('Property Unit', self.unit_no, {
                'allocated_to': "",
                'allocation_date': None,
                'allocation_no': ""
            })
