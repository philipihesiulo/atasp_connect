# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "atasp_connect"
app_title = "ATASP Connect"
app_publisher = "Philip Ihesiulo"
app_description = "Monitoring, evaluation and reporting tool for ATASP."
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "philipihesiulo@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

app_logo_url = '/assets/atasp_connect/images/logo.png'
app_logo_width = 100

website_context = {
	"favicon": 	"/assets/atasp_connect/images/favicon.png",
	"splash_image": "/assets/atasp_connect/images/logo.png"
}

# include js, css files in header of desk.html
# app_include_css = "/assets/atasp_connect/css/atasp_connect.css"
# app_include_js = "/assets/atasp_connect/js/atasp_connect.js"

# include js, css files in header of web template
# web_include_css = "/assets/atasp_connect/css/atasp_connect.css"
# web_include_js = "/assets/atasp_connect/js/atasp_connect.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "atasp_connect/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)

home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "atasp_connect.install.before_install"
# after_install = "atasp_connect.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "atasp_connect.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

permission_query_conditions = {
	"Quarterly Performance": "atasp_connect.permissions.quarterly_performance_query",
	"Zone": "atasp_connect.permissions.zone_query",
	"Role": "atasp_connect.permissions.role_query",
}
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"atasp_connect.tasks.all"
# 	],
# 	"daily": [
# 		"atasp_connect.tasks.daily"
# 	],
# 	"hourly": [
# 		"atasp_connect.tasks.hourly"
# 	],
# 	"weekly": [
# 		"atasp_connect.tasks.weekly"
# 	]
# 	"monthly": [
# 		"atasp_connect.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "atasp_connect.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "atasp_connect.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "atasp_connect.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

auth_hooks = [
	"atasp_connect.auth.validate"
]

fixtures = [
    "Navbar Settings",
	"Website Settings",
	"Workspace",
    "Quarter",
	"Custom DocPerm",
	"Year",
	{"dt": "Role", "filters": [["is_custom", "=", 1]]},
	"Role Profile"
]