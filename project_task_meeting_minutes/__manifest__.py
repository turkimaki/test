# © 2019 - today Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    'name': 'Project Task Meeting Minutes',
    'version': '1.0.0',
    'author': 'Numigi',
    'maintainer': 'Numigi',
    'website': 'https://www.numigi.com',
    'license': 'LGPL-3',
    'category': 'Recording',
    'summary': 'Project Task Meeting Minutes.',
    'depends': [
        'base','project'
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/mail_activity_type.xml',
        'views/means_communication_view.xml',
        'views/project_task_view.xml',
        'views/task_feedback_view.xml',
        'views/reminder_actions_view.xml',
        'views/task_examan_view.xml',
    ],
    'installable': True,
}
