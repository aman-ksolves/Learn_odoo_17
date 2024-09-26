{
    'name': 'Custom Users',
    'summary': 'Learning User Session login',
    'author': 'Aman and Anjali',
    'license': 'LGPL-3',
    'depends': ['web', 'base','product','website','sale'],
    'data': [
        'views/res_user_form_view.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'custom_user/static/src/**/*',

        ],
    },
}
