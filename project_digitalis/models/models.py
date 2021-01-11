# -*- coding: utf-8 -*-

from odoo import models, fields, api

class EstadoCliente(models.Model):
    _name = 'project_digitalis.state'
    _description = 'Gestiona los posibles estados para los clientes'

    name = fields.Char(string='Estado', required=True)
    description = fields.Char(string='Descripcion')

    _sql_constraints = [
        ('name_unique',
         'UNIQUE(name)',
         "Ya existe un estado con el mismo nombre")    ]

class StatePartner(models.Model):
    _inherit = "res.partner"
    _description = 'Agrega Atributo Conduce Viveros'

    state = fields.Many2one('project_digitalis.state', string='Estado')

    

# class project_digitalis(models.Model):
#     _name = 'project_digitalis.project_digitalis'
#     _description = 'project_digitalis.project_digitalis'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
