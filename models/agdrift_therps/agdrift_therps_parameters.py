# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 14:50:59 2012

@author: MSnyder
"""
from django import forms
from django.utils.safestring import mark_safe
from django.core import validators
from models.forms import validation
from models.agdrift import agdrift_parameters
from models.therps import therps_parameters


class Agdrift_TherpsInp(agdrift_parameters.AgdriftInp, therps_parameters.TherpsInp):
    pass