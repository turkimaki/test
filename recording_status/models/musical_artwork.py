# © 2020 - today Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models, api


class MusicalArtwork(models.Model):
    _inherit = 'musical.artwork'
    status = fields.Selection([
        ('to_validate', 'To Validate'), ('validated', 'Validated')], string='Status', default='to_validate',
        track_visibility='onchange')

    def validate_musical_artwork(self):
        old_status = self.status
        self.status = 'validated'
        if self.env.lang == 'fr_FR':
            self.message_post(body="Utilisateur ayant validé : " + self.env.user.name)
            self.message_post(
                body="date et l’heure de validation :" + ' ' + str(self.write_date.strftime("%Y-%m-%d  %H:%M:%S")))
            self.message_post(body="statut avant :" + ' ' + old_status)
            self.message_post(body="statut après :" + ' ' + self.status)

        else:
            self.message_post(body="User who validated: " + self.env.user.name)
            self.message_post(body="validation date :" + ' ' + str(self.write_date.strftime("%Y-%m-%d  %H:%M:%S")))
            self.message_post(body="current status :" + ' ' + old_status)
            self.message_post(body="new status :" + ' ' + self.status)

    def write(self, vals):
        if not self.env.user.has_group('recording.group_manager'):
            vals['status'] = 'to_validate'
        res = super(MusicalArtwork, self).write(vals)
        return res
