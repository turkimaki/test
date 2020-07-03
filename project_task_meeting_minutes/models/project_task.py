# © 2019 - today Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models, api




class ProjectTask(models.Model):
    _inherit = 'project.task'

    def create_task_feedback(self):
        task_feedback = self.env['task.feedback'].create({
            'name': 'Compte-rendu: ' + '[' + self.name + ']',
            'preview_point': self.description,
            'task_id': self.id,
            'action_ids':
                [(0, 0, {
                    'task_id': self.id,
                    'date_deadline': rec.date_deadline,
                    'assigned': rec.user_id.id,
                    'summary': rec.summary,
                    'state': rec.state,
                }) for rec in self.activity_ids]
        })

        print('activity_ids', self.activity_ids)
        for activity in self.activity_ids:
            print('res_id', activity.res_id)
            print('res_model', activity.res_model)
            print('res_model_id*****', activity.res_model_id)

        return {'name': 'Compte rendu',
                'view_type': 'form',
                'view_mode': 'form',
                'view_id': self.env.ref('project_task_meeting_minutes.task_feedback_view_form').id,
                'res_model': 'task.feedback',
                'res_id': task_feedback.id,
                'type': 'ir.actions.act_window',
                'target': 'current',
                }
