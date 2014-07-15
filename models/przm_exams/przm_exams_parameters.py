"""
.. module:: przm_exams_parameters
   :synopsis: A useful module indeed.
"""
from django import forms
from django.utils.safestring import mark_safe
from django.core import validators
from models.forms import validation
from models.przm import przm_parameters
from models.exams import exams_parameters


# Combined Form Classes for Validation
class Przm_ExamsInp(przm_parameters.PrzmInp, exams_parameters.ExamsInp):
    pass