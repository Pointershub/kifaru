// Copyright (c) 2022, Pointershub and contributors
// For license information, please see license.txt
var fields = ["customer", "customer_name", "national_id", "phone_no", "email", "postal_address", "kin_full_name", "kin_national_id", "kin_phone_no", "kin_email", "relationship", "kin_postal_address", "project_name", "unit_no", "cost_of_unit", "cost_agreed_upon", "sales_rep", "date_of_purchase"]

frappe.ui.form.on('Property Allocation', {
    reservation_no: function(frm){
        if(frm.doc.reservation_no){
             frappe.db.get_doc("Property Reservation", frm.doc.reservation_no)
                                .then(doc => {
                                    for(var m = 0; m < fields.length; m++){
                                        frm.set_value(String(fields[m]), doc[fields[m]])
                                    }

                                });

        }
    }
});
