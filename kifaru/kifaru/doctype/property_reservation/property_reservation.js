// Copyright (c) 2022, Pointershub and contributors
// For license information, please see license.txt

frappe.ui.form.on('Property Reservation', {
      onload: function(frm) {
          frm.set_query("unit_no", function () {
              return {
                  "filters": [
                      ["Property Unit", "status", "=", "Available"]
                  ]
              }
          });
      },
    refresh: function(frm){
          if(frm.doc.docstatus == 1){
              frm.add_custom_button(__("Property Allocation"), function() {
			            frappe.set_route("Form", "Property Allocation",
			                {
			                    "reservation_no": frm.doc.name
			                });
			            }, __("Create")).addClass("btn-primary");
          }
    }
});
