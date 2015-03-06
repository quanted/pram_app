"""
.. module:: ore_output
   :synopsis: A useful module indeed.
"""

from django.views.decorators.http import require_POST
import logging 
@require_POST
def oreOutputPage(request):

    # html = template.render(templatepath + '04uberoutput_start.html', {
    #         'model':'ore', 
    #         'model_attributes':'ORE Output'})
    # html = html + """
    # <div class="out_">
    #     <table >
    #         <th>Output</th>
    #         <tr><td>Default</td></tr>
    #     </table>
    # </div>
    # """

    # return html

    args = { "inputs" : {} }
    for key in request.POST:
        # args["inputs"][key] = {"0" : request.POST.get(key)}
        args["inputs"][key] = request.POST.get(key)
        # logging.info(args["inputs"][key])
    args["run_type"] = "single"

    logging.info(args)

    exp_category = request.POST.get('exp_category')

    logging.info('exp_category: ' + exp_category)

    return "Test"