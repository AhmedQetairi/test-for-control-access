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
        if self.partner_id.phone:
            
       
            msg = 'Hello you are welcome'
            # whatsapp_api_url = "https://api.whatsapp.com/send?" 
            raise ValidationError(("Hi Ahmad"))
        
        
        
        return {
           'type' : 'ir.actions.act_url',
           'target' : 'new',
           # 'url' : whatsapp_api_url
        }
        
