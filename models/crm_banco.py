# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CrmBanco(models.Model):
    _name = 'crm.banco'
    _description = 'CRM banco'

    name = fields.Char(string='Banco')
    bank_code = fields.Char(string='Código')

    @api.onchange('name')
    @api.depends('name')
    def _onchange_bank(self):
        bank_codes = {
            'BANCOMER': 'BACOM',
            'BANAMEX': 'BANAM',
            'SCOTIABANK': 'COMER',
            'BANCOPPEL': 'COPPEL',
            'BANCO AZTECA': 'BAZTE',
            'BANORTE': 'BBANO',
            'HSBC': 'BITAL',
            'BANSI': 'BANSI',
            'BAJIO': 'BAJIO',
            'BANOBRAS': 'BOBRA',
            'BANJERCITO': 'BEJER',
            'MIFEL': 'MIFEL',
            'AFIRME': 'BAFIR',
            'BANCO MULTIVA': 'MULTI',
            'BANCO COMPARTAMOS': 'BCOMP',
            'STP FONDEADORA': 'STP'
        }
        # Convierte el valor de 'banco' a mayúsculas para asegurar la coincidencia
        upper_field = self.name if self.name else ''
        self.bank_code = bank_codes.get(upper_field.upper(), '')