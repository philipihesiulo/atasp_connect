# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"module_name": "ATASP Connect",
			"color": "grey",
			"icon": "octicon octicon-file-directory",
			"type": "module",
			"label": _("ATASP Connect")
		},

		{
			"module_name": "Monitoring & Evaluation",
			"color": "grey",
			"icon": "octicon octicon-file-directory",
			"type": "module",
			"label": _("Monitoring & Evaluation")
		}
	]
