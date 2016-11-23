"""
.. module:: beerex_tooltips
   :synopsis: A useful module indeed.
"""


# Dictionary for tooltips, where 'key' = the var name in (model)_parameters, and 'value' = the tooltip text
tooltips = {
    'chemical_name': 'The common name of the chemical',
    'crop_type': 'Type of crop used',
    'application_rate': 'Rate at which pesticide is applied to crops (lb a.i./A)',
    'application_method': 'Pesticide application method',
    'empirical_residue': 'Is there empirical data available on pesticide residue in pollen, nectar, or jelly?',
    'empirical_pollen': 'Empirical pesticide residue in pollen',
    'empirical_nectar': 'Empirical pesticide residue in nectar',
    'empirical_jelly': 'Empirical pesticide residue in jelly',
    'adult_contact_ld50': 'Contact LD50 of adult honeybee (ug a.i./bee)',
    'adult_oral_ld50': 'Oral LD50 of adult honeybee (ug a.i./bee)',
    'adult_oral_noael': 'Oral NOAEL of adult honeybee (ug a.i./bee)',
    'larval_ld50': 'LD50 of honeybee larval (ug a.i./bee)',
    'larval_noael': 'NOAEL of honeybee larval (ug a.i./bee)',
    'log_kow': 'K<sub>OW</sub> of pesticide in log scale',
    'koc': 'K<sub>OW</sub> of pesticide',
    'mass_tree_vegetation': 'Mass of tree vegetation (kg-wet weight)',
    'lw1_jelly': 'larval worker bee jelly consumption rate (mg/day)',
    'lw2_jelly': 'larval worker bee jelly consumption rate (mg/day)',
    'lw3_jelly': 'larval worker bee jelly consumption rate (mg/day)',
    'lw4_nectar': 'larval worker bee nectar consumption rate (mg/day)',
    'lw4_pollen': 'larval worker bee pollen consumption rate (mg/day)',
    'lw5_nectar': 'larval worker bee nectar consumption rate (mg/day)',
    'lw5_pollen': 'larval worker bee pollen consumption rate (mg/day)',
    'ld6_nectar': 'larval drone bee nectar consumption rate (mg/day)',
    'ld6_pollen': 'larval drone bee pollen consumption rate (mg/day)',
    'lq1_jelly': 'larval queen bee jelly consumption rate (mg/day)',
    'lq2_jelly': 'larval queen bee jelly consumption rate (mg/day)',
    'lq3_jelly': 'larval queen bee jelly consumption rate (mg/day)',
    'lq4_jelly': 'larval queen bee jelly consumption rate (mg/day)',
    'aw_cell_nectar': 'adult worker bee nectar consumption rate (mg/day)',
    'aw_cell_pollen': 'adult worker bee pollen consumption rate (mg/day)',
    'aw_brood_nectar': 'adult worker bee nectar consumption rate (mg/day)',
    'aw_brood_pollen': 'adult worker bee pollen consumption rate (mg/day)',
    'aw_comb_nectar': 'adult worker bee nectar consumption rate (mg/day)',
    'aw_comb_pollen': 'adult worker bee pollen consumption rate (mg/day)',
    'aw_fpollen_nectar': 'adult worker bee nectar consumption rate (mg/day)',
    'aw_fpollen_pollen': 'adult worker bee pollen consumption rate (mg/day)',
    'aw_fnectar_nectar': 'adult worker bee nectar consumption rate (mg/day)',
    'aw_fnectar_pollen': 'adult worker bee pollen consumption rate (mg/day)',
    'aw_winter_nectar': 'adult worker bee nectar consumption rate (mg/day)',
    'aw_winter_pollen': 'adult worker bee pollen consumption rate (mg/day)',
    'ad_nectar': 'adult drone bee nectar consumption rate (mg/day)',
    'ad_pollen': 'adult drone bee pollen consumption rate (mg/day)',
    'aq_jelly': 'adult queen bee jelly consumption rate (mg/day)'
}