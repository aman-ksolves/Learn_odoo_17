from odoo import api, fields, models, _

class ResUsers(models.Model):
    _name = 'res.users'
    _inherit = 'res.users'

    enable_time_logout = fields.Boolean('Enable Log Out time')
    max_login_time = fields.Integer('Log in time', default='2')

    def get_logout_time(self):
        if self.enable_time_logout:
            return self.max_login_time
        return -1

class ProductInheritTemplate(models.Model):
    _inherit = 'product.template'

    @api.model_create_multi
    def create(self, vals_list):
        for val in vals_list:
            val['default_code'] = self.env['ir.sequence'].next_by_code('custom_user.code') or _('New')
        return super().create(vals_list)

class ProductInherit(models.Model):
    _inherit = 'product.product'

    @api.model_create_multi
    def create(self, vals_list):
        # for vals in vals_list:
        #     if 'company_id' in vals:
        #         self = self.with_company(vals['company_id'])
        #     if vals.get('name', _("New")) == _("New"):
        #         seq_date = fields.Datetime.context_timestamp(
        #             self, fields.Datetime.to_datetime(vals['date_order'])
        #         ) if 'date_order' in vals else None
        #         vals['name'] = self.env['ir.sequence'].next_by_code(
        #             'sale.order', sequence_date=seq_date) or _("New")
        # vals_list['default_code'] = self.env['ir.sequence'].next_by_code('default.code') or _('New')
        return super().create(vals_list)