"""
.. module:: sip_input
   :synopsis: A useful module indeed.
"""

from django.template.loader import render_to_string


def sipInputPage(request, model='', header='', formData=None):
    import sip_parameters

    html = render_to_string('04uberinput_jquery.html', {'model': model})
    html += render_to_string('04uberinput_start.html', {
        'model': model,
        'model_attributes': header + ' Inputs'})
    html += str(sip_parameters.SipInp(formData))
    html += render_to_string('04uberinput_end.html', {'sub_title': 'Submit'})
    html += render_to_string('sip_ubertool_config.html', {})
    # Check if tooltips dictionary exists
    try:
        import sip_tooltips
        hasattr(sip_tooltips, 'tooltips')
        tooltips = sip_tooltips.tooltips
    except:
        tooltips = {}
    html += render_to_string('05ubertext_tooltips_right.html', {'tooltips': tooltips})

    return html
