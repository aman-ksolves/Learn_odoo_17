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


class QuizAnswer(models.Model):
    _name = 'quiz.answer'
    _description = 'Answers'

    description = fields.Char('Description')
    product_id = fields.Many2one('product.template', 'Product')

    question_id = fields.Many2one('quiz.question')