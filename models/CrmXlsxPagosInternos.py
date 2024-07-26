# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
import xlsxwriter
import logging

class CrmXlsx(models.AbstractModel):
    _name = 'report.sp_group_inherit.report_crm_custom_xlsx_pagos_internos'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, leads):
        # Creación de una nueva hoja de cálculo en el workbook
        sheet = workbook.add_worksheet('Factura Estandar')

        # Definición de formatos de celdas
        header_format = workbook.add_format({
            'bold': True,
            'font_size': 14,
            'align': 'center',
            'bg_color': '#2D5A9B',
            'font_color': '#FFFFFF'
        })
        bold = workbook.add_format({'bold': True})
        bold_blue = workbook.add_format({'bold': True, 'font_color': '#0000FF'})
        letter_blue = workbook.add_format({'font_color': '#0000FF'})
        currency_format = workbook.add_format({'num_format': '#,##0.00'})
        border_format = workbook.add_format({'border': 1})
        merge_format = workbook.add_format({
            'align': 'center',
            'valign': 'vcenter',
            'bold': True,
            'bg_color': '#D3D3D3'
        })
        cell_format = workbook.add_format({
            'font_size': 8, 'align': 'center'
        })
        table_format = workbook.add_format({
            'align': 'center',
            'bg_color': '#CBCBCB',
            'font_size': 8
        })
        response_format = workbook.add_format({
            'border': 1
        })

        # Ajuste de columnas y filas
        col_widths = [2] * 50  # Ancho pequeño para todas las columnas
        for i, width in enumerate(col_widths):
            sheet.set_column(i, i, width)

        # Ajuste de altura de las filas (Aquí es donde se ajusta la altura de las filas)
        for row in range(100):  # Ajusta un número grande de filas
            sheet.set_row(row, 20)  # Ajusta la altura de las filas a 20 puntos (puedes cambiar este valor según sea necesario)

        # Título
        sheet.merge_range('A1:AK1', 'FACTURA ESTANDAR', header_format)

        # Encabezados
        sheet.merge_range('A2:D2', 'EMISOR', bold_blue)
        sheet.merge_range('S2:V2', 'RECEPTOR', bold_blue)

        for lead in leads:
            empresasp = lead.mrk_beneficiary
            receptor = lead.partner_id

            # Formato del emisor
            sheet.merge_range('A3:D3', 'Razón social', letter_blue)
            sheet.write('A4', empresasp.name or '')
            sheet.merge_range('A5:D5', 'RFC', letter_blue)
            sheet.write('A6', empresasp.vat or '')
            sheet.merge_range('J5:M5', 'Teléfono', letter_blue)
            sheet.write('J6', empresasp.phone or '')
            sheet.merge_range('A7:J7', 'Calle (No. Exterior e interior)', letter_blue)
            sheet.write('A8', empresasp.street or '')
            # sheet.merge_range('J7:L7', 'No. exterior', letter_blue)
            # sheet.write('J8', empresasp.street2 or '')
            # sheet.merge_range('N7:P7', 'No. interior', letter_blue)
            # sheet.write('N8', empresasp.mobile or '')
            sheet.merge_range('A9:D9', 'Colonia', letter_blue)
            sheet.write('A10', empresasp.street2 or '')
            sheet.merge_range('J9:L9', 'C.P.', letter_blue)
            sheet.write('J10', empresasp.zip or '')
            sheet.merge_range('A11:D11', 'Municipio', letter_blue)
            sheet.write('A12', empresasp.city or '')
            sheet.merge_range('J11:M11', 'Estado', letter_blue)
            sheet.write('J12', empresasp.mrk_estado or '')
            sheet.merge_range('A13:D13', 'País', letter_blue)
            sheet.write('A14', empresasp.country_id.name or '')
            sheet.merge_range('J13:M13', 'Localidad', letter_blue)
            sheet.write('J14', empresasp.mrk_localidad or '')
            sheet.merge_range('A15:D15', 'e.mail', letter_blue)
            sheet.write('A16', empresasp.email or '')
            sheet.merge_range('J15:M15', 'Régimen Fiscal', letter_blue)
            sheet.write('J16', lead.mrk_regimen or '')
            sheet.merge_range('A17:E17', 'Método de Pago', letter_blue)
            sheet.write('A18', lead.mrk_payment_method or '')
            sheet.merge_range('J17:N17', 'Forma de Pago', letter_blue)
            sheet.write('J18', lead.mrk_waypay or '')

            # Formato del receptor
            sheet.merge_range('S3:V3', 'Razón social', letter_blue)
            sheet.write('S4', receptor.name or '')
            sheet.merge_range('S5:V5', 'RFC', letter_blue)
            sheet.write('S6', receptor.vat or '')
            sheet.merge_range('AD5:AG5', 'Teléfono', letter_blue)
            sheet.write('AD6', receptor.phone or '')
            sheet.merge_range('S7:AB7', 'Calle (No. exterior e interior)', letter_blue)
            sheet.write('S8', receptor.street or '')
            # sheet.merge_range('AD7:AF7', 'No. exterior', letter_blue)
            # sheet.write('AD8', receptor.street2 or '')
            # sheet.merge_range('AH7:AJ7', 'No. interior', letter_blue)
            # sheet.write('AH8', receptor.mobile or '')
            sheet.merge_range('S9:V9', 'Colonia', letter_blue)
            sheet.write('S10', receptor.street2 or '')
            sheet.merge_range('AD9:AF9', 'C.P.', letter_blue)
            sheet.write('AD10', receptor.zip or '')
            sheet.merge_range('S11:V11', 'Municipio', letter_blue)
            sheet.write('S12', receptor.city or '')
            sheet.merge_range('AD11:AF11', 'Estado', letter_blue)
            sheet.write('AD12', receptor.mrk_estado or '')
            sheet.merge_range('S13:V13', 'País', letter_blue)
            sheet.write('S14', receptor.country_id.name or '')
            sheet.merge_range('AD13:AG13', 'Localidad', letter_blue)
            sheet.write('AD14', receptor.mrk_localidad or '')
            sheet.merge_range('S15:V15', 'e.mail', letter_blue)
            sheet.write('S16', receptor.email or '')
            sheet.merge_range('AD15:AG15', 'Uso del CFDI', letter_blue)
            sheet.write('AD16', lead.mrk_cfdi or '')
            sheet.merge_range('S17:V17', 'Observaciones', letter_blue)
            sheet.write('S18', lead.description or '')
            sheet.merge_range('Y17:AB17', 'Referencia pago', letter_blue)
            sheet.write('Y18', lead.mrk_reference or '')
            sheet.merge_range('AD17:AF17', 'Total', letter_blue)
            sheet.write('AD18:AE18', lead.mrk_total or '', cell_format)

            # Tabla de detalles de la factura
            sheet.merge_range('A20:C20', 'Cantidad', table_format)
            sheet.merge_range('D20:G20', 'Clave Unid Medida', table_format)
            sheet.merge_range('H20:J20', 'Clave Prod Servicios', table_format)
            sheet.merge_range('K20:U20', 'Descripción', table_format)
            sheet.merge_range('V20:Z20', 'Precio Unitario', table_format)
            sheet.merge_range('AA20:AD20', 'Impuesto', table_format)
            sheet.merge_range('AE20:AG20', 'Tasa', table_format)
            sheet.merge_range('AH20:AK20', 'Total Línea', table_format)

            for line in lead.mrk_services:
                sheet.write('A21:C21', '1', cell_format)
                sheet.write('D21:G20', line.name if line else '', cell_format)
                sheet.write('H21:J21', line.product_services if line else '', cell_format)
                sheet.write('K21:U21', line.description if line else '', cell_format)
            
                sheet.write('AA21:AD21', 'IVA', cell_format)
                sheet.write('AE21:AG21', '16%', cell_format)

            sheet.write('V21:Z21', lead.mrk_subtotal, cell_format)
            sheet.write('AH21:AK21', lead.mrk_total, cell_format)

            # Total
            sheet.merge_range('AF24:AG24', 'Total', bold_blue)
            sheet.write('AI24:AK24', lead.mrk_total or '', cell_format)