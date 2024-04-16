from odoo import api, fields, models

class ResUsers(models.Model):
    _name = 'res.users'
    _inherit = 'res.users'

    enable_time_logout = fields.Boolean('Enable Log Out time')
    max_login_time = fields.Integer('Log in time', default='2')

    def get_logout_time(self):
        if self.enable_time_logout:
            return self.max_login_time
        return -1