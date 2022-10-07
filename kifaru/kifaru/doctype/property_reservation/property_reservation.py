# Copyright (c) 2022, Pointershub and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class PropertyReservation(Document):
	def before_submit(self):
		if self.unit_no:
			frappe.db.set_value('Property Unit', self.unit_no, {
					'status': 'Booked',
					'reservation_status': "Booked",
					'reserved_by': self.customer,
					'reservation_date': self.posting_date,
					'reservation_no': self.name
				})

	def before_cancel(self):
		if self.unit_no:
			frappe.db.set_value('Property Unit', self.unit_no, {
					'status': 'Available',
					'reservation_status': "",
					'reserved_by': "",
					'reservation_date': None,
					'reservation_no': ""
				})
