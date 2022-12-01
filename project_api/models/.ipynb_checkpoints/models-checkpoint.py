# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError


class AccountPaymentInherit(models.Model):
    _inherit = 'account.payment'
    
    

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
    
    def action_share_whatsapp(self):
        if not self.partner_id.phone:
            raise UserError(("Mobile Number for this Customer doesn't exist"))
        else:
            msg = 'مرحبا *%s*, ~شكراً لإتمامك لعملية الدفع. إلي* إيصال الدفع * - الذي تبلغ قيمته ~%0.2f من المزرعاوي,\nلا تتردد في التواصل معنا إذا كانت لديك أي أسئلة أو استفسارات.' % (self.partner_id.name,self.amount)
            whatsapp_api_url = "https://web.whatsapp.com/send?phone=%s&text=%s" % (self.partner_id.phone , msg)
        # raise UserError(("Hi Ahmad"))
        
        
        
        return {
           'type' : 'ir.actions.act_url',
           'target' : 'new',
           'url' : whatsapp_api_url
        }
        
