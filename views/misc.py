from django.template.loader import render_to_string
from django.http import HttpResponse
from django.shortcuts import redirect
import linksLeft
import os

#######################################################################################
################################ User Login Pages #####################################
#######################################################################################

def login(request):

    next = request.GET['next']  #  Page to redirect to with successful login
    html = render_to_string('01uberheader.html', {
            'site_skin' : os.environ['SITE_SKIN'],
            'title': 'Login Page'})
    html = html + render_to_string('02uberintroblock_nomodellinks.html', {'site_skin' : os.environ['SITE_SKIN']})
    html = html + linksLeft.linksLeft()
    html = html + render_to_string('04ubertext_start.html', {
            'model_attributes': 'User Login',
            'text_paragraph': ""})
    html = html + render_to_string('login_prompt.html', {'next': next})
    html = html + render_to_string('04ubertext_end.html', {})
    html = html + render_to_string('05ubertext_links_right.html', {})
    html = html + render_to_string('06uberfooter.html', {'links': ''})

    response = HttpResponse()
    response.write(html)

    return response


def login_auth(request):
    from django.contrib.auth import authenticate, login
    import base64

    username = request.POST['username']
#     password = base64.b64decode(request.POST['password'])
    password = request.POST['password']
    next = request.POST['next']
    print username, password, next
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page.
            print "Login Successful"
            request.session.set_expiry(3600)  #  Set session length time (sec)
            return redirect(next)
        else:
            # Return a 'disabled account' error message
            print "User account is inactive"
            return redirect('/ubertool/login?next=' + next)
    else:
        # Return an 'invalid login' error message.
        return redirect('/ubertool/login?next=' + next)

#######################################################################################
################################ HTTP Error Pages #####################################
#######################################################################################

def fileNotFound(request):
    html = render_to_string('01uberheader.html', {
            'site_skin' : os.environ['SITE_SKIN'],
            'title': 'Error'})
    html = html + render_to_string('02uberintroblock_nomodellinks.html', {'site_skin' : os.environ['SITE_SKIN']})
    html = html + linksLeft.linksLeft()
    html = html + render_to_string('04ubertext_start.html', {
            'model_attributes': 'File Not Found',
            'text_paragraph': ""})
    html = html + """<br><img src="/static/images/404error.png" width="300" height="300">"""
    html = html + render_to_string('04ubertext_end.html', {})
    html = html + render_to_string('05ubertext_links_right.html', {})
    html = html + render_to_string('06uberfooter.html', {'links': ''})

    response = HttpResponse()
    response.write(html)

    return response


#######################################################################################
################################# Docs Redirect #######################################
#######################################################################################

def docsRedirect(request):
    return redirect('/docs/', permanent=True)