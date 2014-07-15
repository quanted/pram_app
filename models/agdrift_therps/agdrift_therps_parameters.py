"""
.. module:: agdrift_therps_parameters
   :synopsis: A useful module indeed.
"""
from django import forms
from django.utils.safestring import mark_safe
from django.core import validators
from models.forms import validation
from models.agdrift import agdrift_parameters
from models.therps import therps_parameters


class Agdrift_TherpsInp(agdrift_parameters.AgdriftInp, therps_parameters.TherpsInp):
    pass
