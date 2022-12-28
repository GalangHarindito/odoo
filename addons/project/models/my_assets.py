from odoo import api, fields, models
from datetime import datetime

class MyAssets(models.Model):
    _name = "my.assets"
    _description = "My Assets"

    assetsNo = fields.Char(string="Assets No", compute='_compute_assets')
    description = fields.Text(string="Description")
    location = fields.Text(string="Location")
    date = fields.Date(string="Date")
    price = fields.Integer(string="Price", default=0)
    owner = fields.Many2one("res.partner", string="Owner")

    def _compute_assets(self):
        now = datetime.now()
        self.assetsNo = now.strftime("%Y%m%d%H%M%S")

    @api.onchange("owner")
    def _onchange_compute_date(self):
        self.date = datetime.now()
