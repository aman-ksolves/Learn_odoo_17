from odoo import api, fields, models

class ResUsers(models.Model):
    _name = 'res.users'
    _inherit = 'res.users'

    max_login_time = fields.Integer('Log in time')