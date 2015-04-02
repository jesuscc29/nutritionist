# -*- coding: utf-8 -*-
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

__author__ = 'jesuscc29'


@login_required(login_url='login')
def home(request):
    context = dict()
    request_context = RequestContext(request, context)
    return render_to_response('index.html', request_context)


def user_login(request):
    error = ''
    if request.user.is_authenticated():
        return HttpResponseRedirect("/main/")
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                if 'rememberme' not in request.POST:
                    request.session.set_expiry(900)

                login(request, user)
                request.session['username'] = request.user.get_full_name()
                url = "/home/"
                try:
                    ur_get = request.META['HTTP_REFERER']
                except KeyError:
                    pass
                else:
                    ur_get = ur_get.split("next=")
                    if len(ur_get) > 1:
                        url = ur_get[1]
                return HttpResponseRedirect(url)
            else:
                error = "Tu cuenta ha sido desactivada, por favor " \
                        "ponte en contacto con tu administrador"
        else:
            error = "Tu nombre de usuario o contrase&ntilde;a son " \
                    "incorrectos."
    variables = dict(error=error)
    variables_template = RequestContext(request, variables)
    return render_to_response("login.html", variables_template)


def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/login/')