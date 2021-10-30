
from odoo import api, fields, models


class IrSequence(models.Model):
    _inherit = 'ir.sequence'

    def _get_prefix_suffix(self, date=None, date_range=None):
        
        if self.env.company.prefix :
            if not self.prefix :
                    self.prefix = self.env.company.prefix
            else :
                companies_prefix = self.env['res.company'].search([]).mapped('prefix')
                if any(prefix in self.prefix for prefix in companies_prefix) :
                    for prefix in companies_prefix :
                        if prefix in self.prefix :
                            self.prefix = self.prefix.replace(prefix , self.env.company.prefix)
                            break                    
                else :
                    self.prefix = self.env.company.prefix + "/" + self.prefix


        return super(IrSequence,self)._get_prefix_suffix(date=None , date_range=None)