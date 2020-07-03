# © 2019 - today Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    'name': 'Recording Status',
    'version': '1.0.0',
    'author': 'Numigi',
    'maintainer': 'Numigi',
    'website': 'https://www.numigi.com',
    'license': 'LGPL-3',
    'category': 'Recording',
    'summary': 'Status for the recording application.',
    'depends': [
        'base','recording','musical_artwork','mail'
    ],
    'data': [
        'views/recording_form_view.xml',
        'views/musical_artwork_form_view.xml',
    ],
    'installable': True,
}
