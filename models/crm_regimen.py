# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CrmRegimen(models.Model):
    _name = 'crm.regimen'
    _description = 'Regimen Fiscal'

    name = fields.Char(string='Regimen fiscal')