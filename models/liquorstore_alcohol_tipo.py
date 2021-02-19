from odoo import api, fields, models

class AlcoholTipo(models.Model):
    _name = 'liquorstore.alcohol.tipo'
    _description = 'Alcohol Category'
    _parent_store = True
    name = fields.Char('Name', required=True)

    parent_id = fields.Many2one(
        'liquorstore.alcohol.tipo',
        'Parent Category',
        ondelete='restrict')
    parent_path = fields.Char(index=True)