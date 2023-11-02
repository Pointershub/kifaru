# Copyright (c) 2023, Pointershub and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import requests
import random
import json
import hashlib
import base64


class AirtimeDistribution(Document):
	def before_save(self):
		if self.get("items"):
			recipients = []
			for d in self.get("items"):
				if float(d.amount) < 10:
					frappe.throw("You cannot send less than 10 shillings")
				recipients.append({
					"recipient": str(d.mobile),
					"amount": d.amount
				})

			description_results = send_airtime(recipients)
			self.results = description_results


@frappe.whitelist()
def send_airtime(recipients):
	data = {
		"recipients": recipients
	}

	headers = {
		'Content-Type': 'application/json',
		'App-Key': 'f4318bee-a8f7-4627-aeca-2366bd179c45',
		'App-Token': 'M5aX005MP9k7ntmZKOh1fWG2GfCSvkjm'
	}

	URL = "https://quicksms.advantasms.com/api/v3/airtime/send"

	description = ""
	try:
		response = requests.post(URL, data=json.dumps(data), headers=headers)
		if response.status_code == 200:
			response_data = response.json()

			for result in response_data.get('results', []):
				description += f"Recipient: {result.get('recipient', 'N/A')}, Amount: {result.get('amount', 'N/A')}, Message: {result.get('message', 'N/A')}\n"

			return description.strip()
		else:
			return "Failed to send airtime"
	except requests.RequestException as e:
		description = f"ERROR on URL[{URL}] | error[{str(e)}]"
		return description.strip()
