from odoo import api, fields, models

class Quiz(models.Model):
    _name = 'quiz.quiz'
    _description = 'Quizzes'

    name = fields.Char('Name')
    question_list = fields.One2many('quiz.question', 'quiz_id')


class QuizQuestion(models.Model):
    _name = 'quiz.question'
    _description = 'Questions'

    question = fields.Char('Question')
    quiz_id = fields.Many2one('quiz.quiz')
    answer_list = fields.One2many('quiz.answer', 'question_id')
    partner_id = fields.Many2one('res.partner', 'Partner')
    partner_id2 = fields.Many2one('res.partner', 'Partner(Cust.)')

class ResPartner(models.Model):
    _inherit = 'res.partner'

        # def _name_search(self, name, domain=None, operator='ilike', limit=None, order=None):
        #     res = super(ResPartner, self)._name_search(name,domain, operator, limit, order)
        #     return res

    @api.model
    def _name_search(self, name, domain=None, operator='ilike', limit=None, order=None):
        res = super()._name_search(name, domain, operator, limit, order)
        return res

    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=100):
        res = super().name_search(name, args, operator, limit)
        if not self.env.context.get('custom_name'):
            return res
        ids = [rec[0] for rec in res]
        partners = self.browse(ids)
        new_res = list()
        for rec in partners:
            new_res.append((rec.id,rec.email))
        return new_res
class QuizAnswer(models.Model):
    _name = 'quiz.answer'
    _description = 'Answers'

    description = fields.Char('Description')
    product_id = fields.Many2one('product.template', 'Product')

    question_id = fields.Many2one('quiz.question')

