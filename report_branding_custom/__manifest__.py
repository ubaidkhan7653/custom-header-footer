
{
    'name': 'Custom Reports Branding',
    'version': '20.0.1.0.0',
    'summary': 'Custom PDF templates for Sales Quotations and Orders with professional header, footer, and formatting.',
    'description': """
Custom PDF report templates for Sales Orders and Quotations in Odoo 20.

Features:
- Custom header with company logo and address
- Professional footer with page numbers and company information
- Customized Sales Quotation and Sales Order PDF reports
- Detailed order line table with product, quantity, price, and taxes
- Clean and professional totals section
- Currency formatting
- Optional terms and conditions section
- Responsive and professional report layout
""",
    'author': 'Ubaid Ur Rehman',
    'website': 'https://ubaid-dev.netlify.app/',
    'price': 30.00,
    'currency': 'USD',
    'category': 'Sales',
    'license': 'LGPL-3',

    'depends': [
        'sale',
        'sale_management',
        'account',
    ],

    'data': [
        'reports/header-footer/custom_header_footer.xml',
        # 'views/report_action.xml',
    ],

    'assets': {
        'web.assets_backend': [
            'report_branding_custom/static/src/css/style.css',
        ],
    },

    'images': [
        'static/description/banner.png',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
