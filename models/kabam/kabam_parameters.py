"""
.. module:: kabam_parameters
   :synopsis: A useful module indeed.
"""
from django import forms
from django.utils.safestring import mark_safe
from django.core import validators
from models.forms import validation

Species_of_the_tested_bird_CHOICES=(('0','Make a selection'),('178','Northern bobwhite quail'),('1580','Mallard duck'),('1','Other'))
Species_of_the_tested_mamm_CHOICES=(('0','Make a selection'),('350','Laboratory rat'),('1','Other'))
Diet_for_CHOICES=(('Large Fish','Large Fish'),('Medium Fish','Medium Fish'),('Small Fish','Small Fish'),('Filter Feeder','Filter Feeder'),('Benthic Invertebrates','Benthic Invertebrates'),('Zooplankton','Zooplankton'))
Characteristics_of_aquatic_biota_CHOICES=(('Large Fish','Large Fish'),('Medium Fish','Medium Fish'),('Small Fish','Small Fish'),('Filter Feeder','Filter Feeder'),('Benthic Invertebrates','Benthic Invertebrates'),('Zooplankton','Zooplankton'),('Phytoplankton','Phytoplankton'),('Sediment','Sediment'))
Respire_CHOICES=(('Yes','Yes'),('No','No'))
Rate_constants_CHOICES=(('0','Make a selection'),('a','Use default values'),('b','Input rate constants'))


class KabamInp_chem(forms.Form):
    name = forms.CharField(
            widget=forms.Textarea (attrs={'cols': 20, 'rows': 2}),
            initial='Chemical X')
    lkow = forms.FloatField(
            label=mark_safe('Log K<sub>OW</sub>'),
            initial=5,
            validators=[validation.validate_greaterthan0])
    Koc = forms.FloatField(
            label=mark_safe('K<sub>OC</sub> (L/kg OC)'),
            initial=25000,
            validators=[validation.validate_greaterthan0])
    beec = forms.FloatField(
            label=mark_safe('Pore water (benthic) EECs (&#956;g/L)'),
            initial=5,
            validators=[validation.validate_greaterthan0])
    weec = forms.FloatField(
            label=mark_safe('Water Column 1-in-10 year EECs (&#956;g/L)'),
            initial=6,
            validators=[validation.validate_greaterthan0])
    sf = forms.FloatField(
            label='Chemical Specific Mineau scaling factor',
            initial=1.15,
            validators=[validation.validate_greaterthanequalto1])
    cpoc = forms.FloatField(
            label=mark_safe('Concentration of Particulate Organic Carbon (X<sub>POC</sub>; kg OC/L)'),
            initial=0,
            validators=[validation.validate_positive])
    cdoc = forms.FloatField(
            label=mark_safe('Concentration of Dissolved Organic Carbon (X<sub>DOC</sub>; kg OC/L)'),
            initial=0,
            validators=[validation.validate_positive])
    cox = forms.FloatField(
            label=mark_safe('Concentration of Dissolved Oxygen (C<sub>OX</sub>; mg O<sup>2</sup>/L)'),
            initial=5,
            validators=[validation.validate_positive])
    wt = forms.FloatField(
            label=mark_safe('Water Temperature (T; &degC)'),
            initial=15,
            validators=[validation.validate_range0100])
    css = forms.FloatField(
            label=mark_safe('Concentration of Suspended Solids (C<sub>SS</sub>; kg/L)'),
            initial=0.00003,
            validators=[validation.validate_positive])
    oc = forms.FloatField(
            label=mark_safe('Sediment Organic Carbon (OC; %)'),
            initial=4,
            validators=[validation.validate_positive])

class KabamInp_bird(forms.Form):
    Species_of_the_tested_bird = forms.ChoiceField(
            label='Species of the tested bird',
            choices=Species_of_the_tested_bird_CHOICES,
            initial='178',
            validators=[validation.validate_choicefield])
    bw_quail = forms.FloatField(
            label='Weight of the tested bird', 
            initial= 178,
            validators=[validation.validate_greaterthan0])
    bw_duck = forms.FloatField(
            label='Weight of the tested bird', 
            initial= 1580,
            validators=[validation.validate_greaterthan0])
    bwb_other = forms.FloatField(
            label='Weight of the tested bird', 
            initial= 200,
            validators=[validation.validate_greaterthan0])
    ald50 = forms.FloatField(
            label='Avian LD50 (mg/kg-bw)', 
            initial=50,
            validators=[validation.validate_greaterthan0])
    alc50 = forms.FloatField(
            label='Avian LC50 (mg/kg-diet)', 
            initial=500,
            validators=[validation.validate_greaterthan0])
    aNOAEC = forms.FloatField(
            label='Avian NOAEC (mg/kg-diet)', 
            initial=10,
            validators=[validation.validate_greaterthan0])

class KabamInp_mammal(forms.Form):
    m_species = forms.ChoiceField(
            label='Species of the tested mammal',
            choices=Species_of_the_tested_mamm_CHOICES, 
            initial='350',
            validators=[validation.validate_choicefield])    
    bw_rat= forms.FloatField(
            label='Body weight of the tested mammalian (g)', 
            initial=350,
            validators=[validation.validate_greaterthan0])
    bwm_other= forms.FloatField(
            label='Body weight of the tested mammalian (g)', 
            initial=500,
            validators=[validation.validate_greaterthan0])
    mld50 = forms.FloatField(
            label='Mammalian LD50 (mg/kg-bw)', 
            initial='50',
            validators=[validation.validate_greaterthan0])
    mlc50 = forms.FloatField(
            label='Mammalian LC50 (mg/kg-diet)', 
            initial='45',
            validators=[validation.validate_greaterthan0])
    m_chronic = forms.FloatField(
            label='Mammalian chronic endpoint (ppm)', 
            initial='10',
            validators=[validation.validate_greaterthan0])

class KabamInp_lfish(forms.Form):
    #Diet_lfish = forms.ChoiceField(label='Diet for', choices=Diet_for_CHOICES, 
        # initial='Large Fish')
    lfish_p_sediment = forms.FloatField(
            label='Large Fish Diet Sediment (%)', 
            initial='0',
            validators=[validation.validate_positive])
    lfish_p_phyto = forms.FloatField(
            label='Large Fish Diet Phytoplankton (%)', 
            initial='0',
            validators=[validation.validate_positive])
    lfish_p_zoo = forms.FloatField(
            label='Large Fish Diet Zooplankton (%)', 
            initial='0',
            validators=[validation.validate_positive])
    lfish_p_beninv = forms.FloatField(
            label='Large Fish Diet Benthic invertebrates (%)', 
            initial='0',
            validators=[validation.validate_positive])
    lfish_p_ff = forms.FloatField(
            label='Large Fish Diet Filter feeders (%)', 
            initial='0',
            validators=[validation.validate_positive])
    lfish_p_sfish = forms.FloatField(
            label='Large Fish Diet Small Fish (%)', 
            initial='0',
            validators=[validation.validate_positive])
    lfish_p_mfish = forms.FloatField(
            label='Large Fish Diet Medium Fish (%)', 
            initial='100',
            validators=[validation.validate_positive])
    #char_lfish = forms.ChoiceField(label='Characteristics of aquatic biota:', choices=Characteristics_of_aquatic_biota_CHOICES, 
        # initial='Large Fish')
    lfish_ww = forms.FloatField(
            label='Large Fish (kg)', 
            initial=1.0,
            validators=[validation.validate_positive])
    lfish_lipid = forms.FloatField(
            label='Large Fish % lipids', 
            initial=4,
            validators=[validation.validate_positive])
    lfish_NLOM = forms.FloatField(
            label='Large Fish % NLOM', 
            initial=23,
            validators=[validation.validate_positive])
    lfish_water = forms.FloatField(
            label='Large Fish % Water', 
            initial=73,
            validators=[validation.validate_positive])
    lfish_respire = forms.ChoiceField(label='Do organisms in trophic level respire some pore water?',
            choices=Respire_CHOICES, 
            initial='No')

class KabamInp_mfish(forms.Form):
    #Diet_mfish = forms.ChoiceField(label='Diet for', choices=Diet_for_CHOICES, 
        # initial='Medium Fish')
    mfish_p_sediment = forms.FloatField(
            label='Medium Fish Diet Sediment (%)', 
            initial='0',
            validators=[validation.validate_positive])
    mfish_p_phyto = forms.FloatField(
            label='Medium Fish Diet Phytoplankton (%)', 
            initial='0',
            validators=[validation.validate_positive])
    mfish_p_zoo = forms.FloatField(
            label='Medium Fish Diet Zooplankton (%)', 
            initial='0',
            validators=[validation.validate_positive])
    mfish_p_beninv = forms.FloatField(
            label='Medium Fish Diet Benthic Invertebrates (%)', 
            initial='50',
            validators=[validation.validate_positive])
    mfish_p_ff = forms.FloatField(
            label='Medium Fish Diet Filter Feeders (%)', 
            initial='0',
            validators=[validation.validate_positive])
    mfish_p_sfish = forms.FloatField(
            label='Medium Fish Diet Small Fish (%)', 
            initial='50',
            validators=[validation.validate_positive])
    #char_mfish = forms.ChoiceField(label='Characteristics of aquatic biota:', choices=Characteristics_of_aquatic_biota_CHOICES, 
        # initial='Medium Fish')
    mfish_ww = forms.FloatField(
            label='Medium Fish (kg)', 
            initial=1.0E-1,
            validators=[validation.validate_positive])
    mfish_lipid = forms.FloatField(
            label='Medium Fish % lipids', 
            initial=4,
            validators=[validation.validate_positive])
    mfish_NLOM = forms.FloatField(
            label='Medium Fish % NLOM', 
            initial=23,
            validators=[validation.validate_positive])
    mfish_water = forms.FloatField(
            label='Medium Fish % Water', 
            initial=73,
            validators=[validation.validate_positive])
    mfish_respire = forms.ChoiceField(label='Do organisms in trophic level respire some pore water?',
            choices=Respire_CHOICES, 
            initial='Yes')

class KabamInp_sfish(forms.Form):    
    #Diet_sfish = forms.ChoiceField(label='Diet for', choices=Diet_for_CHOICES, 
        # initial='Small Fish')
    sfish_p_sediment = forms.FloatField(
            label='Small Fish Diet Sediment (%)', 
            initial='0',
            validators=[validation.validate_positive])
    sfish_p_phyto = forms.FloatField(
            label='Small Fish Diet Phytoplankton (%)', 
            initial='0',
            validators=[validation.validate_positive])
    sfish_p_zoo = forms.FloatField(
            label='Small Fish Diet Zooplankton (%)', 
            initial='50',
            validators=[validation.validate_positive])
    sfish_p_beninv = forms.FloatField(
            label='Small Fish Diet Benthic invertebrates (%)', 
            initial='50',
            validators=[validation.validate_positive])
    sfish_p_ff = forms.FloatField(
            label='Small Fish Diet Filter feeders (%)', 
            initial='0',
            validators=[validation.validate_positive])
    #char_sfish = forms.ChoiceField(label='Characteristics of aquatic biota:', choices=Characteristics_of_aquatic_biota_CHOICES, 
        # initial='Small Fish')
    sfish_ww = forms.FloatField(
            label='Small Fish (kg)', 
            initial=1.0E-2,
            validators=[validation.validate_positive])
    sfish_lipid = forms.FloatField(
            label='Small Fish % lipids', 
            initial=4,
            validators=[validation.validate_positive])
    sfish_NLOM = forms.FloatField(
            label='Small Fish % NLOM', 
            initial=23,
            validators=[validation.validate_positive])
    sfish_water = forms.FloatField(
            label='Small Fish % Water', 
            initial=73,
            validators=[validation.validate_positive])
    sfish_respire = forms.ChoiceField(label='Do organisms in trophic level respire some pore water?',
            choices=Respire_CHOICES, 
            initial='Yes')

class KabamInp_ff(forms.Form):    
    #Diet_ff = forms.ChoiceField(label='Diet for', choices=Diet_for_CHOICES, 
        # initial='Filter Feeder')
    ff_p_sediment = forms.FloatField(
            label='Filter Feeder Diet Sediment (%)', 
            initial='34',
            validators=[validation.validate_positive])
    ff_p_phyto = forms.FloatField(
            label='Filter Feeder Diet Phytoplankton (%)', 
            initial='33',
            validators=[validation.validate_positive])
    ff_p_zoo = forms.FloatField(
            label='Filter Feeder Diet Zooplankton (%)', 
            initial='33',
            validators=[validation.validate_positive])
    ff_p_beninv = forms.FloatField(
            label='Filter Feeder Diet Benthic invertebrates (%)', 
            initial='0',
            validators=[validation.validate_positive])
    #char_ff = forms.ChoiceField(label='Characteristics of aquatic biota:', choices=Characteristics_of_aquatic_biota_CHOICES, 
        # initial='Filter Feeder')
    ff_ww = forms.FloatField(
            label='Filter Feeders (kg)', 
            initial=1.0E-3,
            validators=[validation.validate_positive])
    ff_lipid = forms.FloatField(
            label='Filter Feeders % lipids', 
            initial=2,
            validators=[validation.validate_positive])
    ff_NLOM = forms.FloatField(
            label='Filter Feeders % NLOM', 
            initial=13,
            validators=[validation.validate_positive])
    ff_water = forms.FloatField(
            label='Filter Feeders % Water', 
            initial=85,
            validators=[validation.validate_positive])
    ff_respire = forms.ChoiceField(label='Do organisms in trophic level respire some pore water?',
            choices=Respire_CHOICES, 
            initial='Yes')

class KabamInp_invert(forms.Form):    
    #Diet_invert = forms.ChoiceField(label='Diet for', choices=Diet_for_CHOICES, 
        # initial='Benthic Invertebrates')
    beninv_p_sediment = forms.FloatField(
            label='Benthic Invertebrates Diet Sediment (%)', 
            initial='34',
            validators=[validation.validate_positive])
    beninv_p_phyto = forms.FloatField(
            label='Benthic Invertebrates Diet Phytoplankton (%)', 
            initial='33',
            validators=[validation.validate_positive])
    beninv_p_zoo = forms.FloatField(
            label='Benthic Invertebrates Diet Zooplankton (%)', 
            initial='33',
            validators=[validation.validate_positive])
    #char_beninv = forms.ChoiceField(label='Characteristics of aquatic biota:', choices=Characteristics_of_aquatic_biota_CHOICES, 
        # initial='Benthic Invertebrates')
    beninv_ww = forms.FloatField(
            label='Benthic Invertebrates (kg)', 
            initial=1.0E-4,
            validators=[validation.validate_positive])
    beninv_lipid = forms.FloatField(
            label='Benthic Invertebrates % lipids', 
            initial=3,
            validators=[validation.validate_positive])
    beninv_NLOM = forms.FloatField(
            label='Benthic Invertebrates % NLOM', 
            initial=21,
            validators=[validation.validate_positive])
    beninv_water = forms.FloatField(
            label='Benthic Invertebrates % Water', 
            initial=76,
            validators=[validation.validate_positive])
    beninv_respire = forms.ChoiceField(label='Do organisms in trophic level respire some pore water?',
            choices=Respire_CHOICES, 
            initial='Yes')

class KabamInp_zoo(forms.Form):    
    #Diet_zoo = forms.ChoiceField(label='Diet for', choices=Diet_for_CHOICES, 
        # initial='Zooplankton')
    zoo_p_sediment = forms.FloatField(
            label='Zooplankton Diet Sediment (%)', 
            initial='0',
            validators=[validation.validate_positive])
    zoo_p_phyto = forms.FloatField(
            label='Zooplankton Diet Phytoplankton (%)', 
            initial='100',
            validators=[validation.validate_positive])
    #char_zoo = forms.ChoiceField(label='Characteristics of aquatic biota:', choices=Characteristics_of_aquatic_biota_CHOICES, 
        # initial='Zooplankton')
    zoo_ww = forms.FloatField(
            label='Zooplankton (kg)', 
            initial=0.0000001,
            validators=[validation.validate_positive])
    zoo_lipid = forms.FloatField(
            label='Zooplankton % lipids', 
            initial=3,
            validators=[validation.validate_positive])
    zoo_NLOM = forms.FloatField(
            label='Zooplankton % NLOM', 
            initial=12,
            validators=[validation.validate_positive])
    zoo_water = forms.FloatField(
            label='Zooplankton % Water', 
            initial=85,
            validators=[validation.validate_positive])
    zoo_respire = forms.ChoiceField(
            label='Do organisms in trophic level respire some pore water?',
            choices=Respire_CHOICES, 
            initial='No')

class KabamInp_sed(forms.Form):    
    #char_s = forms.ChoiceField(label='Characteristics of aquatic biota:', choices=Characteristics_of_aquatic_biota_CHOICES, 
        # initial='Sediment')
    s_lipid = forms.FloatField(
            label='Sediment % lipids', 
            initial=0,
            validators=[validation.validate_positive])
    s_NLOM = forms.FloatField(
            label='Sediment % NLOM', 
            initial=4,
            validators=[validation.validate_positive])
    s_water = forms.FloatField(
            label='Sediment % Water', 
            initial=96,
            validators=[validation.validate_positive])
    s_respire = forms.ChoiceField(label='Do organisms in trophic level respire some pore water?',
            choices=Respire_CHOICES, 
            initial='No')

class KabamInp_phyto(forms.Form):    
    #char_phyto = forms.ChoiceFieldlabel='Characteristics of aquatic biota:', choices=Characteristics_of_aquatic_biota_CHOICES, 
    #   initial='Phytoplankton')
    phyto_lipid = forms.FloatField(
            label='Phytoplankton % lipids', 
            initial=2,
            validators=[validation.validate_positive])
    phyto_NLOM = forms.FloatField(
            label='Phytoplankton % NLOM', 
            initial=8,
            validators=[validation.validate_positive])
    phyto_water = forms.FloatField(
            label='Phytoplankton % Water', 
            initial=90,
            validators=[validation.validate_positive])
    phyto_respire = forms.ChoiceField(
            label='Do organisms in trophic level respire some pore water?',
            choices=Respire_CHOICES, 
            initial='No')
    
#####input parameters for rate constants
class KabamInp_constants(forms.Form):    
    rate_c = forms.ChoiceField(
            label='Rate constants for uptake and elimination',
            choices=Rate_constants_CHOICES, 
            initial='a',
            validators=[validation.validate_choicefield])
    phyto_k1 = forms.FloatField(
            label=mark_safe('phytoplankton k<sub>1</sub> (L/kg*d)'),
            initial=1,
            validators=[validation.validate_positive])
    phyto_k2 = forms.FloatField(
            label=mark_safe('phytoplankton k<sub>2</sub> (d<sup>-1</sup>)'),
            initial=1,
            validators=[validation.validate_positive])
    phyto_kd = forms.FloatField(
            label=mark_safe('phytoplankton k<sub>D</sub> (kg-food/kg-org/d)'),
            initial=0,
            validators=[validation.validate_positive])
    phyto_ke = forms.FloatField(
            label=mark_safe('phytoplankton k<sub>E</sub> (d<sup>-1</sup>)'), 
            initial=0,
            validators=[validation.validate_positive])
    phyto_km = forms.FloatField(
            label=mark_safe('phytoplankton k<sub>M</sub> (d<sup>-1</sup>)'),
            initial=0,
            validators=[validation.validate_positive])
    zoo_k1 = forms.FloatField(
            label=mark_safe('zooplankton k<sub>1</sub> (L/kg*d)'),
            initial=1,
            validators=[validation.validate_positive])
    zoo_k2 = forms.FloatField(
            label=mark_safe('zooplankton k<sub>2</sub> (d<sup>-1</sup>)'),
            initial=1,
            validators=[validation.validate_positive])
    zoo_kd = forms.FloatField(
            label=mark_safe('zooplankton k<sub>D</sub> (kg-food/kg-org/d)'),
            initial=1,
            validators=[validation.validate_positive])
    zoo_ke = forms.FloatField(
            label=mark_safe('zooplankton k<sub>E</sub> (d<sup>-1</sup>)'),
            initial=1,
            validators=[validation.validate_positive])
    zoo_km = forms.FloatField(
            label=mark_safe('zooplankton k<sub>M</sub> (d<sup>-1</sup>)'),
            initial=0,
            validators=[validation.validate_positive])
    beninv_k1 = forms.FloatField(
            label=mark_safe('benthic invertebrates k<sub>1</sub> (L/kg*d)'),
            initial=1,
            validators=[validation.validate_positive])
    beninv_k2 = forms.FloatField(
            label=mark_safe('benthic invertebrates k<sub>2</sub> (d<sup>-1</sup>)'),
            initial=1,
            validators=[validation.validate_positive])
    beninv_kd = forms.FloatField(
            label=mark_safe('benthic invertebrates k<sub>D</sub> (kg-food/kg-org/d)'),
            initial=1,
            validators=[validation.validate_positive])
    beninv_ke = forms.FloatField(
            label=mark_safe('benthic invertebrates k<sub>E</sub> (d<sup>-1</sup>)'),
            initial=1,
            validators=[validation.validate_positive])
    beninv_km = forms.FloatField(
            label=mark_safe('benthic invertebrates k<sub>M</sub> (d<sup>-1</sup>)'),
            initial=0,
            validators=[validation.validate_positive])
    ff_k1 = forms.FloatField(
            label=mark_safe('filter feeders k<sub>1</sub> (L/kg*d)'),
            initial=1,
            validators=[validation.validate_positive])
    ff_k2 = forms.FloatField(
            label=mark_safe('filter feeders k<sub>2</sub> (d<sup>-1</sup>)'),
            initial=1,
            validators=[validation.validate_positive])
    ff_kd = forms.FloatField(
            label=mark_safe('filter feeders k<sub>D</sub> (kg-food/kg-org/d)'),
            initial=1,
            validators=[validation.validate_positive])
    ff_ke = forms.FloatField(
            label=mark_safe('filter feeders k<sub>E</sub> (d<sup>-1</sup>)'),
            initial=1,
            validators=[validation.validate_positive])
    ff_km = forms.FloatField(
            label=mark_safe('filter feeders k<sub>M</sub> (d<sup>-1</sup>)'),
            initial=0,
            validators=[validation.validate_positive])
    sfish_k1 = forms.FloatField(
            label=mark_safe('small fish k<sub>1</sub> (L/kg*d)'),
            initial=1,
            validators=[validation.validate_positive])
    sfish_k2 = forms.FloatField(
            label=mark_safe('small fish k<sub>2</sub> (d<sup>-1</sup>)'),
            initial=1,
            validators=[validation.validate_positive])
    sfish_kd = forms.FloatField(
            label=mark_safe('small fish k<sub>D</sub> (kg-food/kg-org/d)'),
            initial=1,
            validators=[validation.validate_positive])
    sfish_ke = forms.FloatField(
            label=mark_safe('small fish k<sub>E</sub> (d<sup>-1</sup>)'),
            initial=1,
            validators=[validation.validate_positive])
    sfish_km = forms.FloatField(
            label=mark_safe('small fish k<sub>M</sub> (d<sup>-1</sup>)'),
            initial=0,
            validators=[validation.validate_positive])
    mfish_k1 = forms.FloatField(
            label=mark_safe('medium fish k<sub>1</sub> (L/kg*d)'),
            initial=1,
            validators=[validation.validate_positive])
    mfish_k2 = forms.FloatField(
            label=mark_safe('medium fish k<sub>2</sub> (d<sup>-1</sup>)'),
            initial=1,
            validators=[validation.validate_positive])
    mfish_kd = forms.FloatField(
            label=mark_safe('medium fish k<sub>D</sub> (kg-food/kg-org/d)'),
            initial=1,
            validators=[validation.validate_positive])
    mfish_ke = forms.FloatField(
            label=mark_safe('medium fish k<sub>E</sub> (d<sup>-1</sup>)'),
            initial=1,
            validators=[validation.validate_positive])
    mfish_km = forms.FloatField(
            label=mark_safe('medium fish k<sub>M</sub> (d<sup>-1</sup>)'),
            initial=0,
            validators=[validation.validate_positive])
    lfish_k1 = forms.FloatField(
            label=mark_safe('large fish k<sub>1</sub> (L/kg*d)'),
            initial=1,
            validators=[validation.validate_positive])
    lfish_k2 = forms.FloatField(
            label=mark_safe('large fish k<sub>2</sub> (d<sup>-1</sup>)'),
            initial=1,
            validators=[validation.validate_positive])
    lfish_kd = forms.FloatField(
            label=mark_safe('large fish k<sub>D</sub> (kg-food/kg-org/d)'),
            initial=1,
            validators=[validation.validate_positive])
    lfish_ke = forms.FloatField(
            label=mark_safe('large fish k<sub>E</sub> (d<sup>-1</sup>)'),
            initial=1,
            validators=[validation.validate_positive])
    lfish_km = forms.FloatField(
            label=mark_safe('large fish k<sub>M</sub> (d<sup>-1</sup>)'),
            initial=0,
            validators=[validation.validate_positive])


# Combined Form Classes for Validation
class KabamInp( KabamInp_chem, KabamInp_bird, KabamInp_mammal,
                KabamInp_lfish, KabamInp_mfish, KabamInp_sfish, 
                KabamInp_ff, KabamInp_invert, KabamInp_zoo, 
                KabamInp_sed, KabamInp_phyto, KabamInp_constants    ):
    pass