"""
.. module:: agdrift_therps_parameters
   :synopsis: A useful module indeed.
"""
from models.agdrift import agdrift_parameters
from models.therps import therps_parameters


class Agdrift_TherpsInp(agdrift_parameters.AgdriftInp, therps_parameters.TherpsInp):
    pass
