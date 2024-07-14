# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CrmCfdi(models.Model):
    _name = 'crm.cfdi'
    _description = 'Uso CFDI'

    name = fields.Char(string='Uso de CFDI')