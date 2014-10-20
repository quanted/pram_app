from django.template.loader import render_to_string
from collections import OrderedDict


# 03ubertext_links_left:
def linksLeft():
    link_dict = OrderedDict([
        ('Terrestrial Models', OrderedDict([
                ('TerrPlant', 'terrplant'),
                ('SIP', 'sip'),
                ('STIR', 'stir'),
                # ('DUST', 'dust'),
                ('T-REX', 'trex2'),
                ('T-Herps', 'therps'),
                ('IEC', 'iec'),
                ('AgDrift', 'agdrift'),
                ('Agdrift-T-Rex', 'agdrift_trex'),
                ('Agdrift-T-Herps', 'agdrift_therps'),
                ('Earthworm', 'earthworm'),
            ])
        ),
        ('Aquatic Models', OrderedDict([
                ('RICE', 'rice'),
                ('GENEEC', 'geneec'),
                ('Kabam', 'kabam'),
                ('PRZM', 'przm'),
                ('PRZM 5', 'przm5'),
                ('EXAMS', 'exams'),
                ('PFAM', 'pfam'),
                ('PRZM-EXAMS', 'przm_exams'),
                ('SAM', 'sam'),
                # ('Web-ICE', 'webice'),
                # ('VVWM', 'vvwm'),
                # ('Surface Water Calculator', 'swc'),
            ])
        ),
        ('Documentation', OrderedDict([
                ('Source Code', 'docs'),
            ])
        ),
        # ('&uuml;bertool', OrderedDict([
        #         ('Chemical Selection', 'select_chemical'),
        #         ('Use/Label/Site Data', 'site_data'),
        #         ('Pesticide Properties', 'pesticide_properties'),
        #         ('Exposure Concentrations', 'exposure_concentrations'),
        #         ('Aquatic Toxicity', 'aquatic_toxicity'),
        #         ('Terrestrial Toxicity', 'terrestrial_toxicity'),
        #         ('Ecosystem Inputs', 'ecosystem_inputs'),
        #         ('Run &uuml;bertool', 'run_ubertool'),
        #         ('Saved Runs', 'user'),
        #     ])
        # ),
    ])

    html = render_to_string('03ubertext_links_left.html', {'link_dict': link_dict})
    return html