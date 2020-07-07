# © 2019 - today Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models, api


class MeansCommunication(models.Model):
    _name = 'means.communication'
    _order = 'sequence,id'

    name = fields.Char(string='Name')

    sequence = fields.Integer(string='Sequence')


class TaskFeedback(models.Model):
    _name = 'task.feedback'

    name = fields.Char(string='Name')
    start_date = fields.Datetime(string='Start Date')
    end_date = fields.Datetime(string='En Date')
    mean_communication_id = fields.Many2one('means.communication', string='Means communication')

    partner_ids = fields.Many2many('res.partner', string='Participants')

    preview_point = fields.Html('Preview Point')

    task_id = fields.Many2one('project.task', string='Task')

    ressources = fields.Html('Ressources')
    risques = fields.Html('Risques')

    action_ids = fields.One2many('reminder.actions', 'feedback_id', string='Actions')
    exam_ids = fields.One2many('task.examan', 'feedback_id', string='Examan')


class PendingActionsReminder(models.Model):
    _name = 'reminder.actions'

    feedback_id = fields.Many2one('task.feedback', string='Feedback Task')
    task_id = fields.Many2one('project.task')
    summary = fields.Char(string='Summary')
    notes = fields.Char(string='Notes')
    assigned = fields.Many2one('res.users', 'Assigned')
    date_deadline = fields.Date(string='Date DeadLine')
    state = fields.Selection([
        ('overdue', 'Overdue'),
        ('today', 'Today'),
        ('planned', 'Planned')], 'State', )


class TaskExaman(models.Model):
    _name = 'task.examan'
    sequence = fields.Integer(string='Sequence')

    feedback_id = fields.Many2one('task.feedback', string='Feedback Task')
    task_id = fields.Many2one('project.task')
    summary = fields.Char(string='Summary')
    notes = fields.Char(string='Notes')
    assigned = fields.Many2one('res.users', 'Assigned')
    date_deadline = fields.Date(string='Date DeadLine')

    def create(self, vals):
        res = super(TaskExaman, self).create(vals)
        activity = self.env['mail.activity'].create({
            'res_id': res.task_id.id,
            'res_model': 'project.task',
            'summary': res.summary,
            'notes': res.notes,
            'user_id': res.assigned.id,
            'activity_type_id': self.env.ref('project_task_meeting_minutes.activity_examan').id,
            'res_model_id': self.env['ir.model'].search([('model', '=', 'project.task')]).id,
        })
        return res
