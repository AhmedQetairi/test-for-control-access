# -*- coding: utf-8 -*-
# from odoo import http


# class PartnersLimit(http.Controller):
#     @http.route('/partners_limit/partners_limit', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/partners_limit/partners_limit/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('partners_limit.listing', {
#             'root': '/partners_limit/partners_limit',
#             'objects': http.request.env['partners_limit.partners_limit'].search([]),
#         })

#     @http.route('/partners_limit/partners_limit/objects/<model("partners_limit.partners_limit"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('partners_limit.object', {
#             'object': obj
#         })
