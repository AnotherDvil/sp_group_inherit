# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CrmLeads(models.Model):
    _inherit = 'crm.lead'

    mrk_reference = fields.Char(string='Referencia pago')
    mrk_total = fields.Float(string='Total')
    mrk_subtotal = fields.Float(string='Subtotal', readonly=True)
    mrk_comision_percent = fields.Float(string='Porcentaje comisión')
    mrk_comision_total = fields.Float(string='Comisión total', readonly=True)
    mrk_remaining = fields.Float(string='Restante', readonly=True)
    mrk_disponible = fields.Float(string='Disponible', readonly=True)
    mrk_remaining2 = fields.Float(string='Restante', readonly=True)
    mrk_general_balance = fields.Float(string='Cuadre general', readonly=True)
    mrk_total_bill = fields.Float(string='Total factura', readonly=True)

    mrk_total_depositar = fields.Float(string="Total a depositar")

    # Conexiones con otros modelos
    # Many2one
    mrk_beneficiary = fields.Many2one(string='Beneficiario', comodel_name='res.partner')
    mrk_services = fields.Many2one(string="Servicio", comodel_name="crm.services")
    mrk_regimen = fields.Many2one(string="Regimen fiscal", comodel_name='crm.regimen')
    mrk_cfdi = fields.Many2one(string='Uso de CFDI', comodel_name='crm.cfdi')
    mrk_payment_method = fields.Many2one(string='Método de pago', comodel_name='crm.payment')
    mrk_waypay = fields.Many2one(string='Forma de pago', comodel_name='crm.way')
    #Many2many
    mrk_beneficiario_ids = fields.Many2many('crm.benef', 'leads', string='Beneficiario')
    mrk_beneficiario2_ids = fields.Many2many('crm.benef2', 'leads2', string='Beneficiario dos')


    # Métodos
    @api.onchange('mrk_total', 'mrk_comision_percent')
    def _onchange_calculate_vat(self):
        if self.mrk_total:
            self.mrk_subtotal = self.mrk_total / 1.16
            self.expected_revenue = self.mrk_total
        else:
            self.mrk_subtotal = 0

    @api.onchange('mrk_comision_percent', 'mrk_total')
    def _onchange_calculate_percent(self):
        if self.mrk_comision_percent and self.mrk_total:
            self.mrk_comision_total = (self.mrk_comision_percent * 0.01) * self.mrk_total
        else:
            self.mrk_comision_total = 0

    def calculate_disponible(self):
        if self.mrk_comision_total and self.mrk_total:
            self.mrk_disponible = self.mrk_total - self.mrk_comision_total
        else:
            self.mrk_disponible = 0

    @api.onchange('mrk_beneficiario_ids', 'mrk_comision_percent', 'mrk_comision_total')
    def _onchange_calculate_comision_total(self):
        comision_total_count = 0
        if self.mrk_beneficiario_ids:
            for record in self.mrk_beneficiario_ids:
                abono = record.mount
                comision_total_count += abono

        if self.mrk_comision_total:
            self.mrk_remaining = self.mrk_comision_total - comision_total_count
        elif self.mrk_comision_percent:
            self.mrk_remaining = self.mrk_comision_total
        else:
            self.mrk_remaining = 0

        self.calculate_disponible()

    @api.onchange('mrk_disponible', 'mrk_beneficiario2_ids')
    def _onchange_remaining2(self):
        self.mrk_total_depositar = 0
        acumulado = 0
        self.mrk_total_bill = 0

        if self.mrk_beneficiario2_ids:
            for record in self.mrk_beneficiario2_ids:
                abono = record.mount
                self.mrk_total_depositar += abono
                acumulado += abono
        
        self.mrk_total_bill = acumulado / 0.975

        if self.mrk_disponible:
            self.mrk_remaining2 = self.mrk_disponible - self.mrk_total_depositar
        elif self.mrk_disponible:
            self.mrk_remaining2 = self.mrk_disponible
        else:
            self.mrk_remaining2 = 0

    @api.onchange('mrk_remaining', 'mrk_remaining2')
    def _onchange_cuadre(self):
        if self.mrk_remaining and self.mrk_remaining2:
            self.mrk_general_balance = self.mrk_remaining2 + self.mrk_remaining
        elif self.mrk_remaining:
            self.mrk_general_balance = self.mrk_remaining
        elif self.mrk_remaining2:
            self.mrk_general_balance = self.mrk_remaining2
        else:
            self.mrk_general_balance = 0