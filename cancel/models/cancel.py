 
from odoo import api, fields, models, _

 
class cancelrights(models.Model):
    _inherit = 'account.invoice'


class canceljournals(models.Model):
    _inherit = 'account.move'
    
class customerinvoice(models.Model):
    _inherit ='account.invoice'