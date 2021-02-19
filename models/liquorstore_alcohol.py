from odoo import fields, models, api
from odoo.exceptions import Warning


class Alcohol(models.Model):
    _name = 'liquorstore.alcohol'
    _description = 'Alcohol'
    name = fields.Char('Nombre', required=True)
    marca = fields.Char('Marca')
    descripcion = fields.Char('Descripcion')
    image = fields.Image('Image')
    active = fields.Boolean('Active?', default=True)
    precio = fields.Integer('Precio',required=True)

    # Hierarchy fields
    tipos_id = fields.Many2one(
        'liquorstore.alcohol.tipo',
        'Tipo',
        ondelete='restrict')
    parent_path = fields.Char(index=True)

    @api.constrains('precio')
    def button_check_price(self):
        for Alcohol in self:
            if Alcohol.precio <= 0:
                raise Warning('El precio no puede ser cero o menor %s' % Alcohol.name)

