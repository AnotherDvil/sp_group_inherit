# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CrmWayPay(models.Model):
    _name = 'crm.way'
    _description = 'Forma de pago'

    name = fields.Char(string='Forma de pago')