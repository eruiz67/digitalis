# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class EstadoCliente(models.Model):
    _name = 'project_digitalis.state'
    _description = 'Gestiona los posibles estados para los clientes'

    name = fields.Char(string='Estado', required=True)
    description = fields.Char(string='Descripcion')

    partner_id = fields.Many2one('res.partner', string='Compañia', required=True, domain="[('is_company','=',True)]")

    _sql_constraints = [
        ('name_unique',
         'UNIQUE(name)',
         "Ya existe un estado con el mismo nombre")    ]

    
class ProjectPartners(models.Model):
    _inherit ="project.project"
    _description = 'Permite adicionar clientes a los proyectos'

    partner_state_ids = fields.One2many('project_digitalis.partner_state', 'project_id', string='Clientes') 

    
    @api.constrains('partner_state_ids')
    def _constrains_partner_state_ids(self):        
        for i in range(0, len(self.partner_state_ids)-1):
            for j in range(i+1,len(self.partner_state_ids)):
                if self.partner_state_ids[i].partner_id == self.partner_state_ids[j].partner_id:
                    raise ValidationError("El cliente '{}' se ha adicionado más de una vez. Elimine los clientes repetidos para el mismo proyecto".format(self.partner_state_ids[j].partner_id.name)) 


    partner_count = fields.Integer(compute='_compute_partner_count', string='Cantidad Clientes')
    label_partner_count = fields.Char(string='Para clientes', compute='_compute_partner_count', default='Cliente(s)')
    
    
    @api.depends('partner_state_ids')
    def _compute_partner_count(self):
        for rec in self:
            rec.partner_count = len(rec.partner_state_ids)
            if len(rec.partner_state_ids) == 1:
                rec.label_partner_count="Cliente"
            else:
                rec.label_partner_count="Clientes"

    def action_view_partners(self):
        action = self.with_context(active_id=self.id, active_ids=self.ids) \
            .env.ref('project_digitalis.act_project_partner_tree_view') \
            .sudo().read()[0]
        action['display_name'] = self.name
        return action

class PartnerSate(models.Model):
    _name = 'project_digitalis.partner_state'
    _description = 'Permite adicionar un cliente a u proyecto con un estado determinado'

    partner_id = fields.Many2one('res.partner', string='Cliente', required=True)
    state_id = fields.Many2one('project_digitalis.state', string='Estado', required=True, help="Solamente se pueden poner los estados definidos para la compañia del cliente")
    project_id = fields.Many2one('project.project', string='Proyecto')

    def name_get(self):
        result = []
        for rec in self:
            name = rec.project_id.name +" - "+ rec.partner_id.name
            result.append((rec.id, name))
        return result

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        self.state_id = False
        if self.partner_id.is_company:
            return {'domain':{'state_id':[('partner_id','=',self.partner_id.id)]}}
        else:
            return {'domain':{'state_id':[('partner_id','=',self.partner_id.parent_id.id)]}}

    
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
