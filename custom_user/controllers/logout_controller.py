# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class EasyLanguageSelector(http.Controller):

    @http.route('/get_user_time/timer', auth='public', type='json')
    def get_user_time(self):
        if request.env.user.enable_time_logout:
            return request.env.user.max_login_time
