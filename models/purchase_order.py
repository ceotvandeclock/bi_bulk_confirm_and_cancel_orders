# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details
from odoo import api, fields, models, _
from odoo.exceptions import UserError


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    def action_confirm_po(self):
        for rec in self:
            if rec:
                rec.button_confirm()
        for rec in self:
            if rec.state == 'cancel' or rec.state == 'done':
                raise UserError("It is not allowed to confirm an order in the following states : done, cancel")

    def action_cancel_po(self):
        active_ids = self._context.get('active_ids')
        purchase_order_ids = self.env['purchase.order'].browse(active_ids)
        for purchase_order_id in purchase_order_ids:
            if purchase_order_id:
                purchase_order_id.button_cancel()
