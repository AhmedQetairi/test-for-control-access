# -*- coding: utf-8 -*-
from odoo import http


class Odoocontroller(http.Controller):
    
    @http.route('/odoo_controller/odoo_controller', auth='public')
    def index(self, **kw):
        try:
            payments = http.request.env['account.payment'].search([])
        except:
            return "can't accessed"
        
        output = "<h1> Sales Orders </h1><ul>"
        for sale in payments:
            output += '<li>' + sale['name'] + '</li>'
        output += '</ul>'
        
        return output

#     @http.route('/project_api/project_api/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('project_api.listing', {
#             'root': '/project_api/project_api',
#             'objects': http.request.env['project_api.project_api'].search([]),
#         })

#     @http.route('/project_api/project_api/objects/<model("project_api.project_api"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('project_api.object', {
#             'object': obj
#         })
