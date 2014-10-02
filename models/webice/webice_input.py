"""
.. module:: webice_input
   :synopsis: A useful module indeed.
"""

from django.template.loader import render_to_string

def webiceInputPage(request, model='', header='', formData=None):
    
    html = render_to_string('04uberwebice_start.html', {
            'model':model, 
            'model_attributes': header+' Inputs'})
    html = html + render_to_string('webice.html', {})
    html = html + render_to_string('04uberwebice_end.html', {})
    # html = html + render_to_string'05ubertext_tooltips_right.html', {})
    # html = html + render_to_string('06uberfooter.html', {'links': ''})
    
    return html