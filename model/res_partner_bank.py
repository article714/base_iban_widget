from odoo import models
from odoo.exceptions import ValidationError
from odoo.addons.base_iban.models.res_partner_bank import validate_iban


class ResPartnerBank(models.Model):
    _inherit = "res.partner.bank"

    def check_iban(self, iban=""):
        try:
            validate_iban(iban)
            return True
        except ValidationError:
            return False
