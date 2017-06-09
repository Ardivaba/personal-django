from django.shortcuts import render
from django.http import HttpResponse, HttpResponsePermanentRedirect
from .models import Blink, Task
from .models import BlinkNotes
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import requests

def index(request):
	context = {
	}
	return render(request, "index.html", context)

def time(request):
	context = {
	}
	return render(request, "time.html", context)

# Register
def register(request):
	context = {
	}
	return render(request, "register.html", context)

def create_user(request):
	user = User()

	username = request.POST["username"]
	email = request.POST["email"]
	password = request.POST["password"]
	password_confirm = request.POST["password_confirm"]

	user = User.objects.create_user(username, email, password)

	context = {
		"users": User.objects.all()
	}

	user.save()
	return render(request, "create_user.html", context)

# Sign in
def sign_in(request):
	if "username" in request.POST and "password" in request.POST:
		username = request.POST["username"]
		password = request.POST["password"]

		print("1")
		user = authenticate(username=username, password=password)
		print("2")
		login(request, user)
		print("User logged in")
		if user is not None:
			return HttpResponsePermanentRedirect("/personal")

	context = {
	}
	return render(request, "sign_in.html", context)

# Sign out
def sign_out(request):
	logout(request)
	context = {
	}
	return render(request, "sign_out.html", context)

# Tasks
def create_task(request):
	if "title" in request.POST and "tasks" in request.POST:
		task = Task()
		task.owner = request.user
		task.title = request.POST["title"]
		task.sub_tasks = request.POST["tasks"]
		task.task_type = int(request.POST["task-type"])

		print("Creating task")

		task.save()
		return HttpResponsePermanentRedirect("/personal/tasks")
	else:
		print("No post...")

	return render(request, "tasks/create_task.html", {})

def tasks(request):
	do_task = request.GET.get("do_task", -1)
	print("Doing task...")
	print(do_task)
	if do_task != -1:
			Task.objects.filter(id=do_task).delete()

	context = {
		"tasks": Task.objects.filter(owner=request.user)
	}
	return render(request, "tasks/tasks.html", context)

def social(request):
	context = {
	}
	return render(request, "social.html", context)

# Habits
def habits(request):
	context = {
	}
	return render(request, "habits/habits.html", context)

def mission(request):
	context = {
	}
	return render(request, "mission.html", context)

def goals(request):
	context = {
	}
	return render(request, "goals.html", context)

def money(request):
	context = {
		"btc": requests.get("http://api.coindesk.com/v1/bpi/currentprice.json").json()["bpi"]["USD"]["rate"],
	}
	return render(request, "money.html", context)

def notes(request):
	context = {
	}
	return render(request, "notes/notes.html", context)

# Notes
def add_note(request):
	context = {
	}
	return render(request, "notes/add_note.html", context)

def note(request):
	context = {
	}
	return render(request, "notes/note.html", context)

# blinks
def blinks(request):
	delete_blink = request.GET.get("delete_blink", -1)

	if delete_blink != -1:
		Blink.objects.filter(id=delete_blink).delete()

	print(request.user)

	context = {
		"blinks": Blink.objects.filter(owner=request.user)
	}
	return render(request, "blinks/blinks.html", context)

def add_blink(request):
	context = {
	}
	return render(request, "blinks/add_blink.html", context)

def blink(request):
	id=request.GET.get("id", 1)

	comment = request.POST.get("comment", "Empty")
	delete_note = request.GET.get("delete_note", -1)

	if delete_note != -1:
		BlinkNotes.objects.filter(id=delete_note).delete()

	lines = comment.splitlines()
	if comment != "Empty" and len(lines) < 2:
		lines = [comment]
	for line in lines:
		note = BlinkNotes()

		note.owner = Blink.objects.get(id=id)
		note.note = line

		if note.note != "Empty" and len(note.note) > 0:
			note.save()

	context = {
		"blink": Blink.objects.get(id=id),
		"notes": BlinkNotes.objects.filter(owner=id)
	}
	return render(request, "blinks/blink.html", context)

def create_blink(request):
	new_blink = Blink()

	new_blink.owner = request.user
	new_blink.title = request.POST["title"]
	new_blink.author = request.POST["author"]
	new_blink.description = request.POST["description"]
	new_blink.image = request.POST["image"]
	new_blink.url = request.POST["url"]
	new_blink.rating = int(request.POST["rating"])
	new_blink.tags = request.POST["tags"]

	context = {
		"blinks": Blink.objects.all()
	}

	new_blink.save()
	return HttpResponsePermanentRedirect("/personal/blinks")