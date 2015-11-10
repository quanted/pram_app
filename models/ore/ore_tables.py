"""
.. module:: ore_tables
   :synopsis: A useful module indeed.
"""

# import numpy
from django.template import Template, Context
from django.utils.safestring import mark_safe
import logging
import time
import datetime



def tmpl_oreOutputHeader():
	tmpl = """
	<h3>Ocuplationsl Handler Non-Cancer Exposure and Risk Estimates</h3>
	<table>
		<tr>
			<th rowspan="2">Exposure Scenario</th>
			<th rowspan="2">Crop or Target</th>
			<th rowspan="2">Level of Concern</th>
			<th>Dermal Unit<br>Exposure<br>(&micro;g/lb ai)</th>
			<th>Inhalation<br>Unit Exposure<br>(&micro;g/lb ai)</th>
			<th rowspan="2">Maximum<br>Application<br>Rate</th>
			<th rowspan="2">Area<br>Treated or<BR>Amount<br>Handled<br>Daily</th>
			<th colspan="2">Dermal</th>
			<th colspan="2">Inhalation</th>
		{% for header in column_headers %}
			<th>{{ header }}</th>
		{% endfor %}
		</tr>
		<tr>
			<th>Mitigation Level</th>
			<th>Mitigation Level</th>
			<th>Dose<br>(mg/kg/day)</th>
			<th>MOE</th>
			<th>Dose<br>(mg/kg/day)</th>
			<th>MOE</th>
		</tr>
	"""

	return tmpl

def tmpl_oreOutputWorkerActivity():
	tmpl = """
	{% for worker_activity in worker_activities %}
		<tr>
			<th class="ore_worker_activity">{{ worker_activity }}</th>
		</tr>
		<tr>
			<td id="exp_scenario_{{ore_worker_activity}}">{{ore_worker_activity}} for {{}} Applications</td>
		</tr>
	{% endfor %}
	</table>
	"""

	return tmpl

tmpl_oreOutput = Template(tmpl_oreOutputHeader())



def timestamp(ore_obj):
	return """
	<br>
	Dummy Timestamp
	"""

def table1():

	html = tmpl_oreOutput.render(Context(dict(foo="", bar="")))

	return html



table1 = """

<table>
	<tr>
		<th>Exposure Scenario</th>
	</tr>
</table>

"""



def table_all(ore_obj):
	html = table1

	return html