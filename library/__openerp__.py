# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Library Management',
    'version': '2.2',
    'author': 'Serpent Consulting Services PVT. LTD.',
    'category': 'School Management',
    'website': 'http://www.serpentcs.com',
    'license': '',
    'summary': 'A Module For Library Management For School',
    'complexity': 'easy',
    'depends': ['report_intrastat', 'mrp', 'delivery', 'school'],
    'demo': ['demo/library_demo.xml'],
    'data': [
             'security/library_security.xml',
             'security/ir.model.access.csv',
             'views/report_view.xml',
             'views/qrcode_label.xml',
             'views/library_data.xml',
             'views/library_view.xml',
             'views/library_issue_workflow.xml',
             'views/library_sequence.xml',
             'views/library_workflow.xml',
             'views/library_category_data.xml',
             'wizard/update_prices_view.xml',
             'wizard/update_book_view.xml',
             'wizard/book_issue_no_view.xml',
             'wizard/card_no_view.xml',
            ],
    'installable': True,
    'application': True,
}
