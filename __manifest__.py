# -*- coding: utf-8 -*-
{
    'name': "sp_group_inherit",
    'summary': "Modulo desarrollado para la herencia dentro de CRM y Empleados",
    'description': "Modulo desarrollado para la herencia dentro de CRM y Empleados",
    'author': "Ángel López",
    'category': 'CRM',
    'version': '2.1',
    # any module necessary for this one to work correctly
    'depends': [ 'base', 'report_xlsx', 'crm', 'hr' ],
    # always loaded
    'data': [
        'reports/report_dispersion.xml',
        'reports/report_internos.xml',
        'reports/report_pago_interno_factura.xml',
        'reports/report_pago_externo.xml',
        'reports/report_pago_interno_dispersion.xml',
        'security/crm_security.xml',
        'security/ir.model.access.csv',
        'views/crm_lead.xml',
        'views/crm_benef.xml',
        'views/crm_benef2.xml',
        'views/res_partner_inherit.xml',
        'views/template_pago_interno_factura.xml',
        'views/template_pago_interno_dispersion.xml',
        'views/template_pago_externo.xml',
    ],
}