from django.views.generic import View
from django.shortcuts import render, get_object_or_404, render_to_response
from django.template.loader import render_to_string
from django.http import HttpResponse
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

class genericDescriptionPage(View):
    def get(self, request):
        # logger.log(BASE_DIR)
        text_file1 = open('./generic/generic_description.txt','r')
        x = text_file1.read()
        
        context = {'title':'Ubertool'}

        html = render_to_string('01uberheader.html', context)
        html = html + render_to_string('02uberintroblock_wmodellinks.html', {'model':'generic_hh','page':'description'})
        html = html + render_to_string('03ubertext_links_left.html', {})
        html = html + render_to_string('04ubertext_start.html', {
                'model_page':'#', 
                'model_attributes':'Generic Overview', 
                'text_paragraph':x})
        html = html + render_to_string('04ubertext_end.html', {})
        html = html + render_to_string('05ubertext_links_right.html', {})
        html = html + render_to_string('06uberfooter.html', {'links': ''})

        response = HttpResponse()
        response.write(html)

        # html = html + '02hh_uberintroblock_wmodellinks.html', {'model':'generic_hh','page':'description'}
        # html = html + '03hh_ubertext_links_left.html', {}                       
        # html = html + '04ubertext_start.html', {
        #         'model_page':'#', 
        #         'model_attributes':'Generic Overview', 
        #         'text_paragraph':x}
        # html = html + '04ubertext_end.html', {}
        # html = html + '05hh_ubertext_links_right.html', {}
        # html = html + '06hh_uberfooter.html', {'links': ''}

        # return render(request, html, context)
        return response