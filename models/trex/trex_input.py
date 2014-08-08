# -*- coding: utf-8 -*-
"""
Created on Tue Jan 03 13:30:41 2012
@author: T. Hong
"""
from django.template.loader import render_to_string


def trexInputPage(request, model='', header='', formData=None):
    import trex_parameters

    # html = render_to_string('04uberinput_jquery.html', { 'model': model })    
    html = render_to_string('04uberinput_start.html', {
            'model':model, 
            'model_attributes': header+' Inputs'})
    html = html + str(trex_parameters.TrexInp(formData))
    html = html + render_to_string('04uberinput_end.html', {'sub_title': 'Submit'})
    # Check if tooltips dictionary exists
    try:
       import trex_tooltips
       hasattr(trex_tooltips, 'tooltips')
       tooltips = trex_tooltips.tooltips
    except:
       tooltips = {}
    html = html + render_to_string('05ubertext_tooltips_right.html', {'tooltips':tooltips})

    return html