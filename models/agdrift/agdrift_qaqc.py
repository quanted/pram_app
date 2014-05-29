import agdrift_model
import os
import unittest
from StringIO import StringIO
import csv

# agdrift_obj = agdrift_model.agdrift(True, True, 'single', drop_size, ecosystem_type, application_method, boom_height, orchard_type, application_rate, distance, aquatic_type, calculation_input, None)

agdrift_obj = agdrift_model.agdrift(True, True, 'qaqc', "Fine", "EPA Pond", "Aerial", "", "", "0.5", "225", "1", "0.5", None)