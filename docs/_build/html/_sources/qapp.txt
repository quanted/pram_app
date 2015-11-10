ubertool Quality Assurance Project Plan
------------------------------

Project Management
+++++++++++++++++++++++++++++++++++++++++++++++++++++++

Revision number of QA Project Plan
######################################
1.0

Effective Data of QA Project Plan
#########################################
October 1, 2014

Names of all organizations involved in the modeling project
#########################################################
U.S. Environmental Protection Agency
Office of Research and Development
National Exposure Research Laboratory (NERL)
Ecosystems Research Division (ERD)
Athens, Georgia 30605 USA

U.S. Environmental Protection Agency
Office of Pesticide Programs
Ecological Fate and Effects Division (EFED)
Arlington, Virginia XXXXX USA

Names of all key project officials, with space for dataed signatures
#################################################


Project/Task Organization
++++++++++++++++++++++++++++++++++++++++++++++

Objective and Product Vision
##########################
The objective of this effort is to implement appropriate technologies and update the source code base for the übertool, a web application system that executes algorithms for pesticide registration and endangered species effects assessments, so that it can be deployed in scalable computational environments that provide front end access to cloud-executed models and database backbone capabilities for querying and storing parameter inputs/outputs. This system is to be deployed internally within the EPA for government users and externally on a public-facing server for use by the public, academia, and the regulated community. The intent of this implementation is to accomplish EPA goals concerning transparency of the data analyses and scientific algorithm estimation components of the pesticide registration process. The project vision is an Agency collaboration platform that serves as an integrated scientific workflow application to implement relevant assessment methods, respond to changing empirical data availability (e.g., required toxicity tests, bioassays) and incorporate current fate, exposure, and effect algorithms in a model selection framework. Unlike the time-inefficient and outdated collection of legacy science components, this scientific modeling platform will replace critical regulatory data analysis and modeling processes with a more efficient, 21st century system at a reasonable cost.

Context of the research
#########################
Pesticide evaluations are required for ecological and human health risks under a number of regulatory statutes (e.g., Federal Insecticide, Fungicide, and Rodenticide Act (FIFRA), Pesticide Registration improvement Extension Act (PRIA 3), Federal Food, Drug, and Cosmetic Act (FD&C Act), Food Quality Protection Act (FQPA), Endangered Species Act (ESA)). Ecological risk assessments under FIRFA and ESA are often implemented by the Ecological Fate and Effects Division within the Office of Chemical Safety and Pollution Prevention by accessing model tools and databases that have been in continual development since the early 1980s on a range of software development platforms. These tools include Microsoft Excel Spreadsheets, Windows-based interfaces, legacy Fortran code compiled as DOS executables, as well as programs originally written in other programming languages (e.g., C, Perl, R). These models are parameterized with available information from a number of different source data sets that also may vary in format. The results are documented as risk assessment and management decisions for conventional active ingredients used in pesticide formulations. The National Pesticide Program manages 1100 active ingredients and 19000 products that must be reevaluated on a regular basis. The program also evaluates new pesticide formulations, ingredients, and novel uses of approved active ingredients. The result of this process is a large number of models to be run for many chemicals with many possible adverse outcomes that must be summarized and reported. The current system of distributed models and databases result in inefficiencies when conducting assessment and prevents transparency regarding the evaluation process for regulatory risk evaluation.

The decision to register a pesticide is based on the consideration of scientific data and other factors showing that it will not cause unreasonable risks to human health, workers, or the environment when used as directed on product labeling. The registration review program is intended to ensure that, as the ability to assess risk evolves and as policies and practices change, all registered pesticides continue to meet the statutory standard of no unreasonable adverse effects to human health and the environment. Changes in science, public policy, and pesticide use practices occur over time. Through the registration review program, EPA periodically reevaluates pesticides to ensure that as change occurs, products in the marketplace can be used safely. As part of the registration review process, EFED assesses risks of pesticides to Federally-listed threatened and/or endangered (listed) species from registered uses of pesticides.  These assessments are conducted in accordance with provisions of the Endangered Species Act (ESA), and the Services’ Endangered Species Consultation Handbook (NMFS). The models used are periodically updated in view of new pesticides, changing science, and as novel exposure pathways come to light.

Team Organization and Task Implementation
###########################

Modern software development methods are used to develop the web application, proceeding according to the principles of “scrum” development, an iterative and incremental agile software development process for developing software applications (Lacey 2012). This approach is centered around deploying applications in short time increments and getting rapid feedback from end users.  Both of these occur at the end of each defined sprint period (2-6 weeks)in length. This deployment and feedback approach is paired with modern industry standard approaches from XP programming and agile development.  XP programming approaches include test-driven development, pair programming, collective code ownership, sustainable development pace, coding standards, continuous integration, and code refactoring. Agile development processes include approaches for 

Scrum meetings are weekly on the same day every week at 3pm with monthly sprints replacing the scrum meeting the first Thursday of every month.  Daily checkins are likely to be conducted in Athens and via phone at 3pm EST for approximately 15-30 minutes. Monthly ubertool progress reports are also scheduled with EFED via conference call.

There are three core roles involved in this process, these roles are:
* Product Owner: represents the stakeholders via stories backlog and priorities (Tom Purucker)
* Development Team: delivers product increments at the end of each sprint (EPA employees, ORISE fellows, and SSA contractors working with ORD and EFED)
* Scrum Master: scrum facilitator who removes impediments for delivering sprint goals/deliverables, performs tasking, bug priority, task followup, etc. (contracted)


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

* Mark Bagley [ERD Division Director]
* Tina Bohardi [CSS NPD]
* Jim Cowles [Associate Director at EFED]
* John Kenneke [CSS Matrix Interface]
* Matt Martin [CSS Ecological Modeling Project Lead]
* Sandy Raimondo [CSS Dashboards Project Lead]
* Kate Sullivan [EAB Branch Chief]

Problem definition/Background
+++++++++++++++++++++++++++++++++++++

Goals and objectives of this project that will address this problem
##########################################
Efficiently conduct environmental assessments for pesticide registration and endangered species effects assessments for models that currently are deployed in a number of different ways (Fortran DOS executables, Windows programs, Excel spreadsheets) using data from a number of different data source.

Definition of the population the problem targets and what measures within this population the problem addresses
#######################################################
EFED risk assessors are the target audience for the ecological models. Main contacts include Bill Eckel, Ed Odenkirchen, and Tom Steeger. Three divisions within OPP will use the human health version of the product- HED, AD, and RD. Contacts include Vickie Dellarco, Jennifer McClain, Matt Lloyd, and Dana Vogel from the initial meeting. 

The ecological and human health divisions of OPP already share implementation of some of the models. There may be instances where OPPT personnel used similar models as the OPP human health risk assessment divisions and may use some of the models a la carte.  Members of the public, academia, and the registrants may use the product via a public facing web page in the future.

As python code, it can be run on a computer locally using a web browser as an interface (without being on the Internet, which will be necessary for the EPA to use it for applications involving confidential business information) and/or it can be hosted on the Internet as a web domain so that the public can access the public domain models that are used to determine pesticide registration and label restrictions (available at http://www.ubertool.org).  Component libraries for the ubertool can be accessed individually in non-HTML applications.  Alternatively, the code could be hosted on an EPA server with the requisite technologies to provide online access to the python code.  Regardless of how it is accessed, some of the models (these are mostly older Fortran codes in the public domain, not web applications) are of interest to the EPA pesticide office and could potentially realize significant efficiencies in regulating pesticides, transparency for the ecological risk assessment process, and higher levels of quality assurance given the larger audience that might use the models--whether for chemical regulation or for educational purposes.

Reason the project includes a modeling approach to address the problem (is it a new predictive tool?)
#########################################################################
EPA is responsible for registering pesticides under FIFRA; as part of the registration process, the EPA’s Ecological Fate and Effects Division of the Office of Chemical Safety and Pollution is responsible for analyzing data and developing/ implementing ecological models that estimate risks to non-target receptors. The Food Quality Protection Act of 1996 mandated the Environmental Protection Agency (EPA) to implement a new program for assessing the risks of pesticides, registration review. The decision to register a pesticide is based on the consideration of scientific data and other factors showing that it will not cause unreasonable risks to human health, workers, or the environment when used as directed on product labeling. The registration review program is intended to ensure that, as the ability to assess risk evolves and as policies and practices change, all registered pesticides continue to meet the statutory standard of no unreasonable adverse effects to human health and the environment. Changes in science, public policy, and pesticide use practices will occur over time. Through the new registration review program, EPA periodically reevaluates pesticides to ensure that as change occurs, products in the marketplace can be used safely. As part of the registration review process, EFED is assessing risks of pesticides to Federally-listed threatened and/or endangered (listed) species from registered uses of pesticides.  These assessments are conducted in accordance with the Overview Document[1], provisions of the Endangered Species Act (ESA), and the Services’ Endangered Species Consultation Handbook (NMFS 1998). The models used are periodically updated in view of new pesticides, changing science, and as novel exposure pathways come to light.


Models to be incorporated
#######################################

Databases to be incorporated
############################################

Projected outcomes and findings 
############################################

Summary of relevant literature
##############################################

Types of decisions that may be made as a result of this project
##################################################

Background information on the problem
########################################################
EPA (2004) provides an overview of OPP’s ecological risk assessment process:
www.epa.gov/espp/consultation/ecorisk-overview.pdf

Project Task Description and Schedule 
+++++++++++++++++++++++++++++++++++++++++++++++++++++++

Summary of work to be performed, products to be produced, and the schedule for implementation
#########################################################
To create an aggregate ubertool assessment, a user will have created the above data objects for each of the tables above, and will combine them to reate a batched assessment.  A tree with dropdown comboboxes that reflect available data objects saved to the user account will be presented to the user.  By selecting an appropriate data object for each of the 8 data node objects on the tree, the user can then execute the aggregate ubertool to run the included models.  At this point, there will be no option to deselect a constituent model in the aggregate ubertool.  We need a figure of a mock-up of the ubertool aggregate data tree.

An additional priority is development of the spatial overlay tool to compare endangered species ranges to crop and pesticide application distributions.  This will develop will proceed separately from the aggregate ubertool initially.

A future priority is using the fate and transport models to create exposure concentrations data objects that are used by a number of the ecological models.

List of products, deliverables, and milestones to be completed in the various stages of the project
#####################################################

Schedule of anticipated start and completion dates for the milestones and deliverables, and persons responsible for each
##########################################################

Quality Objectives and Criteria for Model Inputs/Outputs (A7)
++++++++++++++++++++++++++++++++++++++++++

Project data quality objectives (DQOs), performance criteria, and acceptance criteria
############################################################## 
All model components will be developed using an appropriate approach to quality assurance and documentation.

Description of task that needs to be addressed and the intended uses of the output of the modeling project to achieve the task
############################################################


List of requirements associated with the hardware/software configuration for those studies involving software evaluation
################################################################# 
Python uses web application frameworks that conform to a common standard called the Web Server Gateway Interface (WSGI).  We currently use two frameworks, webapp2 and Django, that help automate the integration of the Python backend and the web application frontend allowing for rapid development.

Web hosting services provide the cloud storage and host the web site containing the web applications.  These web services are vital to the übertool in terms of accessibility and data processing.  The Python web application frameworks work with the web hosting services to ultimately provide the deliverable to the end user.

The nature of web application development allows for the use of many cross-platform (i.e. Microsoft Windows, Apple OSX, Redhat Linux, etc.) software programs.  Python itself is a cross-platform language designed to easily integrate various programming languages.  The software development environment includes text editors such as Sublime Text, Python IDEs such as Spyder, Python extensions such as NumPy, and web browsers such as Microsoft’s Internet Explorer, Google’s Chrome, and Mozilla’s Firefox.

The source code for the übertool is version controlled using GitHub.  GitHub manages all changes to the source code, allowing for simultaneous development from multiple developers on the same source code.  Each developer has his/her own “branch” of the source code on which they work.  These branches are merged back into the “trunk” or master branch of the source code as the software is updated.  Software can be rolled back as necessary as GitHub tracks the history of the software development.

The übertool is requires database support for full functionality.  The database of choice is MongoDB as it is cross-platform, flexible, and open source. 

Documentation and records
++++++++++++++++++++++++++++++++++++++++++++++++++++
An updated version of the quality assurance plan will be developed annually and distributed by email. The date of the latest update will be included in the plan. Records of yearly quality assurance audits performed by the QA manager and QA officer are maintained by the QA manager. The auditor uses a checklist to mark which portions of the QAPP are followed, and to document deviations or absence of any QA measures. The results of such audits shall be documented and filed by the Quality Assurance Manager. The audit process itself shall be designed to objectively measure compliance with written procedures and assess the effectiveness of the process. The evaluation shall include interviews with development team members, and a review of research project work and quality records.

Before submission of a paper to an archival journal, the work will be reviewed for conformance with the applicable quality assurance criteria. Program code and output will be maintained in electronic data files and backed up on cloud platform (www.github.com). These documents will be maintained for a minimum of 5 years after the completion of the project. 

Code standards, code auditing and testing reports, interim project progress reports
######################################################
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

Some of these development tools may be accessible through ubertool subdomains in order to allow access from within the EPA firewall.

Configuration management (after production version) and code maintenance (e.g., or software internal documentation of logic and structure) manuals
########################################################################

Quality Assurance/Quality Control Processes
++++++++++++++++++++++++++++++++++++++++++++++++++
 
Resources and responsibilities for verification of model output
######################################
In addition to input data, government publications and publically available scientific liberature will be considered for the development of the model. For example, the Agency’s Wildlife Exposure Factors Handbook will be considered for estimating the dose to birds, mammals, terrestrial phase amphibians, reptiles, and terrestrial insects via ingestion of water by determining the appropriate allometric equations for each taxa’s drinking water intake. 

Analysis of model output relative to acceptance criteria
###########################################

Corrective action to be taken if criteria are not met
###################################################

Standard Operating Procedures
################################


Criteria used to review and validate (accept, reject, or qualify) model components such as theory, mathematical procedures, code, and calibration (convergence criteria, etc.) 
######################################


Criteria used to review and validate input data
######################################
To evaluate the correctness of programmed models, a quality control/quality assurance (QA/QC) page is created, which validates models’ inputs and outputs towards given sample calculations. The sources of sample calculations come from verified EPA reports. Any discrepancies will trigger an in-depth review of the code. Intermediate computations will be compared against simple analytical cases in order to localize the source of the error in the code. Discrepancies will be addressed through consideration of alternative scenarios and parameter values and adjustments to model structure as indicated by the feedback.

Input data will be obtained from verified EPA reports, which legitimizes the sources. Thus data review, verification, and validation will focus on the consistency of the input data used for calculations and modeling. As a result, an input table (Figure below) is present on the QA/QC page, including values used in the computation. Numerical comparisons between QA/QC input table and verified EPA reports will be executed. Any deviations will raise the check of the code and will be documented in writing and reviewed by the ORD Management team and the ORD Quality team.

Criteria used to test model performance
######################################
Model performance is checked through the ‘Batch’ mode, which sequentially calculates scenarios provided in the template. Two testing criterion are considered here: 1. repeat the same scenarios in the template (e.g. 10 times), and check the consistency of model inputs and outputs among 10 scenarios; 2. list a large number of scenarios (e.g. 10,000) and estimate the time consumed during the computation.

Criteria used to review or validate model outputs
######################################
The integrity of model output data will be verified and validated by project technical staff. Reviews may include a thorough evaluation of content and/or a “spot-check” of calculated between output tables (Figure below) in the QA/QC page and verified EPA reports. Should a review identify an aberration, the reviewer will notify those responsible for taking corrective actions. The QA officers will be notified if corrective action is potentially required. Evaluation of whether model components and their outputs are correct will be an ongoing process for QA personnel during the model calibration and validation stage of the project. In-progress assessments of validation issues will be discussed between a team including both technical and QA representatives from EPA. The results of performing evaluations will be logged and integrated into the project documentation at the conclusion of the project, as well any corrective actions that were implemented.  


Hardware/Software Configuration
+++++++++++++++++++++++++++++++++++++++
 
 
List of equipment, hardware, and software that will be used on the project
################################

Decisions regarding security issues
################################

Decisions regarding software installation issues
################################

Coding standards
################################

Testing plans
################################

Plans for an API
################################

Plans for a maintenance manual (explaining software logic and organization)
################################

Plans for source code for the ultimate user of the model or model framework
################################ 




Document Compliance
++++++++++++++++++++++++++++++++++++++++++++++++++


Statement of Question, Objectives, and Hypotheses 
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
Overarching research question, derived from problem statement 

Intended outcome of this piece of research (usually to test hypotheses and define relationships), including an estimate of time and resources needed 

Specific mechanistic hypotheses, tests in summary, populations to which the hypotheses are to be applied 


Methods 
##############################
A. List of variables and sources of variation, sorted byindepen- dent and dependent variables, with reasons for their selection 

B. Other sources of variation and how they will be dealt with 

C. Study design and analysis, including models, statistical tests if used, detailed analytical procedures, graphs of potential outcomes 

D. Field, laboratory, and computational procedures, in sufficient detail so that someone other than the author could do the study 

Budget and Schedule 
##########################

A. A comprehensive three-column budget for the duration of the study 

B. A schedule of tasks with initiation and completion target dates, with designated responsibilities and reporting requirements and dates


Reports and Publications 
################################
A. Intended disposition of research results, in terms of audience, publication type, and timing 

B. Fiscal, accounting, and procedural reporting requirements and how they will be met


References
################################

Apandi, T., 2009 Extreme Programming Pocket Guide. O’Reilly Media, Sebastopol, CA.

USEPA. 2004. Overview of the Ecological Risk Assessment Process in the Office of Pesticide Programs. U.S. Environmental Protection Agency, Office of Prevention, Pesticides and Toxic Substances, Office of Pesticide Programs, Washington DC. 100 pp. January 23, 2004.



Helms, J.C., 2013. Web-Based Application Quality Assurance Testing. Accessed at  http://ils.indiana.edu/faculty/hrosenba/www/S512/pdf/helm_web-qa.pdf on 9/5/2013.

U.S. FWS and National Marine Fisheries Service (NMFS). 1998. Endangered Species Consultation Handbook: Procedures for Conducting Consultation and Conference Activities Under Section 7 of the Endangered Species Act. Final Draft. March 1998.
