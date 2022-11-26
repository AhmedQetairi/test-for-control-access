# -*- coding: utf-8 -*-
# from odoo import http


# class ProjectApi(http.Controller):
#     @http.route('/project_api/project_api', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

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
