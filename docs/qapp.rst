ubertool Quality Assurance Project Plan
######################################

Project Management
**************************************

Title and Approval Sheet
======================================

Title of QA Project Plan
------------------------------------

Revision number of QA Project Plan
------------------------------------
1.0

Effective Data of QA Project Plan
------------------------------------
December 1, 2015

Names of all organizations involved in the modeling project
-------------------------------------------------------------
U.S. Environmental Protection Agency
Office of Research and Development
National Exposure Research Laboratory (NERL)
Ecosystems Research Division (ERD)
Athens, Georgia 30605 USA

U.S. Environmental Protection Agency
Office of Pesticide Programs
Ecological Fate and Effects Division (EFED)
Arlington, Virginia XXXXX USA

Names of all key project officials, with space for dated signatures
---------------------------------------------------------------------

Table of Contents and Document Control Format
==================================================

Distribution List (A3)
==================================================
List of all individuals (and their role on the project) who will be provided copies of the approved QA Project
Plan, including all persons responsible for implementation, including project managers, QA Managers, and
representatives of all groups involved.
Bill Eckel
Nelson Thurman
John Johnston
QA Manager

Project/Task Organization (A4)
==================================================
The übertool is a web application implementation of ecological risk models used by the EPA in pesticide registration
under FIFRA and for the assessment of pesticide risks to endangered species. Modern software development methods
are used to develop the web application, proceeding according to the principles of “scrum” development, an iterative
and incremental agile software development process for developing software applications (Lacey 2012). This approach
is centered around deploying applications in short time increments and getting rapid feedback from end users.  Both
of these occur at the end of each defined sprint period (4-6 weeks) in length. This deployment and feedback approach
is paired with modern industry standard approaches from XP programming and agile development.  XP programming
approaches include test-driven development, pair programming, collective code ownership, sustainable development
pace, coding standards, continuous integration, and code refactoring. Agile development processes include approaches
for

Scrum meetings are weekly on the same day every week (currently Thursday) at 3pm with monthly sprints replacing the
scrum meeting the first Thursday of every month.

Daily checkins are likely to be conducted on Google Hangout at 3pm for approximately 15 minutes.

Monthly ubertool progress reports are also scheduled with EFED via conference call.

There are three core roles involved in this process, these roles are:
- Product Owner: represents the stakeholders via stories backlog and priorities (Tom Purucker)
- Development Team: delivers product increments at the end of each sprint (ORISE fellowships working at the Athens
lab and others identified by Bill Eckel of OPP/EFED)
- Scrum Master: scrum facilitator who removes impediments for delivering sprint goals/deliverables, performs tasking,
 bug priority, task followup, etc. (contracted)

Ancillary roles on the scrum team are:
- Stakeholders: (Bill Eckel, Ed Odenkirchen, Dirk Young, Nelson Thurman, Ron Parker, Katrina White, others
identified by Bill Eckel)
- Managers: People who control the environment (John Johnston [Branch Chief], Roy Sidle [Division Director],
John Kenneke [CSS Matrix Interface], Tina Bohardi [CSS], Jim Cowles [Associate Director at EFED])

Modern software development methods are used to develop the web application, proceeding according to the principles
of “scrum” development, an iterative and incremental agile software development process for developing software
applications (Lacey 2012). This approach is centered around deploying applications in short time increments and
getting rapid feedback from end users.  Both of these occur at the end of each defined sprint period (2-6 weeks)
in length. This deployment and feedback approach is paired with modern industry standard approaches from XP
programming and agile development.  XP programming approaches include test-driven development, pair programming,
collective code ownership, sustainable development pace, coding standards, continuous integration, and code
refactoring. Agile development processes include approaches for

Scrum meetings are weekly on the same day every week at 3pm with monthly sprints replacing the scrum meeting the
first Thursday of every month.  Daily checkins are likely to be conducted in Athens and via phone at 3pm EST for
approximately 15-30 minutes. Monthly ubertool progress reports are also scheduled with EFED via conference call.

There are three core roles involved in this process, these roles are:
* Product Owner: represents the stakeholders via stories backlog and priorities (Tom Purucker)
* Development Team: delivers product increments at the end of each sprint (EPA employees, ORISE fellows, and SSA
contractors working with ORD and EFED)
* Scrum Master: scrum facilitator who removes impediments for delivering sprint goals/deliverables, performs
tasking, bug priority, task followup, etc. (contracted)


EFED Stakeholders:

* Bill Eckel
* Meridith Fry
* Andrew Kanarek
* Ed Odenkirchen
* Michelle Thawley
* Nelson Thurman
* Dirk Young
* others identified by Bill Eckel

EPA Managers:

* Gerald [CED Division Director]
* Tina Bohardi [CSS NPD]
* Jim Cowles [Associate Director at EFED]
* John Kenneke [CSS Matrix Interface]
* Matt Etterson [CSS Ecological Modeling Project Lead]
* John Johnston [WEB Branch Chief]

Problem Definition/Background (A5)
==================================================
Safety evaluations for pesticides are required for ecological and human health risks under a number of regulatory
statutes (e.g., Federal Insecticide, Fungicide, and Rodenticide Act (FIFRA), Pesticide Registration improvement
Extension Act (PRIA 3), Federal food, Drug, and Cosmetic Act (FD&C Act), Food Quality Protection Act (FQPA),
Endangered Species Act (ESA)). Ecological risk assessments under FIRFA and ESA are often implemented by the
Ecological Fate and Effects Division with OCSPP by accessing model tools and databases that have been developed
since the early 1980s on a range of software development platforms. These tools include Microsoft Excel
Spreadsheets, Windows-based interfaces, legacy Fortran code compiled as DOS executables, as well as programs
originally written in other programming languages (e.g., C, Perl, R). These models are parameterized with available
information from a number of different source data sets that also may vary in format. The results are documented
as risk assessment and management decisions for conventional active ingredients used in pesticide formulations.
The National Pesticide Program manages 1100 active ingredients and 19000 products that must be reevaluated on a
regular basis. The program also evaluates new pesticide formulations, ingredients, and novel uses of approved
active ingredients. The result of this process is that there are a large number of models to be run for many
chemicals with many possible adverse outcomes that must be summarized and reported. The current system of
distributed models and databases result in inefficiencies when conducting assessment and prevents transparency
regarding the evaluation process for regulatory risk evaluation.

Goals and objectives of this project that will address this problem
---------------------------------------------------------------------
The objective of this effort is to implement appropriate technologies and update the source code base for the übertool,
a web application system that executes algorithms for pesticide registration and endangered species effects assessments,
so that it can be deployed in scalable computational environments that provide front end access to cloud-executed
models and database backbone capabilities for querying and storing parameter inputs/outputs. This system is to be
deployed internally within the EPA for government users and externally on a public-facing server for use by the
public, academia, and the regulated community. The intent of this implementation is to accomplish EPA goals
concerning transparency of the data analyses and scientific algorithm estimation components of the pesticide
registration process. The project vision is an Agency collaboration platform that serves as an integrated scientific
workflow application to implement relevant assessment methods, respond to changing empirical data availability
(e.g., required toxicity tests, bioassays) and incorporate current fate, exposure, and effect algorithms in a model
selection framework. Unlike the time-inefficient and outdated collection of legacy science components, this scientific
modeling platform will replace critical regulatory data analysis and modeling processes with a more efficient, 21st
century system at a reasonable cost.

Efficiently conduct environmental assessments for pesticide registration and endangered species effects assessments
for models that currently are deployed in a number of different ways (Fortran DOS executables, Windows programs,
Excel spreadsheets) using data from a number of different data sources.

Definition of the population the problem targets and what measures within this population the problem addresses
---------------------------------------------------------------------
EFED risk assessors are the target audience for the ecological models. Main contacts include Bill Eckel,
Ed Odenkirchen, and Tom Steeger. Three divisions within OPP will use the human health version of the product-
HED, AD, and RD. Contacts include Vickie Dellarco, Jennifer McClain, Matt Lloyd, and Dana Vogel from the initial
meeting.

The ecological and human health divisions of OPP already share implementation of some of the models.
There may be instances where OPPT personnel used similar models as the OPP human health risk assessment divisions
and may use some of the models a la carte.  Members of the public, academia, and the registrants may use the product
via a public facing web page in the future.

As python code, it can be run on a computer locally using a web browser as an interface (without being on the Internet,
which will be necessary for the EPA to use it for applications involving confidential business information) and/or it
can be hosted on the Internet as a web domain so that the public can access the public domain models that are used to
determine pesticide registration and label restrictions (available at http://www.ubertool.org).  Component libraries
for the ubertool can be accessed individually in non-HTML applications.  Alternatively, the code could be hosted on an
EPA server with the requisite technologies to provide online access to the python code.  Regardless of how it is
accessed, some of the models (these are mostly older Fortran codes in the public domain, not web applications) are
of interest to the EPA pesticide office and could potentially realize significant efficiencies in regulating
pesticides, transparency for the ecological risk assessment process, and higher levels of quality assurance given
the larger audience that might use the models--whether for chemical regulation or for educational purposes.

Pesticide evaluations are required for ecological and human health risks under a number of regulatory statutes (e.g.,
Federal Insecticide, Fungicide, and Rodenticide Act (FIFRA), Pesticide Registration improvement Extension Act
(PRIA 3), Federal Food, Drug, and Cosmetic Act (FD&C Act), Food Quality Protection Act (FQPA), Endangered Species
Act (ESA)). Ecological risk assessments under FIRFA and ESA are often implemented by the Ecological Fate and
Effects Division within the Office of Chemical Safety and Pollution Prevention by accessing model tools and
databases that have been in continual development since the early 1980s on a range of software development platforms.
These tools include Microsoft Excel Spreadsheets, Windows-based interfaces, legacy Fortran code compiled as DOS
executables, as well as programs originally written in other programming languages (e.g., C, Perl, R). These models
are parameterized with available information from a number of different source data sets that also may vary in format.
The results are documented as risk assessment and management decisions for conventional active ingredients used in
pesticide formulations. The National Pesticide Program manages 1100 active ingredients and 19000 products that must
be reevaluated on a regular basis. The program also evaluates new pesticide formulations, ingredients, and novel uses
of approved active ingredients. The result of this process is a large number of models to be run for many chemicals
with many possible adverse outcomes that must be summarized and reported. The current system of distributed models
and databases result in inefficiencies when conducting assessment and prevents transparency regarding the evaluation
process for regulatory risk evaluation.

The decision to register a pesticide is based on the consideration of scientific data and other factors showing that
it will not cause unreasonable risks to human health, workers, or the environment when used as directed on product
labeling. The registration review program is intended to ensure that, as the ability to assess risk evolves and as
policies and practices change, all registered pesticides continue to meet the statutory standard of no unreasonable
adverse effects to human health and the environment. Changes in science, public policy, and pesticide use practices
occur over time. Through the registration review program, EPA periodically reevaluates pesticides to ensure that as
change occurs, products in the marketplace can be used safely. As part of the registration review process, EFED
assesses risks of pesticides to Federally-listed threatened and/or endangered (listed) species from registered uses
of pesticides.  These assessments are conducted in accordance with provisions of the Endangered Species Act (ESA),
and the Services’ Endangered Species Consultation Handbook (NMFS). The models used are periodically updated in
view of new pesticides, changing science, and as novel exposure pathways come to light.

Reason the project includes a modeling approach to address the problem (is it a new predictive tool?)
---------------------------------------------------------------------
EPA is responsible for registering pesticides under FIFRA; as part of the registration process, the EPA’s Ecological
Fate and Effects Division of the Office of Chemical Safety and Pollution is responsible for analyzing data and
developing/ implementing ecological models that estimate risks to non-target receptors. The Food Quality Protection
Act of 1996 mandated the Environmental Protection Agency (EPA) to implement a new program for assessing the risks of
pesticides, registration review. The decision to register a pesticide is based on the consideration of scientific data
and other factors showing that it will not cause unreasonable risks to human health, workers, or the environment when
used as directed on product labeling. The registration review program is intended to ensure that, as the ability to
assess risk evolves and as policies and practices change, all registered pesticides continue to meet the statutory
standard of no unreasonable adverse effects to human health and the environment. Changes in science, public policy,
and pesticide use practices will occur over time. Through the new registration review program, EPA periodically
reevaluates pesticides to ensure that as change occurs, products in the marketplace can be used safely. As part
of the registration review process, EFED is assessing risks of pesticides to Federally-listed threatened and/or
endangered (listed) species from registered uses of pesticides.  These assessments are conducted in accordance
with the Overview Document[1], provisions of the Endangered Species Act (ESA), and the Services’ Endangered
Species Consultation Handbook (NMFS 1998). The models used are periodically updated in view of new pesticides,
changing science, and as novel exposure pathways come to light.

created an integrated web-based tool, the übertool, designed to estimate exposure doses and ecological risks
under the Federal Insecticide, Fungicide, and Rodenticide Act (FIFRA) and the Endangered Species Act (ESA).
This involved combining a number of individual software models into web applications so they can be more
easily parameterized, run, and documented by the EPA regulatory program office as well as federal,
industry, and academic researchers outside the agency. These models include a range of aquatic, terrestrial,
and atmospheric deposition fate and transport models used to estimate pesticide exposures and effects for a wide
range of ecological receptors. Risk assessments based on these models are evaluated when seeking approval for
pesticide formulations by the Environmental Protection Agency (EPA). Übertool integration of the ecological
risk models creates a unified environment where data inputs and outputs are shared amongst models and saved
for each user. This web-based approach takes advantage of new technologies including on-demand cloud computation
of models written in a variety of programming languages (e.g., Python, Fortran, C) as well as spreadsheet calculators
(e.g., Microsoft Excel) to support complex and screening level models. The übertool can also batch run multiple
models simultaneously given the appropriate inputs providing an efficient and previously unavailable ecological
risk service.

Übertool’s web-based framework has also extended to population dynamic models not currently used by FIFRA and
ESA that are publicly available for educational and research purposes. Traditionally, ecological assessment
of pesticides is based on the ratio between estimated environmental concentrations and extrapolated toxicity
effects levels that can be difficult to relate to ecological endpoints that are actually valued and regulated
(e.g., populations).  By aggregating these models into a virtual dashboard, we enable linkages to be created
in the gap between the traditional ecological hazard assessment of screening models (risk quotients) and
assessing ecological endpoints at the population level. Closing this gap has been identified in a recent
National Academy of Science’s report as being necessary to create a common, scientifically credible approach
to resolve discrepancies between how FIFRA and the ESA manage ecological risks. The new framework (Untertool)
incorporates a variety of models including basic models of population dynamics (e.g. logistic model), intra-colony
honey bee population dynamic models, and links to other online models and resources.

Types of decisions that may be made as a result of this project
---------------------------------------------------------------------
The EPA is dependent on multiple scientific computational models for the environmental regulatory process of chemicals
and laws that codify ecological and human health protection standards. Laws include the Federal Insecticide, Fungicide,
and Rodenticide Act (FIFRA), Endangered Species Act (ESA), Toxic Substances Control Act (TSCA) and the Federal Food,
Drug and Cosmetic Act (FFDCA). More often than not, the effective basis of such standards are decisions about the
selection and application of data and computational models. Over time, the relevant laws, data and computational
models have evolved due to increased complexity of EPA regulations and scenario-dependent implementations. This
complexity leaves a legacy of computational models, still relevant to the regulatory process, varied with incompatible
computer languages and software that are not easily integrated or updated as the science evolves. These limitations
are addressed by integrating EPA’s existing and developing regulatory models into a unified science application
platform known as the ubertool.

Any other types of problems that the project may address
---------------------------------------------------------------------

Background information on the problem
---------------------------------------------------------------------
 EPA (2004) provides an overview of OPP’s ecological risk assessment process:
www.epa.gov/espp/consultation/ecorisk-overview.pdf

Reasons the project is important, how it supports other existing research, programs, or regulations
---------------------------------------------------------------------

Conflicts or uncertainties that will be resolved by this project
---------------------------------------------------------------------

Reasons one model is determined to be better than another for this application
---------------------------------------------------------------------
The program office uses them, after a review process...

Project/Task Description and Schedule (A6)
==================================================

Summary of all work to be performed, products to be produced, and the schedule for implementation
---------------------------------------------------------------------
To create an aggregate ubertool assessment, a user will have created the above data objects for each of the
tables above, and will combine them to create a batched assessment.  A tree with dropdown comboboxes that reflect
available data objects saved to the user account will be presented to the user.  By selecting an appropriate data
object for each of the 8 data node objects on the tree, the user can then execute the aggregate ubertool to run the
included models.  At this point, there will be no option to deselect a constituent model in the aggregate ubertool.
We need a figure of a mock-up of the ubertool aggregate data tree.

An additional priority is development of the spatial overlay tool to compare endangered species ranges to crop and
pesticide application distributions.  This will develop will proceed separately from the aggregate ubertool initially.

A future priority is using the fate and transport models to create exposure concentrations data objects that are used
by a number of the ecological models.

List of products, deliverables, and milestones to be completed in the various stages of the project
---------------------------------------------------------------------
The ubertool is developed in an iterative development environment, so that new releases of the web application are
distributed every 3 weeks at the conclusion of each sprint.

Schedule of anticipated start and completion dates for the milestones and deliverables, and persons responsible for each
---------------------------------------------------------------------

Quality Objectives and Criteria for Model Inputs/Outputs (A7)
====================================================================

Project data quality objectives (DQOs), performance criteria, and acceptance criteria
---------------------------------------------------------------------
All model components will be developed using an appropriate approach to quality assurance and documentation.

Description of task that needs to be addressed and the intended uses of the output of the modeling project to achieve the task
---------------------------------------------------------------------

Ecological Models
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
A number of models are used to estimate risk to non-target species in this process.  These models are listed in Table
1 and their current development status within the ubertool.

Table 1. Models in version 1 of the ubertool
+--------------+-------------+
|Model         | Purpose     |
+==============+=============+
|TerrPlant     |             |
+--------------+-------------+
|Sip           |             |
+--------------+-------------+
|Stir          |             |
+--------------+-------------+
|T-Rex|        |             |
+--------------+-------------+
|T-Herps       |             |
+--------------+-------------+
|IEC	       |             |
+--------------+-------------+
|AgDrift       |             |
+--------------+-------------+
|AgDrift-TRex  |             |
+--------------+-------------+
|AgDrift-THerps|             |
+--------------+-------------+
|Earthworm     |             |
+--------------+-------------+
|Rice          |             |
+--------------+-------------+
|Kabam         |             |
+--------------+-------------+
|PFAM          |             |
+--------------+-------------+
|SAM           |             |
+--------------+-------------+

Table 2. Candidate models for the untertool
+----------+----------------+
|Model	   | Purpose        |
+==========+================+
|EXAMS	   |                |
+----------+----------------+
|PRZM	   |                |
+----------+----------------+
|Geneec	   |                |
+----------+----------------+
|VVWM      |                |
+----------+----------------+
|First	   |                |
+----------+----------------+
|DUST	   |                |
+----------+----------------+
|TIM	   |                |
+----------+----------------+
|DDM	   |                |
+----------+----------------+
|PlantX	   |                |
+----------+----------------+
|Bee-Rex   |                |
+----------+----------------+
|SuperPRZM |                |
+----------+----------------+


Table 3. Population models
+----------------------------------+-------------+
|Model                             | Purpose     |
+==================================+=============+
|Exponential                       |             |
+----------------------------------+-------------+
|Logistic                          |             |
+----------------------------------+-------------+
|Gompertz                          |             |
+----------------------------------+-------------+
|Fox Surplus Yield                 |             |
+----------------------------------+-------------+
|Maximum Sustainable Yield         |             |
+----------------------------------+-------------+
|Yule-Furry Markov Process         |             |
+----------------------------------+-------------+
|Feller-Arley Markov Process       |             |
+----------------------------------+-------------+
|Leslie Projection Matrix          |             |
+----------------------------------+-------------+
|Leslie with Logistic Dose Response|             |
+----------------------------------+-------------+



Database Sources
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
It will be necessary to crosswalk the data that is available in the database sources with the listed data object tables. The crosswalk is available at http://tiny.cc/ubertool_crosswalk

Database backbone details (MongoDB, possibly Amazon-based via EC2) and mapping technologies (maybe Google maps plus postgis/postgresql) are still undecided.
http://www.mongodb.org/display/DOCS/Amazon+EC2
http://aws.amazon.com/rds/
https://developers.google.com/maps/documentation/webservices/
http://postgis.refractions.net/
http://www.postgresql.org/

Table 4. Available databases with parameters of interest

Database	Location	Description
Ecological Incident Information System	C:\Documents and Settings\All Users\programs\EIIS\EIISv2.1.mdb	Data on incidents of adverse field effects plants and wild animals. (Nick Mastrota)
Avian Incident Monitoring System	http://www.abcbirds.org/abcprograms/policy/pesticides/aims/aims/index.cfm	An American Bird Conservancy database of avian incidents. (Nick Mastrota)
Pesticide Ecotoxicity Database	G:\Science Databases\ Ecotoxicity\Toxdata\EcoToxData.mdb	Data of toxicity of pesticides to plants and animals from EPA-reviewed studies. (Brian Montague)
Pesticide Fate Database	http://cfpub.epa.gov/pfate/home.cfm	Environmental fate data from EPA-reviewed studies. (Larry Liu)
EFED Ingredients	N:\EFED_Applicaitions\databases\EFED Ingredients\EFED Ingredients.mdb	Data on pesticide ingredients reviewed by EFED. (Nick Mastrota)
LOCATES	C:\Documents and Settings\All Users\programs\LOCATES\LOCATES FE.mdb	Co-ocurrence of endangered species and crop locations. (Kurt Pluntke)
EFED library	G:\Information Resources\EFED Library\ EFED Library.mdb	Information on books and articles in the EFED library. (Nick Mastrota)
ChemFiles	N:\EFED_Applications\databases\ChemFiles\ChemFiles_FE.mdb	Tracking data on EFED’s chemical files. (Nick Mastrota)
Birds in Agricultural Areas	http://www.abcbirds.org/abcprograms/policy/pesticides/biaa/index.html	An American Bird Conservancy database of use of crops by birds. (Brian Montague)
STORET	http://www.epa.gov/storet	An EPA database of water quality data from U.S. surface and ground water monitoring. (Nelson Thurman)
LUIS


List of requirements associated with the hardware/software configuration for those studies involving software evaluation
-----------------------------------------------------------------------
Python uses web application frameworks that conform to a common standard called the Web Server Gateway Interface
(WSGI).  We currently use two frameworks, webapp2 and Django, that help automate the integration of the Python backend
and the web application frontend allowing for rapid development.

Web hosting services provide the cloud storage and host the web site containing the web applications.  These web
services are vital to the übertool in terms of accessibility and data processing.  The Python web application
frameworks work with the web hosting services to ultimately provide the deliverable to the end user.

The nature of web application development allows for the use of many cross-platform (i.e. Microsoft Windows, Apple
OSX, Redhat Linux, etc.) software programs.  Python itself is a cross-platform language designed to easily integrate
various programming languages.  The software development environment includes text editors such as Sublime Text,
Python IDEs such as Spyder, Python extensions such as NumPy, and web browsers such as Microsoft’s Internet Explorer,
Google’s Chrome, and Mozilla’s Firefox.

The source code for the übertool is version controlled using GitHub.  GitHub manages all changes to the source code,
allowing for simultaneous development from multiple developers on the same source code.  Each developer has his/her
own “branch” of the source code on which they work.  These branches are merged back into the “trunk” or master
branch of the source code as the software is updated.  Software can be rolled back as necessary as GitHub tracks
the history of the software development.

The übertool is requires database support for full functionality.  The database of choice is MongoDB as it is
cross-platform, flexible, and open source.


Special Training Requirements/Certification (A8)
====================================================================

Types of required training and certification needed by the project team
-----------------------------------------------------------------------

Plan for obtaining training and/or certification
-----------------------------------------------------------------------

Documentation of training and/or certification
-----------------------------------------------------------------------


Documentation and Records (A9)
======================================
Project progress will be documented annually in terms of the annual reports. In addition, conference presentations and
publications will be prepared as appropriate and archived in the EPA knowledge management systems (Google doc?,
github wiki?).

An updated version of the quality assurance plan will be developed annually and distributed by email. The date of the
latest update will be included in the plan. Records of yearly quality assurance audits performed by the QA manager
and QA officer are maintained by the QA manager. The auditor uses a checklist to mark which portions of the QAPP are
followed, and to document deviations or absence of any QA measures. The results of such audits shall be documented and
filed by the Quality Assurance Manager. The audit process itself shall be designed to objectively measure compliance
with written procedures and assess the effectiveness of the process. The evaluation shall include interviews with
development team members, and a review of research project work and quality records.

Before submission of a paper to an archival journal, the work will be reviewed for conformance with the applicable
quality assurance criteria. Program code and output will be maintained in electronic data files and backed up on
cloud platform (www.github.com). These documents will be maintained for a minimum of 5 years after the completion
of the project.

Description of information to be included in reports
-----------------------------------------------------------------------

Proper document control and distribution procedures
-----------------------------------------------------------------------

Details on document storage
-----------------------------------------------------------------------

Backup plan for records stored electronically
-----------------------------------------------------------------------

Description of the change control process (who approves changes, etc.)
-----------------------------------------------------------------------

Length of retention periods for each record
-----------------------------------------------------------------------

Data assessment reports, interim project progress reports
-----------------------------------------------------------------------

Model science formulation report, peer review reports
-----------------------------------------------------------------------

Model assessment reports, interim project progress reports
-----------------------------------------------------------------------

Code standards, code auditing and testing reports, interim project progress reports
-----------------------------------------------------------------------
 Potential collaboration/development tools include:
- kunagi (agile/scrum management system)
http://kunagi.org/
- chiliproject (bug and feature tracking for agile development and quality)
https://www.chiliproject.org/
- jenkins (continuous integration and testing server)
http://jenkins-ci.org/
- sonar (code quality/bug prevention)
http://www.sonarsource.org/
- teambox collaboration (ubertool project currently active)
http://teambox.com/
- Google hangout (requires a Google+ account)
http://www.google.com/+/learnmore/hangouts/

Some of these development tools may be accessible through ubertool subdomains in order to allow access from within the
EPA firewall.


Model calibration report
-----------------------------------------------------------------------

Model evaluation records (How well does the model report variability and uncertainty in its output?)
-----------------------------------------------------------------------

User’s manual
-----------------------------------------------------------------------

Configuration management (after production version) and code maintenance (e.g., or software internal documentation of logic and structure) manuals
-----------------------------------------------------------------------

Licensing Issues
-----------------------------------------------------------------------
There are still a lot of questions about the use of open source licenses by federal agencies. If the software is
developed solely by government employees, the questions are even more open.  A developer can release software under
an OSS because he or she has a copyright in the software, a property right that can be licensed.  A government work,
like employee-developed software, is not entitled to U.S. copyright protection.   NASA and others address this dilemma
with this argument: The software is still property (if not intellectual property) of the U.S. government.  Since the
U.S. government can choose not to release its property, it can also choose to release it only under the conditions of
a license.

GROUP B: Measurement and Data Acquisition
**************************************
This project is based entirely on modeling with existing publicly available mathematical and empirical
 models and therefore follows the Guidance for Quality Assurance Project Plans for Modeling
EPA QA/G-5m (USEPA, 2002). The project relies exclusively on secondary sources of data, also
referred to as non-direct measurements, for parameterization. Most of this information is submitted to the EPA from
registrants or publicly available with their own documented quality control
procedures. Some data utilized from public and private sources that may have less well
documented quality assurance procedures.

Sampling Process Design (B1)
======================================
This section pertains to the acquisition of primary data and is not applicable to this project.

Sampling Methods (B2)
======================================
This section pertains to the acquisition of primary data and is not applicable to this project.

Sampling Handling and Custody (B3)
======================================
This section pertains to the acquisition of primary data and is not applicable to this project.

Analytical Methods (B4)
======================================
This section pertains to the acquisition of primary data and is not applicable to this project.

Quality Control (B5)
======================================
This section pertains to the acquisition of primary data and is not applicable to this project.

Instrument/Equipment Testing, Inspection, and Maintenance (B6)
======================================
This section pertains to the acquisition of primary data and is not applicable to this project.

Calibration (B7)
======================================

Objectives of model calibration activities, including acceptance criteria
-----------------------------------------------------------------------

Frequency of model calibration activities
-----------------------------------------------------------------------

Details on the model calibration procedure
-----------------------------------------------------------------------

Method(s) of acquiring input data
-----------------------------------------------------------------------

Types of output generated by the model calibration
-----------------------------------------------------------------------

Approach to characterize uncertainty (e.g., sensitivity analysis)
-----------------------------------------------------------------------

Corrective action to be taken if criteria are not met
-----------------------------------------------------------------------

Resources and responsibilities for calibrating the model
-----------------------------------------------------------------------
In addition to input data, government publications and publically available scientific liberature will be
considered for the development of the model. For example, the Agency’s Wildlife Exposure Factors Handbook will be
considered for estimating the dose to birds, mammals, terrestrial phase amphibians, reptiles, and terrestrial insects
via ingestion of water by determining the appropriate allometric equations for each taxa’s drinking water intake.

Analysis of model output relative to acceptance criteria
-----------------------------------------------------------------------

Non-direct Measurements (Data Acquisition Requirements) (B9)
======================================
The project will use secondary (non-direct) data from many sources and may generate large volumes of
modeled data during implementation. Some parameters are accepted as inputs from users who access the web application.
Other data sources undergo quality assurance analysis per their own project objectives. It is anticipated that all
secondary data will be acquired in electronic format. Acquisition of data will be documented in
electronic repositories.

Types of data needed for implementing a project that are obtained from non-measurement sources such as databases, literature files
-----------------------------------------------------------------------

Need for non-direct measurements, intended use of data
-----------------------------------------------------------------------

Method(s) of identifying and acquiring data
-----------------------------------------------------------------------

Method of determining the underlying quality of the data
-----------------------------------------------------------------------

SOPs and field or lab-specific deviations associated with these procedures
-----------------------------------------------------------------------

Acceptance criteria for non-direct measurements: such as completeness, representativeness, bias, precision, qualifying data
-----------------------------------------------------------------------

Data Management and Hardware/Software Configuration (B10)
======================================
This project will will acquire data from secondary sources, manipulate
secondary data to meet use requirements, generate data from model output, and create summary and
processed files for further statistical and analytical treatment. It is anticipated that the project will acquire
or generate little or no hardcopy data. The project will maintain a data management system that protects
integrity of the data received and generated throughout the project. This includes file management
systems, version control, archiving procedures, and quality assurance activities.

The project team will conduct all work and store all electronic files on a common ORD server at the
ERD/NERL Athens facility on the L drive. This server is backed up weekly
and maintained by EPA’s ITI contractors under the supervision of OSIM.

Information on the project data management process (field, office, and lab)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Record-keeping procedures, document control system, audit trails
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Control mechanism for detecting and correcting errors, preventing loss of data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Procedures for assuring applicable Agency resource management requirements are satisfied
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Required computer hardware/software and any specific performance requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Data Management (Element B10a)
-----------------------------------------------------------------------

Any data forms, checklists, on-line interactive screens used in the modeling process
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Any graphics developed to document the data management process (process flow diagrams, modeling flow charts, etc.)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Documentation of internal checks used during data entry
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Data calculations and analyses that should to be highlighted in the QA Project Plan
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Plans for characterization of uncertainty and variability in the model results (e.g., summary statistics, frequency distributions, goodness-of-fit tests)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Hardware/software Configuration (Element B10b)
-----------------------------------------------------------------------

List of equipment, hardware, and software that will be used on the project
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Description of performance requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Decisions regarding security issues
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Decision regarding communication issues
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Decisions regarding software installation issues
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Decisions regarding response time issues
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Plans for requirements documentation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Coding standards
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Testing plans
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Plans for data dictionary (may not need to be a separate document)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Plans for a user’s manual
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Plans for a maintenance manual (explaining software logic and organization)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Plans for source code for the ultimate user of the model or model framework
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Configuration management plan (procedures to control software/hardware configuration during development of the original model version)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


GROUP C: Assessment and Oversight
**************************************


Assessment and Response Actions (C1)
======================================
The EPA Quality Assurance Manager will conduct a Technical Systems Audit (TSA) to ensure that this QAPP is being
followed during the execution of the research project. The research team is responsible for documenting the response
to any significant findings. Work conducted for this project will undergo ongoing technical review by personnel at
EPA/ORD/NERL/ERD who are implementing the project.

The project team leader will have responsibility for monitoring project activities and identifying or confirming any
quality problems. Any problems will be brought to the attention of the ORD Management Team and the ORD QA Team, who
will initiate corrective actions, document the nature of the problem, and ensure that the recommended corrective
action is carried out.

This QAPP describes processes for model sensitivity and uncertainty analysis (Section B7), data quality assessment
(Section B9), data management and error checking (Section B9) and model performance evaluations (section B7).
The project team will assess model sensitivity to parameters in calibration steps as well as in analysis steps
to understand model performance specific to modeling objectives. It has provisions for data validation and usability
(Section D)

Many of the technical problems that might occur can be solved on the spot by the technical staff, for example, by
modifying the technical approach or correcting errors or deficiencies in documentation. Immediate corrective
actions form part of normal operating procedures and are noted in records for the project. Problems that cannot be
solved in this way require more formalized, long-term corrective action. If quality problems that require attention
are identified, the QA Officers will determine whether attaining acceptable quality requires either short- or
long-term actions.

The Project Team Leader will perform surveillance activities to ensure that management and technical aspects are
being properly implemented according to the schedule and quality requirements specified in this QAPP. These
surveillance activities will include assessing how project milestones are achieved and documented, corrective
actions are implemented, budgets are adhered to, reviews are performed, and data are managed.

The technical systems assessment will include assessment of data collection activities, documentation, quality
checks, record management, and reporting.

Assessments of internal code validity and consistency of model structure will be ongoing. The first assessment will
occur when the model is initially structured and will emphasize internal code validation. At this point numerical
comparisons will be executed between model outputs and verified EPA reports. Any discrepancies will trigger an
in-depth review of the code. Intermediate computations will be compared against simple analytical cases in order
to localize the source of the error in the code. This will be conducted iteratively until the errors are found.
Discrepancies will be addressed through consideration of alternative scenarios and parameter values and adjustments
to model structure as indicated by the feedback. Revisions will be performed either by Tom Purucker or by a team
member under the close supervision of Tom Purucker. Documentation of QA procedures will occur when a draft paper is
being vetted for submission to an archival journal. If necessary based on the QA review, changes will be made to the
paper proposed for publication.

Assessment/oversight strategies and schedule of assessment activities, order of events
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Organizations and individuals expected to participate in assessments, including peer reviews
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Information expected, success criteria
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Scope of authority of assessors to recommend or direct changes to the model (corrective actions)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Qualitative and quantitative assessments
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Internal assessments (internal QA officer’s review of input data, code verification, calibration, benchmarking) and external assessments (peer review of model theory or mathematical structure)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Surveillance activities (continued monitoring of status and progress of the project, tracking project milestones and budgets)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Plans for model performance evaluations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Plans for sensitivity analysis
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Plans for uncertainty analysis
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Plans for data quality assessment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Plans for code testing
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Hardware/Software Assessments
-----------------------------------------------------------------------

Plans for hardware and software configuration testing, if appropriate
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Plans for code verification tests
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Plans for internal and external peer reviews
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Plans for checking for programming errors
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Plans for checking for correct insertion of model equations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Plans for checking for code’s linkage to analysis of uncertainty
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Hardware/Software Configuration Tests
-----------------------------------------------------------------------

Plans for software code development inspections
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Plans for software code performance testing
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Plans for a test of the model framework
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Plans for integration tests (check computational and transfer interfaces between modules)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Plans for regression tests
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Plans for stress testing of complex models (to ensure that maximum load during peak usage does not exceed limits of the system)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Plans for acceptance testing (contractually-required testing needed before a new model or model application is accepted by the customer and final payment is made)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Plans for beta testing of pre-release hardware/software, recording of anomalies
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Plans for checking for programming errors
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Plans for science and product peer review
-----------------------------------------------------------------------


Theoretical basis for the model
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Mathematical model structure
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Model algorithms
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Model predictions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Model calibration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Plans for data quality assessment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Plans for peer review of final technical product
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Reports to Management (C2)
======================================


Project reporting schedule
-----------------------------------------------------------------------
This QAPP will be distributed to the ubertool project team and stored on the G-drive in the ubertool folder. The
model, user guidance, and technical documentation will be stored on the XXX drive XXXX folder. The model and
technical documentation will also be made available on the ubertool web page. Backup copies of all the development
documentation will be kept by the project lead.

Periodic updates/progress reports will be given to ORD management, the XXXX and end users as needed to discuss the
progress of the project. A written QC, technical assessments, and documentation will be made available to interested
parties. Management will be kept informed of the project’s progress through the managerial advisor and/or periodic
briefings.

Any identified errors, deficiencies, and anomalies will be documented and reported to the team. If needed, an error
analysis will be performed and the model processes will be reviewed and/or modified.

Frequency, content, and distribution of reports
-----------------------------------------------------------------------

Deviations from approved QA Project Plan
-----------------------------------------------------------------------

Need for response actions to correct deviations
-----------------------------------------------------------------------

Potential uncertainties in decisions based on input data and model limitations
-----------------------------------------------------------------------

Data Quality Assessment findings
-----------------------------------------------------------------------


GROUP D: Data Validation and Usability
**************************************
This project uses well-known ecological assessment models to estimate risk that have a history of extensive use by
public agencies and universities and
documentation in peer-reviewed literature. The modeling requires input data that must be acquired
from federal, state, and local authorities, as well as private entities. The quality of data used for and
generated during modeling will be reviewed and verified at multiple levels by project technical staff and
QA officers, as described in detail in other sections.

Departures from Validation Criteria (D1)
======================================


To evaluate the correctness of programmed models, a quality control/quality assurance (QA/QC) page is created, which
validates models’ inputs and outputs towards given sample calculations. The sources of sample calculations come from
verified EPA reports. Any discrepancies will trigger an in-depth review of the code. Intermediate computations will
be compared against simple analytical cases in order to localize the source of the error in the code. Discrepancies
will be addressed through consideration of alternative scenarios and parameter values and adjustments to model
structure as indicated by the feedback.

Criteria used to review and validate (accept, reject, or qualify) model components such as theory, mathematical procedures, code, and calibration (convergence criteria, etc.)
-----------------------------------------------------------------------
Model-dependent.

Criteria used to review and validate input data
-----------------------------------------------------------------------
Input data will be obtained from verified EPA reports, which legitimizes the sources. Thus data review, verification,
and validation will focus on the consistency of the input data used for calculations and modeling. As a result, an
input table (Figure below) is present on the QA/QC page, including values used in the computation. Numerical
comparisons between QA/QC input table and verified EPA reports will be executed. Any deviations will raise the
check of the code and will be documented in writing and reviewed by the ORD Management team and the ORD Quality team.

Data review, verification, and validation will focus on acceptability of the input data used for calculations
and modeling. All original and modified data files will be reviewed for input, handling, and calculation
errors. Any issues identified through this review process will be evaluated and, if necessary, data will be
corrected and analysis carried out using corrected data.

Deviations from the approved QAPP could occur as the project proceeds. The need for adjustments may
arise based on data validation and quality assurance checks, outcomes of model initialization and
calibration steps, scenario development, and so on. Deviations will be documented in writing and
reviewed by the ORD Management Team and the ORD Quality Team. The QAPP will be revised
accordingly and recirculated for Quality Assurance review and approval.

Figure #. User input table from the QA/QC page

To evaluate the correctness of programmed models, a quality control/quality assurance (QA/QC) page is created, which
validates models’ inputs and outputs towards given sample calculations. The sources of sample calculations come
from verified EPA reports. Any discrepancies will trigger an in-depth review of the code. Intermediate computations
will be compared against simple analytical cases in order to localize the source of the error in the code.
Discrepancies will be addressed through consideration of alternative scenarios and parameter values and adjustments
to model structure as indicated by the feedback.

Input data will be obtained from verified EPA reports, which legitimizes the sources. Thus data review, verification,
and validation will focus on the consistency of the input data used for calculations and modeling. As a result, an
input table (Figure below) is present on the QA/QC page, including values used in the computation. Numerical
comparisons between QA/QC input table and verified EPA reports will be executed. Any deviations will raise the
check of the code and will be documented in writing and reviewed by the ORD Management team and the ORD Quality team

Criteria used to test model performance
-----------------------------------------------------------------------
Model performance is checked through the ‘Batch’ mode, which sequentially calculates scenarios provided in the
template. Two testing criterion are considered here: 1. repeat the same scenarios in the template (e.g. 10 times),
and check the consistency of model inputs and outputs among 10 scenarios; 2. list a large number of scenarios
(e.g. 10,000) and estimate the time consumed during the computation.

Criteria used to review or validate model outputs
-----------------------------------------------------------------------
The integrity of model output data will be verified and validated by project technical staff. Reviews may
include a thorough evaluation of content and/or a “spot-check” of calculated between output tables
(Figure below) in the QA/QC page and verified EPA reports. Should a review identify an aberration, the reviewer
will notify those responsible for taking corrective actions. The QA officers will be notified if corrective action
is potentially required. Evaluation of whether model components and their outputs are correct will be an ongoing process
for QA personnel during the model calibration and validation stage of the project.
In-progress assessments of validation issues will be discussed between a team including both technical and
QA representatives from EPA. The results of performing evaluations will be logged and integrated into the project
documentation at the conclusion of the project, as well any corrective actions that were implemented.

Evaluation of whether model components and their outputs are satisfying the project objectives will be an ongoing
process for QA personnel during model calibration and validation stages of the project. In-progress
assessments of validation issues will be discussed by a team including technical and QA representatives
from EPA.

 Figure #. Output tables from the QA/QC page

Validation Methods (D2)
======================================

Methods for review of model components such as theory, mathematical procedures, code, and calibration (peer review, etc.)
-----------------------------------------------------------------------

Methods for review of input data
-----------------------------------------------------------------------

Methods for review of model performance tests
-----------------------------------------------------------------------

Methods for assessment of model output and usability
-----------------------------------------------------------------------

Reconciliation with User Requirements (D3)
======================================
The objective of the project is to assess..

Discussion of project or task results
-----------------------------------------------------------------------

List of departures from assumptions set in the planning phase of the model
-----------------------------------------------------------------------

Report on limitations on use of output data for decision makers or users
-----------------------------------------------------------------------


REFERENCES
**************************************
Apandi, T., 2009 Extreme Programming Pocket Guide. O’Reilly Media, Sebastopol, CA.

Helms, J.C., 2013. Web-Based Application Quality Assurance Testing. Accessed at
http://ils.indiana.edu/faculty/hrosenba/www/S512/pdf/helm_web-qa.pdf on 9/5/2013.

USEPA, 2002. Guidance for Quality Assurance Project Plans for Modeling. EPA QA/G-5M.

USEPA. 2004. Overview of the Ecological Risk Assessment Process in the Office of Pesticide Programs. U.S.
Environmental Protection Agency, Office of Prevention, Pesticides and Toxic Substances, Office of Pesticide Programs,
Washington DC. 100 pp. January 23, 2004.

USFWS and National Marine Fisheries Service (NMFS). 1998. Endangered Species Consultation Handbook:
Procedures for Conducting Consultation and Conference Activities Under Section 7 of the Endangered Species Act.
Final Draft. March 1998.
