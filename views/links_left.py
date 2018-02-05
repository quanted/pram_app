from collections import OrderedDict
from django.shortcuts import redirect
from django.template.loader import render_to_string


# 03ubertext_links_left:
def ordered_list(model=None, page=None):
    # get right set of links for links left
    if(model in ['agdrift','beerex','iec','sip','stir','terrplant','therps',
                 'trex','kabam','rice','landing_pram']):
        link_dict = ordered_list_pram(model)
    elif(model in ['exponential','logistic','gompertz','foxsurplus','maxsus',
                   'yulefurry','fellerarley','leslie','lesliedr','leslie_probit',
                   'loons','landing_pop']):
        link_dict = ordered_list_pop(model)
    elif(model in ['agdisp','earthworm','insect','pat','perfum','pfam','pwc',
                   'sam','ted','landing_unter']):
        link_dict = ordered_list_unter(model)
    return render_to_string('03ubertext_links_left_drupal.html', {
        'LINK_DICT': link_dict,
        'MODEL': model,
        'PAGE': page
    })


def ordered_list_pram(model=None, page=None):
    link_dict = OrderedDict([
        ('Apps', OrderedDict([
            ('Q.E.D.', '..'),
            ('\u00FCtool', ''),
            ('pop', 'pop'),
            ('unter', 'unter'),
        ])
         ),
        ('Terrestrial Models', OrderedDict([
            ('AgDrift', 'agdrift'),
            ('Bee-REX', 'beerex'),
            ('IEC', 'iec'),
            ('SIP', 'sip'),
            ('STIR', 'stir'),
            ('TerrPlant', 'terrplant'),
            ('T-Herps', 'therps'),
            ('T-REX', 'trex'),
            ])
        ),
        ('Aquatic Models', OrderedDict([
            ('Kabam', 'kabam'),
            ('RICE', 'rice'),
            ])
        ),
        ('Documentation', OrderedDict([
                ('Source Code', '/github.com/quanted/pram'),
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
        #         ('Run &uuml;bertool', 'run_pram'),
        #         ('Saved Runs', 'user'),
        #     ])
        # ),
    ])
    return link_dict


def ordered_list_pop(model=None, page=None):
    link_dict = OrderedDict([
        ('Apps', OrderedDict([
            ('Q.E.D.', '..'),
            ('\u00FCtool', ''),
            ('pop', 'pop'),
            ('unter', 'unter'),
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
        ('Documentation', OrderedDict([
                ('Source Code', redirect('https://github.com/quanted/pram')),
                ('Links', 'links'),
            ])
        ),
    ])
    return link_dict

def ordered_list_unter(model=None, page=None):
    link_dict = OrderedDict([
        ('Apps', OrderedDict([
            ('Q.E.D.', '..'),
            ('\u00FCtool', ''),
            ('pop', 'pop'),
            ('unter', 'unter'),
        ])
         ),
        ('Beta Versions', OrderedDict([
            ('AgDisp', 'agdisp'),
            ('Earthworm', 'earthworm'),
            ('Insect', 'insect'),
            ('Pat', 'pat'),
            ('Perfum', 'perfum'),
            ('Pfam', 'pfam'),
            ('PWC', 'pwc'),
            ('SAM', 'sam'),
            ('TED', 'ted'),
        ])
         ),
        ('Documentation', OrderedDict([
                ('Source Code', '/github.com/quanted/pram'),
                ('Links', 'links')
            ])
        ),
    ])
    return link_dict