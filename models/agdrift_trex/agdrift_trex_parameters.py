"""
.. module:: agdrift_trex_parameters
   :synopsis: A useful module indeed.
"""
from models.agdrift import agdrift_parameters
from models.trex import trex2_parameters

# Combined Form Classes for Validation
class Agdrift_TrexInp(agdrift_parameters.AgdriftInp, trex2_parameters.Trex2Inp):
    pass
