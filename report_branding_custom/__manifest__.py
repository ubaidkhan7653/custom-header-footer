{
    'name': 'Custom Reports Branding',
    'version': '18.0',
    'summary': "Custom PDF template for Sales Quotation and Order with header, footer, and detailed formatting.",
    'description': """
This module provides a fully customized PDF report template for Sale Orders and Quotations in Odoo. 
It includes:

- Custom header with company logo and address
- Professional footer with page numbers, company info, and optional logo
- Order line table with product, description, quantity, unit price, taxes, and subtotal
- Total section with currency formatting and centered amounts
- Optional terms and conditions section
- Designed for clean and professional Sales Quotation and Order PDFs
""",
    "author": "Ubaid Ur Rehman || Leader's Corporate",
    "developer": "Ubaid Ur Rehman || Leader's Corporate",
    "category": "Sales",
    'depends': ['sale','sale_management', 'account', 'accountant'],
    'license': 'LGPL-3',
    'data': [
        'reports/header-footer/custom_header_footer.xml',
        'reports/sale_report_template.xml',
        'reports/sale_order_confirm.xml',
        #
        # 'reports/invoice_report.xml',
        # 'reports/account_payment_report.xml',
        # 'reports/invoice_report_without_payment.xml',


        # 'views/report_action.xml',
        'views/order_views.xml',
    ],
    'images': ['static/description/icon.png'],
    "auto_install": True,
    "application": True,
    "installable": True,
}
