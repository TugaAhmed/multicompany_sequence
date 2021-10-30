
from odoo import api, fields, models


class SequenceMixin(models.AbstractModel):
    _inherit = 'sequence.mixin'
    
    def _get_sequence_format_param(self, previous):
            format , format_values = super(SequenceMixin,self)._get_sequence_format_param(previous)

            if self.env.company.prefix :
                if not format_values['prefix1'] :
                    format_values['prefix1'] = self.env.company.prefix
                else :
                    companies_prefixs = self.env['res.company'].search([('prefix','!=',False)]).mapped('prefix')
                    if any(prefix in format_values['prefix1'] for prefix in companies_prefixs) :
                        for prefix in companies_prefixs :
                            if prefix in format_values['prefix1'] :
                                format_values['prefix1'] = format_values['prefix1'].replace(prefix , self.env.company.prefix)
                                break                    
                    else :
                        format_values['prefix1'] = self.env.company.prefix + "/" + format_values['prefix1']

            return format, format_values