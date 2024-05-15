from django import forms
from django.shortcuts import render, redirect
from django.http import HttpResponse
from CRA import settings
from .models import signup, submissions
import google.generativeai as genai
# Create your views here.

genai.configure(api_key="Your API Key")


def intial(request):
    return render(request, 'html/start.html')


def loginform(request):
    if request.method == "POST":
        e = request.POST['email']
        pa = request.POST['password']
        p = "Incorrect password"
        q = "Email does not exist"
        try:
            x = signup.objects.get(email=e)
        except:
            return render(request, 'html/loginform.html', {'error': q})
        if (x.password == pa):
            request.session['D_id'] = x.D_id
            return redirect('hp')
        else:
            return render(request, 'html/loginform.html', {'error': p})
    return render(request, 'html/loginform.html')


def register(request):
    if request.method == "POST":
        e = request.POST['email']
        pa = request.POST['password']
        try:
            y = signup.objects.create(email=e, password=pa)
            return redirect('lf')

        except:
            t = "Email Already Exists."
            return redirect('lf')

    return render(request, 'html/signup.html')


def homepage(request):
    return render(request, 'html/homepage.html')


def submit(request):
    if request.method == "POST":
        codes = request.POST['code']
        a = "Review Generated Successfully"
        b = "Error!... while Submitting Code"
        id = request.session.get('D_id')
        model = genai.GenerativeModel("gemini-pro")
        chat = model.start_chat()
        response = chat.send_message(
            "Give me code review for the below code in professional code review format\n"+codes)
        try:
            submissions.objects.create(
                D_id=id, code=codes, gemini_output=response.text)

            return render(request, 'html/submitcode.html', {'error': a})
        except:
            return render(request, 'html/submitcode.html', {'error': b})
    return render(request, 'html/submitcode.html')


def history(request):
    id = request.session.get('D_id')
    reviews = submissions.objects.filter(D_id=id)
    return render(request, "html/history.html", {'reviews': reviews})
