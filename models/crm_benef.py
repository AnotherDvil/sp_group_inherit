# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CrmBenef(models.Model):
    _name = 'crm.benef'
    _description = 'CRM Beneficiarios'

    name = fields.Char(string="Beneficiario")
    bank = fields.Many2one(string='Banco', comodel_name='crm.banco')
    bank_code = fields.Char(string="Código banco", readonly=True, store=True, compute='_get_bank_code')
    clabe = fields.Char(string="No. Cuenta, CLABE, no. tarjeta")
    percent = fields.Float(string="Porcentaje")
    mount = fields.Float(string="Monto")

    leads = fields.Many2one(string='Leads', comodel_name='crm.lead')

    @api.depends('bank')
    def _get_bank_code(self):
        self.bank_code = self.bank.bank_code