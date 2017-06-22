from collections import OrderedDict

from django.template.loader import render_to_string


# 03ubertext_links_left:
def ordered_list(model=None, page=None):
    link_dict = OrderedDict([
        ('utool', OrderedDict([
            ('home', ''),
        ])
         ),
        ('Terrestrial Models', OrderedDict([
                ('TerrPlant', 'terrplant'),
                ('SIP', 'sip'),
                ('STIR', 'stir'),
                # ('DUST', 'dust'),
                ('T-REX', 'trex'),
                ('T-Herps', 'therps'),
                ('IEC', 'iec'),
                ('AgDrift', 'agdrift'),
                # ('Agdrift-T-Rex', 'agdrift_trex'),
                # ('Agdrift-T-Herps', 'agdrift_therps'),
                ('Earthworm', 'earthworm'),
                ('Bee-REX', 'beerex'),
            ])
        ),
        ('Aquatic Models', OrderedDict([
                ('RICE', 'rice'),
                # ('GENEEC', 'geneec'),
                ('Kabam', 'kabam'),
                # ('PRZM', 'przm'),
                # ('PRZM 5', 'przm5'),
                # ('EXAMS', 'exams'),
                # ('PFAM', 'pfam'),
                # ('PRZM-EXAMS', 'przm_exams'),
                ('SAM', 'sam_new'),
                #('SWC', 'swc'),
                # ('Web-ICE', 'webice'),
                # ('VVWM', 'vvwm'),
                # ('Surface Water Calculator', 'swc'),
            ])
        ),
        ('Population Models', OrderedDict([
            ('Exponential', 'exponential'),
            ('Logistic', 'logistic'),
            ('Gompertz', 'gompertz'),
            ('Fox Surplus Yield', 'foxsurplus'),
            ('Max Sustainable Yield', 'maxsus'),
            ('Yule-Furry Markov Process', 'yulefurry'),
            ('Feller-Arley Markov Process', 'fellerarley'),
            ('Leslie Process', 'leslie'),
            ('Leslie-Logistic Dose Response', 'lesliedr'),
            ('Leslie-Probit Dose Response', 'leslie_probit'),
            ('Loons Population', 'loons'),
        ])
         ),
        ('Beta Versions', OrderedDict([
            ('AgDisp', 'agdisp'),
            ('Perfum', 'perfum'),
            ('Pfam', 'pfam'),
            ('PWC', 'pwc'),
            ('TED', 'ted'),
        ])
         ),
        ('Documentation', OrderedDict([
                ('Source Code', 'docs'),
                ('API Documentation', 'api'),
                ('Links', 'links')
            ])
        )
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

    return render_to_string('03ubertext_links_left_drupal.html', {
        'LINK_DICT': link_dict,
        'MODEL': model,
        'PAGE': page
    })