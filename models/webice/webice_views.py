"""
Created on Tue Jan 03 13:30:41 2012
@author: Jon F.
"""

from django.template.loader import render_to_string


def ICETabletPage(requests):

    html = render_to_string('webice_ICETable.html', {})
    
    return html

def webiceSSDOutputPage(requests):

	html = render_to_string('01pop_uberheader.html', {'title':'Ubertool'})
    html = html + render_to_string('webiceSSD-jqueryOutput.html', {})
    html = html + render_to_string('02pop_uberintroblock_wmodellinks.html',  {'model':'webice','page':'output'})
    html = html + render_to_string('03pop_ubertext_links_left.html', {})                               
    html = html + render_to_string('04uberoutput_start.html', {
            'model':'webice', 
            'model_attributes':'Web-ICE v3.2.1 Output'})
    html = html + render_to_string('webiceSSDOutput.html', {})
    html = html + render_to_string('04uberwebice_end.html', {})
    html = html + render_to_string('06pop_uberfooter.html', {'links': ''})

    return html

def webiceTNEOutputPage(requests):

	html = render_to_string('01pop_uberheader.html', {'title':'Ubertool'})
    html = html + render_to_string('webiceTNE-jqueryOutput.html', {})
    html = html + render_to_string('02pop_uberintroblock_wmodellinks.html',  {'model':'webice','page':'output'})
    html = html + render_to_string('03pop_ubertext_links_left.html', {})                               
    html = html + render_to_string('04uberoutput_start.html', {
            'model':'webice', 
            'model_attributes':'Web-ICE v3.2.1 Output'})
    html = html + render_to_string('webiceTNEOutput.html', {})
    html = html + render_to_string('04uberwebice_end.html', {})
    html = html + render_to_string('06pop_uberfooter.html', {'links': ''})

    return html