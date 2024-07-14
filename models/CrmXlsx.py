# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
import logging

class CrmXlsx(models.AbstractModel):
    _name = 'report.sp_group_inherit.report_crm_custom_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, leads):
        sheet = workbook.add_worksheet('CRM Report')

        # Define formatos
        bold = workbook.add_format({'bold': True, 'bg_color': '#FFFF00'})
        bold_black = workbook.add_format({'bold': True, 'bg_color': '#FFFF00', 'font_color': '#000000'})

        # Declara el nombre de las filas
        headers = ['CONSEC.', 'CLABE INTERBANCARIA', 'CÓDIGO BANCO', 'NOMBRE', 'IMPORTE']
        for col_num, header in enumerate(headers):
            if header == 'NOMBRE':
                sheet.write(0, col_num, header, bold_black)
            else:
                sheet.write(0, col_num, header, bold)

        # Escribimos la data
        row_num = 1
        for lead in leads:
            for line in lead.beneficiario_ids:
                sheet.write(row_num, 0, row_num)
                sheet.write(row_num, 1, line.clabe if line else '')
                sheet.write(row_num, 2, line.bank_code if line else '')
                sheet.write(row_num, 3, line.name if line.beneficiario else '')
                sheet.write(row_num, 4, line.mount if line else 0)
                row_num += 1
            for line in lead.beneficiario2_ids:
                sheet.write(row_num, 0, row_num)
                sheet.write(row_num, 1, line.clabe if line else '')
                sheet.write(row_num, 2, line.bank_code if line else '')
                sheet.write(row_num, 3, line.name if line.beneficiario else '')
                sheet.write(row_num, 4, line.mount if line else 0)
                row_num += 1

        # Set column widths
        sheet.set_column(0, 0, 10)
        sheet.set_column(1, 1, 20)
        sheet.set_column(2, 2, 15)
        sheet.set_column(3, 3, 30)
        sheet.set_column(4, 4, 10)