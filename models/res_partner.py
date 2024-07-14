# -*- coding: utf-8 -*-

from odoo import models, fields, api

class res_partner_inherit(models.Model):
    _inherit = 'res.partner'

    localidad = fields.Char(string='Localidad')
    estado = fields.Selection([
        ('Aguascalientes', 'Aguascalientes'),
        ('Baja California', 'Baja California'),
        ('Baja California Sur', 'Baja California Sur'),
        ('Campeche', 'Campeche'),
        ('Chiapas', 'Chiapas'),
        ('Chihuahua', 'Chihuahua'),
        ('Coahuila', 'Coahuila'),
        ('Colima', 'Colima'),
        ('Ciudad de México', 'Ciudad de México'),
        ('Durango', 'Durango'),
        ('Guanajuato', 'Guanajuato'),
        ('Guerrero', 'Guerrero'),
        ('Hidalgo', 'Hidalgo'),
        ('Jalisco', 'Jalisco'),
        ('México', 'México'),
        ('Michoacán', 'Michoacán'),
        ('Morelos', 'Morelos'),
        ('Nayarit', 'Nayarit'),
        ('Nuevo León', 'Nuevo León'),
        ('Oaxaca', 'Oaxaca'),
        ('Puebla', 'Puebla'),
        ('Querétaro', 'Querétaro'),
        ('Quintana Roo', 'Quintana Roo'),
        ('San Luis Potosí', 'San Luis Potosí'),
        ('Sinaloa', 'Sinaloa'),
        ('Sonora', 'Sonora'),
        ('Tabasco', 'Tabasco'),
        ('Tamaulipas', 'Tamaulipas'),
        ('Tlaxcala', 'Tlaxcala'),
        ('Veracruz', 'Veracruz'),
        ('Yucatán', 'Yucatán'),
        ('Zacatecas', 'Zacatecas')
    ], string='Estado')