# -*- coding: utf-8 -*-
# from odoo import http


# class DynamicAccountsReport(http.Controller):
#     @http.route('/dynamic_accounts_report/dynamic_accounts_report', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dynamic_accounts_report/dynamic_accounts_report/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('dynamic_accounts_report.listing', {
#             'root': '/dynamic_accounts_report/dynamic_accounts_report',
#             'objects': http.request.env['dynamic_accounts_report.dynamic_accounts_report'].search([]),
#         })

#     @http.route('/dynamic_accounts_report/dynamic_accounts_report/objects/<model("dynamic_accounts_report.dynamic_accounts_report"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dynamic_accounts_report.object', {
#             'object': obj
#         })
