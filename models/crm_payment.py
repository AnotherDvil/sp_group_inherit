# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CrmPayment(models.Model):
    _name = 'crm.payment'
    _description = 'Método de pago'

    name = fields.Char(string='Método de pago')
