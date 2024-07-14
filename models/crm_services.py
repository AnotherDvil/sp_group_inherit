# -*- coding: utf-8 -*-

from odoo import models, fields, api

# Modelo creado para el crm
class CrmServices(models.Model):
    _name = 'crm.services'
    _description = 'Servicios CRM'

    name = fields.Char(string="Clave unidad de medida")
    product_services = fields.Char(string="Clave producto servicios")
    description = fields.Char(string="Descripción")