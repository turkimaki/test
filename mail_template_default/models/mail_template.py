# © 2019 - today Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models,api


class MailTemplate(models.Model):
    _inherit = 'mail.template'

    is_default_template  = fields.Boolean(string='Default Template')