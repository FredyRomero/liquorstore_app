from odoo import api, fields, models


class AlcoholTipo(models.Model):
    _name = 'liquorstore.alcohol.tipo'
    _description = 'Alcohol Category'
    name = fields.Char('Name', required=True)

    alcohol_id = fields.Many2one(
        'liquorstore.alcohol.tipo',
        'tipos_id',
        ondelete='restrict')
    parent_path = fields.Char(index=True)
