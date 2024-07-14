# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CrmLeads(models.Model):
    _inherit = 'crm.lead'

    reference = fields.Char(string='Referencia pago')
    total = fields.Float(string='Total')
    subtotal = fields.Float(string='Subtotal', readonly=True)
    comision_percent = fields.Float(string='Porcentaje comisión')
    comision_total = fields.Float(string='Comisión total', readonly=True)
    remaining = fields.Float(string='Restante', readonly=True)
    disponible = fields.Float(string='Disponible', readonly=True)
    remaining2 = fields.Float(string='Restante', readonly=True)
    general_balance = fields.Float(string='Cuadre general', readonly=True)
    total_bill = fields.Float(string='Total factura', readonly=True)

    total_depositar = fields.Float(string="Total a depositar")

    # Conexiones con otros modelos
    # Many2one
    beneficiary = fields.Many2one(string='Beneficiario', comodel_name='res.partner')
    services = fields.Many2one(string="Servicio", comodel_name="crm.services")
    regimen = fields.Many2one(string="Regimen fiscal", comodel_name='crm.regimen')
    cfdi = fields.Many2one(string='Uso de CFDI', comodel_name='crm.cfdi')
    payment_method = fields.Many2one(string='Método de pago', comodel_name='crm.payment')
    waypay = fields.Many2one(string='Forma de pago', comodel_name='crm.way')
    #Many2many
    beneficiario_ids = fields.Many2many('crm.benef', 'leads', string='Beneficiario')
    beneficiario2_ids = fields.Many2many('crm.benef2', 'leads2', string='Beneficiario dos')


    # Métodos
    @api.onchange('total', 'comision_percent')
    def _onchange_calculate_vat(self):
        if self.total:
            self.subtotal = self.total / 1.16
            self.expected_revenue = self.total
        else:
            self.subtotal = 0

    @api.onchange('comision_percent', 'total')
    def _onchange_calculate_percent(self):
        if self.comision_percent and self.total:
            self.comision_total = (self.comision_percent * 0.01) * self.total
        else:
            self.comision_total = 0

    def calculate_disponible(self):
        if self.comision_total and self.total:
            self.disponible = self.total - self.comision_total
        else:
            self.disponible = 0

    @api.onchange('beneficiario_ids', 'comision_percent', 'comision_total')
    def _onchange_calculate_comision_total(self):
        comision_total_count = 0
        if self.beneficiario_ids:
            for record in self.beneficiario_ids:
                abono = record.mount
                comision_total_count += abono

        if self.comision_total:
            self.remaining = self.comision_total - comision_total_count
        elif self.comision_percent:
            self.remaining = self.comision_total
        else:
            self.remaining = 0

        self.calculate_disponible()

    @api.onchange('disponible', 'beneficiario2_ids')
    def _onchange_remaining2(self):
        self.total_depositar = 0
        acumulado = 0
        self.total_bill = 0

        if self.beneficiario2_ids:
            for record in self.beneficiario2_ids:
                abono = record.mount
                self.total_depositar += abono
                acumulado += abono
        
        self.total_bill = acumulado / 0.975

        if self.disponible:
            self.remaining2 = self.disponible - self.total_depositar
        elif self.disponible:
            self.remaining2 = self.disponible
        else:
            self.remaining2 = 0

    @api.onchange('remaining', 'remaining2')
    def _onchange_cuadre(self):
        if self.remaining and self.remaining2:
            self.general_balance = self.remaining2 + self.remaining
        elif self.remaining:
            self.general_balance = self.remaining
        elif self.remaining2:
            self.general_balance = self.remaining2
        else:
            self.general_balance = 0