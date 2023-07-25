# Copyright 2023 Camilo Prado - Xtendoo (https://xtendoo.es)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import _, models, fields


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    nafss = fields.Char(
        string="Número de afiliación a la seguridad social",
    )
    contrato = fields.Char(
        string="Número de contrato",
    )
    antiguedad = fields.Date(
        string="Fecha de alta",
    )
    discapacidad = fields.Boolean(
        string="Tiene discapacidad",
    )
    categoria = fields.Char(
        string="Categoría",
    )
    ct = fields.Char(
        string="Centro de trabajo",
    )
    js = fields.Float(
        string="Jornada semanal",
    )



