# -*- coding: utf-8 -*-
# from odoo import http


# class ProjectDigitalis(http.Controller):
#     @http.route('/project_digitalis/project_digitalis/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/project_digitalis/project_digitalis/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('project_digitalis.listing', {
#             'root': '/project_digitalis/project_digitalis',
#             'objects': http.request.env['project_digitalis.project_digitalis'].search([]),
#         })

#     @http.route('/project_digitalis/project_digitalis/objects/<model("project_digitalis.project_digitalis"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('project_digitalis.object', {
#             'object': obj
#         })
