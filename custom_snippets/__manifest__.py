{
    'name': 'Custom Snippets',
    'description': 'Custom Snippets',
    'summary': 'Custom Snippets',
    'author': 'Chinmay Roy',
    'website': 'https://chinmayroy.github.io/',
    'category': 'Website',
    'sequence': 1,
    'version': '16.0.1',
    'depends': ['hr_recruitment'],

    # Security
    'data': [
        'security/ir.model.access.csv',
    ],

    # Views and templates
    'data': [
        'views/snippets/snippets.xml',
        'views/snippets/explore_jobs.xml',
        'views/snippets/fetch_bitcoin.xml',
        'views/snippets/modal.xml',
        'views/snippets/button.xml',
        'views/snippets/navs.xml',
        'views/snippets/offcanvas.xml',
        'views/snippets/pagination.xml',
        'views/snippets/scrollspy.xml',
        'views/snippets/spinners.xml',
        'views/snippets/tutorial.xml',
        'views/snippets/placeholder.xml',
        'demo/demo.xml',
        'views/options.xml',
    ],

    # Assets (CSS, JS, images)
    'assets': {
        'web.assets_frontend': [
            'custom_snippets/static/src/scss/styles.scss',
            # 'custom_snippets/static/src/js/explore_jobs.js',
            'custom_snippets/static/src/js/fetch_bitcoin_graph.js',
            'custom_snippets/static/src/css/owl.carousel.min.css',
            'custom_snippets/static/src/css/owl.theme.default.min.css',
            'custom_snippets/static/src/js/owl.carousel.min.js',
        ],
        'web._assets_primary_variables': [
            'custom_snippets/static/src/scss/primary_variables.scss',
        ],
    },

    # Images and other media
    'images': [
        'static/description/images/banner.gif',
        'static/description/icon.png',
    ],
    'icon': 'custom_snippets/static/description/icon.png',
    # Other settings
    'auto_install': False,
    'application': False,
    'price': 0,
    'currency': 'USD',
    'license': 'LGPL-3',
    'contributors': [
        'Chinmay Roy <https://chinmayroy.github.io/>',
    ],
}
