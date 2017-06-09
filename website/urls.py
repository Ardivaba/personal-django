from django.conf.urls import url
from . import views

urlpatterns = [
	url(r"^$", views.index, name = "index"),
	url(r"^time", views.time, name = "time"),

# Tasks
	url(r"^tasks/create_task", views.create_task, name = "create_task"),
	url(r"^tasks", views.tasks, name = "tasks"),

	url(r"^social", views.social, name = "social"),
	url(r"^habits", views.habits, name = "habits"),
	url(r"^mission", views.mission, name = "mission"),
	url(r"^goals", views.goals, name = "goals"),
	url(r"^money", views.money, name = "money"),

# Notes
	url(r"^notes/add_note", views.add_note, name = "add_note"),
	url(r"^notes/note", views.note, name = "note"),
	url(r"^notes", views.notes, name = "notes"),

# Blinks
	url(r"^blinks/create", views.create_blink, name = "create_blink"),
	url(r"^blinks/add_blink", views.add_blink, name = "add_blink"),
	url(r"^blinks/blink", views.blink, name = "blink"),
	url(r"^blinks", views.blinks, name = "blinks"),

# User system
	url(r"^sign_in", views.sign_in, name = "sign_in"),
	url(r"^sign_out", views.sign_out, name = "sign_out"),
	url(r"^register", views.register, name = "register"),
	url(r"^create_user", views.create_user, name = "create_user"),

	url(r"r'^.*/$'", views.index, name = "index")
]