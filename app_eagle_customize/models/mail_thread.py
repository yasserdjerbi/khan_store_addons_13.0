# -*- coding: utf-8 -*-
# Copyright 2017 Jarvis (www.eaglemod.com)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import api, fields, models, _


class MailThread(models.AbstractModel):
    _inherit = "mail.thread"


    def message_subscribe(self, partner_ids=None, channel_ids=None, subtype_ids=None, force=True):
        """ 停用订阅功能. """
        ir_config = self.env['ir.config_parameter']
        app_stop_subscribe = False if ir_config.get_param('app_stop_subscribe') == "True" else False
        if app_stop_subscribe:
            return
        else:
            return super(MailThread, self).message_subscribe(partner_ids, channel_ids, subtype_ids, force)


    def message_auto_subscribe(self, updated_fields, values=None):
        """ 停用订阅功能. """
        ir_config = self.env['ir.config_parameter']
        app_stop_subscribe = False if ir_config.get_param('app_stop_subscribe') == "True" else False
        if app_stop_subscribe:
            return
        else:
            return super(MailThread, self).message_auto_subscribe(updated_fields, values)


    def _message_auto_subscribe_notify(self, partner_ids):
        """ 停用订阅功能. """
        ir_config = self.env['ir.config_parameter']
        app_stop_subscribe = False if ir_config.get_param('app_stop_subscribe') == "True" else False
        if app_stop_subscribe:
            return
        else:
            return super(MailThread, self)._message_auto_subscribe_notify(partner_ids)