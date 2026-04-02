{
    'name': 'Custom Reports Branding',
    'version': '17.0.1.0.0',
    'summary': "Custom PDF template for Sales Quotation and Order with header, footer, and detailed formatting.",
    'description': """
Custom PDF report template for Sale Orders and Quotations in Odoo 17.

Features:
- Custom header with company logo and address
- Professional footer with page numbers and company info
- Order line table with full details (product, qty, price, taxes)
- Clean total section with proper currency formatting
- Optional terms and conditions section
- Professional and clean layout for quotations and orders
""",
    'author': "Ubaid Ur Rehman",
    'website': "",
    'category': 'Sales',
    'license': 'LGPL-3',

    'depends': [
        'sale',
    ],

    'data': [
        'reports/header-footer/custom_header_footer.xml',
    ],

    'assets': {
        'web.report_assets_common': [
            # Add custom CSS if required
            # 'your_module/static/src/css/report_style.css',
        ],
    },

    'images': ['static/description/banner.png'],

    'installable': True,
    'application': False,
    'auto_install': False,
}