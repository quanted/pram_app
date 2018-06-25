import os

from django.http import HttpResponse
from django.shortcuts import redirect
from django.template.loader import render_to_string

from . import links_left


#######################################################################################
################################ User Login Pages #####################################
#######################################################################################

def login(request):
    next_page = request.GET['next']  # Page to redirect to with successful login
    html = render_to_string('01uberheader_main_drupal.html', {
        'SITE_SKIN': os.environ['SITE_SKIN'],
        'TITLE': 'Login'})
    html += render_to_string('02uberintroblock_wmodellinks_drupal.html', {
        'CONTACT_URL': os.environ['CONTACT_URL']})
    html += render_to_string('04ubertext_start_index_drupal.html', {
        'TITLE': 'User Login',
        'TEXT_PARAGRAPH': ""})
    html += render_to_string('login_prompt.html', {'next': next_page})
    html += render_to_string('04ubertext_end_drupal.html', {})
    html += links_left.ordered_list()
    html += render_to_string('06uberfooter.html', {})

    response = HttpResponse(status=302)
    response.write(html)

    return response


def login_auth(request):
    from django.contrib.auth import authenticate, login

    username = request.POST['username']
    password = request.POST['password']
    next_page = request.POST['next']

    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page.

            request.session.set_expiry(3600)  # Set session length time (sec)
            return redirect(next_page)
        else:
            # Return a 'disabled account' error message

            return redirect('/pram/login?next=' + next_page)
    else:
        # Return an 'invalid login' error message.
        return redirect('/pram/login?next=' + next_page)


#######################################################################################
################################ HTTP Error Pages #####################################
#######################################################################################

def file_not_found(request):
    html = render_to_string('01uberheader_main_drupal.html', {
        'SITE_SKIN': os.environ['SITE_SKIN'],
        'TITLE': 'Error'})
    html += render_to_string('02uberintroblock_wmodellinks_drupal.html', {
        'CONTACT_URL': os.environ['CONTACT_URL']})
    html += render_to_string('04ubertext_start_index_drupal.html', {
        'TITLE': 'Error Processing Request',
        'TEXT_PARAGRAPH': ""})
    html += """<br><img src="/static/images/404error.png" width="300" height="300">"""
    html += render_to_string('04ubertext_end_drupal.html', {})
    html += links_left.ordered_list()
    html += render_to_string('06uberfooter.html', {})

    response = HttpResponse(status=404)
    response.write(html)

    return response


#######################################################################################
################################# Docs Redirect #######################################
#######################################################################################

def docs_redirect(request):
    return redirect('/docs/', permanent=True)


def api_redirect(request):
    return redirect('/api/', permanent=True)


#######################################################################################
################################### Links Page ########################################
#######################################################################################

def links(request):

    html = render_to_string('01uberheader_main_drupal.html', {
        'SITE_SKIN': os.environ['SITE_SKIN'],
        'TITLE': u"\u00FCbertool Links"})
    html += render_to_string('02uberintroblock_wmodellinks_drupal.html', {
        'CONTACT_URL': os.environ['CONTACT_URL']})
    html += render_to_string('04ubertext_start_index_drupal.html', {
        'TITLE': u"\u00FCbertool External Links",
        'TEXT_PARAGRAPH': ""})
    html += render_to_string('05ubertext_links_right.html')
    html += render_to_string('04ubertext_end_drupal.html', {})
    html += links_left.ordered_list()
    html += render_to_string('06uberfooter.html', {})

    response = HttpResponse()
    response.write(html)

    return response
