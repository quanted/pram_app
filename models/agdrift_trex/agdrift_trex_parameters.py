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
from models.trex2 import trex2_parameters


# Combined Form Classes for Validation
class Agdrift_TrexInp(agdrift_parameters.AgdriftInp, trex2_parameters.Trex2Inp):
    pass