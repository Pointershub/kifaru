// Copyright (c) 2022, Pointershub and contributors
// For license information, please see license.txt

frappe.ui.form.on('Property Reservation', {
      onload: function(frm) {
          frm.set_query("unit_no", function () {
              return {
                  "filters": [
                      // ["Property Unit", "reservation_status", "=", "Available"],
                      ["Property Unit", "status", "=", "Available"]
                  ]
              }
          });
      }
});
