{
    'name': 'Quiz',
    'summary': 'Quiz app',
    'author': 'Aman',
    'license': 'LGPL-3',
    'version': '17.0',
    'application': True,
    'installable': True,
    'depends': ['product'],
    'data': [
        'security/ir.model.access.csv',
        'views/quiz_view.xml',

    ],

    # 'assets': {
    #     'web.assets_backend': [
    #         'custom_user/static/src/**/*',
    #
    #     ],
    # },
}
