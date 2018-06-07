""""
.. module:: varroapop_tables
   :synopsis: A useful module indeed.
"""

import datetime
import logging
import pandas as pd
import math
from bokeh.plotting import figure, show
from bokeh.embed import file_html
from bokeh.models import ColumnDataSource, Range1d, BoxAnnotation, LinearAxis
from bokeh.resources import CDN

from .varroapop_parameters import application_type_CHOICES

from django.template import Context, Template
from django.utils.safestring import mark_safe

logger = logging.getLogger("varroapopTables")


class VarroapopPlots(object):
    def __init__(self, varroapop_obj):
      self.data = varroapop_obj.pd_obj_out.loc[1:].copy()
      self.data['out_date'] = pd.to_datetime(self.data['out_date'], format="%m/%d/%Y")
      self.model_obj = varroapop_obj


    def bee_pop_plot(self):
      source = ColumnDataSource(self.data)
      p = figure(plot_width=1000, plot_height=400, x_axis_type="datetime", title= "Click legend entries to show/hide",
                   toolbar_location="above")
      r_csize = p.line(x='out_date', y='out_colony_size', source=source, color='navy', alpha=0.5,
             line_width = 6, legend='Colony size', line_join = 'round')
      r_foragers = p.line(x='out_date', y='out_foragers', source=source, color='mediumseagreen', alpha=0.5,
                       line_width=4, legend='Foragers', line_join = 'round')
      r_wadult = p.line(x='out_date', y='out_adult_workers', source=source, color='darkred', alpha=0.5,
             line_width=4, legend='Worker adults', line_join = 'round')
      r_wbrood = p.line(x='out_date', y='out_capped_worker_brood', source=source, color='tomato', alpha=0.5,
                        line_width=4, legend='Worker brood', line_join = 'round')
      r_wlarvae = p.line(x='out_date', y='out_worker_larvae', source=source, color='orange', alpha=0.5,
                        line_width=4, legend='Worker larvae', line_join = 'round')
      r_weggs = p.line(x='out_date', y='out_worker_eggs', source=source, color='yellow', alpha=0.5,
                        line_width=4, legend='Worker eggs', line_join = 'round')
      r_dadult = p.line(x='out_date', y='out_adult_drones', source=source, color='slategray', alpha=0.5,
             line_width=4, legend='Drone adults', line_join = 'round')
      p.yaxis.axis_label = '# of individuals'
      y_max = math.ceil(self.data['out_colony_size'].max()/5000)*5000
      p.y_range = Range1d(start=0,end=y_max, bounds = 'auto')
      p.legend.location = 'top_left'
      p.legend.click_policy="hide"
      self.bee_pop = p
      p = self.add_exposure_label(p)
      html = file_html(p, CDN, "population_plot")
      return html


    def pol_nec_plot(self):
        source = ColumnDataSource(self.data)
        p = figure(plot_width=1000, plot_height=400, x_axis_type="datetime", title="Click legend entries to show/hide",
                   toolbar_location="above")
        y_max = max(self.model_obj.MaxColPollen, self.model_obj.MaxColNectar) + 1000
        conc_y_max = self.data['out_chemical_conc_pollen'].append(self.data['out_chemical_conc_nectar']).max()
        conc_y_max = conc_y_max + conc_y_max*.5
        if conc_y_max == 0: conc_y_max = 10
        p.yaxis.axis_label = 'grams'
        p.y_range = Range1d(start=0, end=y_max, bounds='auto')
        p.extra_y_ranges = {"conc": Range1d(0,conc_y_max,bounds="auto")}
        p.add_layout(LinearAxis(y_range_name="conc", axis_label = 'A.I. concentration (\u03bcg/g)'), 'right')
        r_pollen = p.line(x='out_date', y='out_colony_pollen', source=source, color='navy', alpha=0.5,
                         line_width=6, legend='Colony pollen', line_join = 'round')
        r_nectar = p.line(x='out_date', y='out_colony_nectar', source=source, color='darkred', alpha=0.5,
                          line_width=6, legend='Colony nectar', line_join = 'round')
        r_pollenc = p.line(x='out_date', y='out_chemical_conc_pollen', source=source, color='navy', alpha=0.5,
                          line_width=4, legend='A.I. in pollen', y_range_name = 'conc',
                           line_dash='dashed', line_join = 'round')
        r_nectarc = p.line(x='out_date', y='out_chemical_conc_nectar', source=source, color='darkred', alpha=0.5,
                           line_width=4, legend='A.I. in nectar', y_range_name = 'conc',
                           line_dash='dashed', line_join = 'round')
        p.legend.location = 'top_left'
        p.legend.click_policy = "hide"
        self.pol_nec = p
        p = self.add_exposure_label(p)
        html = file_html(p, CDN, "nec_pol_plot")
        return html


    def mites_plot(self):
            source = ColumnDataSource(self.data)
            p = figure(plot_width=1000, plot_height=400, x_axis_type="datetime",
                       title="Click legend entries to show/hide",
                       toolbar_location="above")
            y_max = math.ceil((self.data['out_free_mites'].append(self.data['out_worker_brood_mites']).append(
                              self.data['out_mites_dying']).max() + .01) / 10000) * 10000 #round max up to nearest 10k
            #conc_y_max = self.data['out_chemical_conc_pollen'].append(self.data['out_chemical_conc_nectar']).max()
            #conc_y_max = conc_y_max + conc_y_max * .5
           # if conc_y_max == 0: conc_y_max = 10
            p.yaxis.axis_label = '# of mites'
            p.y_range = Range1d(start=0, end=y_max, bounds='auto')
            #p.extra_y_ranges = {"conc": Range1d(0, conc_y_max, bounds="auto")}
           # p.add_layout(LinearAxis(y_range_name="conc", axis_label='A.I. concentration (\u03bcg/g)'), 'right')
            r_freemites = p.line(x='out_date', y='out_free_mites', source=source, color='navy', alpha=0.5,
                              line_width=6, legend='Free mites', line_join='round')
            r_workerbroodm = p.line(x='out_date', y='out_worker_brood_mites', source=source, color='darkred', alpha=0.5,
                              line_width=6, legend='Worker brood mites', line_join='round')
            r_dronebroodm = p.line(x='out_date', y='out_drone_brood_mites', source=source, color='olive', alpha=0.5,
                               line_width=6, legend='Drone brood mites',line_dash='solid', line_join='round')
            r_mitesdying = p.line(x='out_date', y='out_mites_dying', source=source, color='slategray', alpha=0.5,
                               line_width=6, legend='Mite mortality', line_dash='solid', line_join='round')
            p.legend.location = 'top_left'
            p.legend.click_policy = "hide"
            self.mites = p
            p = self.add_exposure_label(p)
            html = file_html(p, CDN, "mites_plot")
            return html


    def mortality_plot(self):
        source = ColumnDataSource(self.data)
        p = figure(plot_width=1000, plot_height=400, x_axis_type="datetime",
                   title="Click legend entries to show/hide",
                   toolbar_location="above")
        y_max = math.ceil((self.data['out_dead_worker_adults'].append(self.data['out_dead_worker_larvae']).append(
            self.data['out_dead_foragers']).append(self.data['out_dead_drone_adults']).append(self.data['out_dead_drone_larvae'])
                           .max() + .01) / 2000) * 2000  # round max up to nearest 2k
        p.yaxis.axis_label = '# of individuals'
        p.y_range = Range1d(start=0, end=y_max, bounds='auto')
        r_wadultmort = p.line(x='out_date', y='out_dead_worker_adults', source=source, color='navy', alpha=0.5,
                             line_width=6, legend='Worker adult mortality', line_join='round')
        r_wlarvaemort = p.line(x='out_date', y='out_dead_worker_larvae', source=source, color='olive', alpha=0.5,
                               line_width=6, legend='Worker larvae mortality', line_dash='solid', line_join='round')
        r_foragermort = p.line(x='out_date', y='out_dead_foragers', source=source, color='darkred', alpha=0.5,
                                line_width=6, legend='Forager mortality', line_join='round')
        r_dadultmort = p.line(x='out_date', y='out_dead_drone_adults', source=source, color='slategray', alpha=0.5,
                              line_width=6, legend='Drone adult mortality', line_dash='solid', line_join='round')
        r_dlarvaemort = p.line(x='out_date', y='out_dead_drone_larvae', source=source, color='lightgray', alpha=0.5,
                              line_width=6, legend='Drone larvae mortality', line_dash='solid', line_join='round')
        p.legend.location = 'top_left'
        p.legend.click_policy = "hide"
        self.mites = p
        p = self.add_exposure_label(p)
        html = file_html(p, CDN, "mortality_plot")
        return html


    def add_exposure_label(self, plot):
       if self.model_obj.enable_pesticides == "true":
          if self.model_obj.application_type == application_type_CHOICES[0][0]: #"Foliar spray"
             start_date = pd.to_datetime("/".join([str(self.model_obj.FoliarForageBegin_month), str(self.model_obj.FoliarForageBegin_day),
                                                   str(self.model_obj.FoliarForageBegin_year)]),
                                         format="%m/%d/%Y")
             end_date = pd.to_datetime("/".join([str(self.model_obj.FoliarForageEnd_month), str(self.model_obj.FoliarForageEnd_day),
                                                 str(self.model_obj.FoliarForageEnd_year)]),
                                         format="%m/%d/%Y")
             plot.add_layout(BoxAnnotation(left=start_date,right=end_date))

          if self.model_obj.application_type == application_type_CHOICES[1][0]: #"Soil"
             start_date = pd.to_datetime("/".join([str(self.model_obj.SoilForageBegin_month), str(self.model_obj.SoilForageBegin_day),
                                                   str(self.model_obj.SoilForageBegin_year)]),
                                         format="%m/%d/%Y")
             end_date = pd.to_datetime("/".join([str(self.model_obj.SoilForageEnd_month), str(self.model_obj.SoilForageEnd_day),
                                                 str(self.model_obj.SoilForageEnd_year)]),
                                         format="%m/%d/%Y")
             plot.add_layout(BoxAnnotation(left=start_date,right=end_date))

          if self.model_obj.application_type == application_type_CHOICES[2][0]: #"Seed treatment"
             start_date = pd.to_datetime(
                "/".join([str(self.model_obj.SeedForageBegin_month), str(self.model_obj.SeedForageBegin_day),
                          str(self.model_obj.SeedForageBegin_year)]),
                format="%m/%d/%Y")
             end_date = pd.to_datetime(
                "/".join([str(self.model_obj.SeedForageEnd_month), str(self.model_obj.SeedForageEnd_day),
                          str(self.model_obj.SeedForageEnd_year)]),
                format="%m/%d/%Y")
             plot.add_layout(BoxAnnotation(left=start_date, right=end_date))

       return plot





