from odoo import models, fields, api
from datetime import datetime
from datetime import timedelta, datetime
import logging

_logger = logging.getLogger(__name__)

class AccountMove(models.Model):
    _inherit = 'account.move'

    #accion para realizar el envio de facturas
    def action_post(self):
        res = super().action_post()

        for move in self:
            if move.move_type == 'out_invoice' and move.partner_id.email:
                template = self.env.ref('account.email_template_edi_invoice', raise_if_not_found=False)
                if template:
                    template.send_mail(move.id, force_send=True)

        return res

