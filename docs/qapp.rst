#########################################
ubertool Quality Assurance Project Plan
#########################################

*************************************
Project Management
*************************************

Title and Approval Sheet
======================================

Title of QA Project Plan
------------------------------------
Quality Assurance Project Plan for USEPA Models used for Pesticide Registration

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
960 College Station Rd
Athens, Georgia 30605 USA

U.S. Environmental Protection Agency
Office of Pesticide Programs
Ecological Fate and Effects Division (EFED)
One Potomac Yard
Arlington, Virginia 22202 USA

Names of all key project officials, with space for dated signatures
---------------------------------------------------------------------

Table of Contents and Document Control Format
==================================================

Distribution List (A3)
==================================================
List of all individuals (and their role on the project) who will be provided copies of the approved QA Project
Plan, including all persons responsible for implementation, including project managers, QA Managers, and
representatives of all groups involved.
Tina Bahadori
Elaine Cohen Hubal
Jim Cowles
Bill Eckel
John Johnston
James Noel (QA Manager)
Nelson Thurman

Project/Task Organization (A4)
==================================================
The übertool is a web application implementation of ecological risk models used by the EPA in pesticide registration
under FIFRA and for the assessment of pesticide risks to endangered species. Modern software development methods
are used to develop the web application, proceeding according to the principles of “scrum” development, an iterative
and incremental agile software development process for developing software applications (Lacey 2012). This approach
is centered around deploying applications in short time increments and getting rapid feedback from end users.  Both
of these occur at the end of each defined sprint period (3 weeks) in length. This deployment and feedback approach
is paired with modern industry standard approaches from XP programming and agile development.  XP programming
approaches include test-driven development, pair programming, collective code ownership, sustainable development
pace, coding standards, continuous integration, and code refactoring. Agile development processes include approaches
for

Daily checkins are conducted on at 10am every working day for approximately 15 minutes. Scrum meetings are at the
beginning and end of each 3 week sprint.

Progress reports with OPP/EFED stakeholders and developers are conducted biweekly with EFED via conference call.

There are three core roles involved in this process, these roles are:
- Product Owner: represents the stakeholders by populating user stories in the backlog and sprint priorities
(Tom Purucker)
- Development Team: delivers product increments at the end of each sprint (USEPA federal Developers from OPP and ORD;
research fellows, student contractors and contractors working for OPP and ORD; others individuals identified by OPP/EFED)
- Scrum Master: scrum facilitator who removes impediments for delivering sprint goals/deliverables, performs tasking,
 bug priority, task followup, etc. (Tom Purucker)

Additonal roles on the scrum team are:
- Current Development Team: (Jon Flaishans, Carmen Kuan, Marcia Snyder, Andrew Kanarek, Tom Purucker, Kurt Wolfe,
Mike Galvin, Meredith Fry, Trip Hook, Gerry Laniak)
- Stakeholders: (Bill Eckel, Ed Odenkirchen, Dirk Young, Nelson Thurman, Kris Garber, Andrew Kanarek, Katrina White,
Meridith Fry, others identified by OPP/EFED)
- Managers: People who control the environment (John Johnston [Branch Chief], Tom Pierce/Gerald Brunson
[Division Director], John Kenneke [CSS Matrix Interface], Tina Bohardi [CSS], Elaine Cohen-Hubal[CSS], Jim Cowles [Associate
Director at EFED], James Noel [CED QA])

Problem Definition/Background (A5)
==================================================
Safety evaluations for pesticides are required for ecological and human health risks under a number of regulatory
statutes (e.g., Federal Insecticide, Fungicide, and Rodenticide Act (FIFRA), Pesticide Registration improvement
Extension Act (PRIA 3), Federal food, Drug, and Cosmetic Act (FD&C Act), Food Quality Protection Act (FQPA),
Endangered Species Act (ESA)).

The two primary statutes that EPA regulates pesticides under include the Federal Insecticide,
Fungicide, and Rodenticide Act (FIFRA) and the Federal Food, Drug, and Cosmetic Act
(FFDCA), both amended by the Food Quality Protection Act (FQPA) of 1996. Under FIFRA,
pesticides intended for use in the United States must be registered (licensed) by EPA before they
may be sold or distributed in commerce. EPA will register a pesticide if scientific data provided
by the applicant show that, when used according to labeling directions, it will not cause
“unreasonable adverse effects on the environment”. (FIFRA defines “unreasonable adverse
effects on the environment” as “any unreasonable risk to man or the environment, taking into
account the economic, social and environmental costs and benefits of the use of any pesticide
.....”) Under FFDCA, the Agency is responsible for setting tolerances (maximum permissible
residue levels) for any pesticide used on human food or animal feed.

With the passage of the Food Quality Protection Act (FQPA) in 1996, both major
pesticide statutes were amended to establish a more consistent, protective regulatory scheme
grounded in sound science. FQPA mandated a single, health-based standard for setting
tolerances for pesticides in foods; provided special protections for infants and children; expedited
approval of safer pesticides; created incentives for the development and maintenance of effective
crop protection tools; and required periodic re-evaluation of pesticide registrations and tolerances
to ensure that the scientific data supporting pesticide registrations would remain up-to-date in the
future. It should be noted that FQPA also limited the consideration of benefits when setting
tolerances. FQPA did not address the consideration of ecological risk.

The ubertool addresses ecological risk models under these regulations. Ecological risk assessments under
FIRFA and the Endangered Species Act (ESA) are typically implemented by the
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
regarding the evaluation process for regulatory risk evaluation. This project is addressing this limitation be
refactoring the existing EPA pesticide registration models and data as a scalable web application.

Goals and objectives of this project that will address this problem
---------------------------------------------------------------------
The overall objective of this effort is to implement appropriate technologies and update the source code base for the übertool,
a web application system that executes algorithms for pesticide registration and endangered species effects assessments.
This effort allows it to be deployed in scalable computational environments that provide front end access to cloud-executed
models and database backbone capabilities for querying and storing parameter inputs/outputs. This system is to be
deployed internally within the EPA for government users and externally on a public-facing server for use by the
public, academia, and the regulated community. The intent of this implementation is to accomplish EPA goals
concerning transparency of the data analyses and scientific algorithm estimation components of the pesticide
registration process. The project vision is an Agency collaboration platform that serves as an integrated scientific
workflow application to implement relevant assessment methods, respond to changing empirical data availability
(e.g., required toxicity tests, bioassays) and incorporate current fate, exposure, and effect algorithms in a model
selection framework. Unlike the time-inefficient and outdated collection of legacy science components, this scientific
modeling platform will replace critical regulatory data analysis and modeling processes with a more efficient, 21st
century system at a reasonable cost. This implementation allows for efficient environmental assessments
for pesticide registration and endangered species effects assessments
for models that currently are deployed in a number of different ways (Fortran DOS executables, Windows programs,
Excel spreadsheets) using data from a number of different data sources.

Definition of the population the problem targets and what measures within this population the problem addresses
---------------------------------------------------------------------
EFED risk assessors are the target audience for the ecological models. Main contacts include EFED scientists such as
Bill Eckel, Kris Garber, Ed Odenkirchen, and Tom Steeger. Three divisions within OPP that use human health version
models under the same
regulations are also a user base. Contacts include Vickie Dellarco, Jennifer McClain, Matt Lloyd, and Dana Vogel.
The ecological and human health divisions of OPP already share implementation of some of the models.
There may be instances where OPPT personnel used similar models as the OPP human health risk assessment divisions
and may use some of the models a la carte.  In addition, members of the public, academia, and the registrants may use
the product via a public facing web page.

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

Pesticide are defined in the Code of Federal Regulations (CFR), aas:
“Any substance or mixture of substances intended for preventing, destroying,
repelling, or mitigating any pest, or intended for use as a plant regulator,
defoliant, or dessicant....” (40 CFR 152.3).
Substances that are not covered in this definition include, but are not limited to,
deodorizers, non-toxic physical barriers against pests, fertilizers or other plant nutrient substances
which do not target pest species. Some products meeting the definition of a pesticide are exempt
from requirements of FIFRA, such as those for human drug use only, pesticide treated articles
(clothing, paints, etc.), pheromones used in traps, food preservatives, or natural repellants such as
cedar wood (40 CFR 152).
Based on 40 CFR 152.3, an active ingredient and an inert ingredient, respectively, are
defined as follows:
“Any substance (or group of structurally similar substances if specified by the
Agency) that will prevent, destroy, repel or mitigate any pest, or that functions as
a plant regulator, dessicant, or defoliant within the meaning of FIFRA section
2(a), except as provided in §174.3 of this chapter.”
“Any substance (or group of structurally similar substances if specified by the
Agency), other than an active ingredient, which is intentionally included in a
pesticide product, except as provided in §174.3 of this chapter.”
Many different types of pesticides are available. They may be grouped according to the
pests they control, their use pattern, or their chemical class. The following list provides some
examples of the categories of pesticides that are grouped according to the pests they control:

- Insecticides - act pesticidally against the growth or survival of insects. Also includes
specific types such as miticides, mosquito larvicides or adulticides;
- Herbicides - act pesticidally against plants, weeds, or grasses;
- Rodenticides - act pesticidally against rats or other rodents;
- Avicides - act pesticidally against damaging bird populations;
- Fungicides - act pesticidally against fungi on food or grain crops; • Nematicides - act pesticidally against nematodes;
- Fumigants - gaseous pesticides used for invertebrate and fungal control;
- Antimicrobials - act pesticidally against microscopic organisms on a variety of sites;
- Plant Growth Regulators - accelerate or retard plant growth rates;
- Insect Growth Regulators - retard insect growth;
- Biopesticides - naturally occurring substances with pesticidal properties, including
microbial pesticides, biochemical pesticides and plant incorporated protectants;
- Piscicides - act pesticidally against unwanted or invasive fish populations; and
- Molluscides - act pesticidally against slugs, snails, or bivalves.

Pesticides may also be categorized into the following general use patterns in order to
determine registration data requirements: terrestrial, aquatic, greenhouse, forestry, domestic
outdoor, and indoor (40 CFR 158). The terrestrial, aquatic, and greenhouse patterns are further
divided into food crop and nonfood applications.

Pesticides that have similar chemical structures often have similar modes of action, as
well as comparable fate and transport properties. Such chemicals may be grouped in the same
chemical class. Some examples of chemical classes include the following:
- Insecticides: chloronicotinyl compounds (e.g., imidacloprid, nicotine), N-methyl
carbamates (e.g., carbaryl, aldicarb), organophosphorus compounds (e.g., chlorpyrifos,
diazinon), and pyrethroids (e.g., cyfluthrin, cypermethrin), and others.
- Herbicides: benzoic acids (e.g., dicamba), chloroacetanilides (e.g., alachlor,
metolachlor), chlorophenoxy acids/esters (e.g., 2,4-D, MCPA), imidazolinones (e.g.,
imazamox, imazapyr), sulfonylureas (e.g., bensulfuron-methyl, rimsulfuron),
thiocarbamates (e.g., butylate, molinate), and triazines (e.g., atrazine, simazine), and
others.
- Fungicides: benzimidazoles (e.g., benomyl, thiabendazole), carboxamides (e.g., carboxin,
flutolanil), and dithiocarbamates (e.g., maneb, ziram), and others.

Reason the project includes a modeling approach to address the problem
-----------------------------------------------------------------------
EPA is responsible for registering pesticides under FIFRA; as part of the registration process, the EPA is responsible
for analyzing data and
developing/ implementing ecological models that estimate risks to non-target receptors. The Food Quality Protection
Act of 1996 mandated a new program for assessing the risks of
pesticides, registration review. The decision to register a pesticide is based on the consideration of scientific data
and other factors showing that it will not cause unreasonable risks to human health, workers, or the environment when
used as directed on product labeling. The registration review program is intended to ensure that, as the ability to
assess risk evolves and as policies and practices change, all registered pesticides continue to meet the statutory
standard of no unreasonable adverse effects to human health and the environment. Changes in science, public policy,
and pesticide use practices will occur over time. Through the new registration review program, EPA periodically
reevaluates pesticides to ensure that as change occurs, products in the marketplace can be used safely. As part
of the registration review process, EFED is assessing risks of pesticides to Federally-listed threatened and/or
endangered (listed) species from registered uses of pesticides.  These assessments are conducted in accordance
with the Overview Document, provisions of the Endangered Species Act (ESA), and the Services’ Endangered
Species Consultation Handbook (NMFS 1998). Models are and integral part of this process, and are periodically updated
in view of new pesticides,
changing science, and as novel exposure pathways come to light.

Specific EPA responsibilities include assessing and characterizing ecological risk from varying pesticide scenarios in a
screening-level assessment, which includes the consideration of listed species. These
assessments address (1) fate and transport of pesticides in water, soil, and other
environmental media; (2) toxicity to wildlife and vegetation; (3) exposure to non-target
vegetation, aquatic life, birds, and other wildlife; and (4) effects on listed species. More refined assessments may
be conducted on a case-by-case basis and typically involve some combination of the models addressed here.
An additional core responsibility is for the EPA to develop and advance methods and tools for
environmental fate, ecological risk and drinking water assessments.

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

By law, the Agency has the authority to obtain data under three provisions of FIFRA:

- FIFRA 3(c)(1)(F) - Authorizes the Agency to require data to support an application for
registration of a pesticide. OPP’s data requirements are set forth in 40 CFR Part 158, but
EPA has broad authority to ask for additional data or waive requirements, as appropriate.
These data requirements are discussed under Section IV of this document.
- FIFRA 3(c)(2)(B) - Provides the authority to require additional data on currently
registered products. These data must be “required to maintain in effect an existing
registration of a pesticide.” If EPA imposes a data requirement under this authority, EPA
must allow enough time to design the study and generate data. In addition, EPA must
comply with the Paperwork Reduction Act.
- FIFRA Section 6(a)(2) - Requires that pesticide registrants inform the Agency of any
relevant adverse effects information relating to their products, even though it was not
formally requested by EPA. Information reportable under this provision includes new
information derived from scientific studies, such as efficacy failures of antimicrobial
products and pest resistance. Incidents of adverse effects resulting from the use of
pesticide products are also reported. The information collected under 6(a)(2) is tracked
and regularly distributed to the various divisions in OPP, as appropriate.

Any other types of problems that the project may address
---------------------------------------------------------------------
The science models in the ubertool provide testable predictions concerning chemical concentrations in environmental
media, exposure doses, tissue residues and ultimately predictions of effects. These predictions are relevant for a
number of ecological species under regulations that the EPA is responsible for - including FIFRA, ESA, FFDCA, and the
FQPA. These model predictions can be tested by comparing them to relevant data from laboratory, field and/or modeling
investigations. From an exposure perspective, improvements to this core set of models can come in different forms --
they may include:

- better algorithms: algorithmic improvements to core EPA ecological models (e.g., updated versions of T-Rex, PRZM,
EXAMS), many of which were initially developed at ORD, to provide better predictive capability or extend their use
to new exposure settings,
- identifying novel exposure areas: (receptors, environments) not adequately covered by the current set of ecological
models (e.g., ongoing research for amphibians and honeybees),
better input data: finding new data sources that improve ecological model (e.g., molecular bioassay endpoints, -omics
applications, propose/modify/eliminate specific registrant data submittal requirements),
- scaling exposure processes: enable applications of existing models in spatially and temporally realistic settings
at scale (e.g., SAM applications for endangered species), and/or
- replace existing models: evaluating proposed replacements for models that are currently used in pesticide
registration decisions via model selection processes.
All of these improvements require execution of the existing models in order to scientifically demonstrate model
enhancements in a reproducible manner. The primary goal of these studies is to minimize false positive and false
negative pesticide registration decisions made by the Agency, so the relevance of these types of scientific
exercises is very high.

Background information on the problem
---------------------------------------------------------------------
EPA (2004) provides an overview of OPP’s ecological risk assessment process.

Reasons the project is important, how it supports other existing research, programs, or regulations
---------------------------------------------------------------------
This project directly support EPA regulatory proigramsn. The two main regulatory processes for pesticides are
registration and reregistration.

Registration focuses on decisions that allow new pesticide products to enter the market place or
that allow registrants to make changes to the way existing pesticide products are sold, distributed,
or used. While many registration decisions involve minor changes or applications for new
products that are identical to currently registered pesticides, EPA devotes considerable resources
to the review of applications involving new active ingredients and applications involving new
uses of currently registered pesticides.

Section 3 of FIFRA authorizes EPA to register new pesticide products and new uses of
existing pesticide products for use in the United States. In registering pesticide products, EPA
may place restrictions on the site or crop on which it is used; the method, amount, frequency, and
timing of its use; and the storage and disposal practices. Some pesticides may be registered for
more limited use in certain states. In addition, States, Tribes and Territories can place further
restrictions on EPA-registered pesticide products used or sold within their own jurisdictions.
For a Section 3 registration action, the pesticide manufacturer submits to EPA a
registration application, which includes the following information:

- Required test data;
- Information concerning the manufacturing process;
- Product chemistry;
- Human and environmental risk data packages;
- Tolerance information, consisting of information about pesticide residues on food; and
- Labeling information.

The scientific review is assigned for an evaluation of human health risks and for evaluating environmental risks,
including potential risks to listed species. Human health effects and exposure data are integrated
into a comprehensive health risk
assessment to assess the potential impact that the pesticide product or active ingredient will have
on the human population. At the same time, scientific ecological effects and
exposure information are integrated into an environmental risk assessment to assess potential impacts on the
environment. Both the health and environmental risk assessments undergo a process of internal
peer review by scientific experts.

All new chemicals submitted for a Section 3 registration to
EFED and HED for a complete scientific review. For ecological risk, EFED provides an initial
review and risk assessment for non-target species, including listed species. This assessment is
conducted using data, which are required based on the uses of the pesticide.
Some pesticide uses, such as indoor application, are screened to determine if there
is a potential exposure to non-target organisms. If there is no exposure, these uses may not
require environmental fate and ecotoxicity data or a full scientific review. For example, some
specialized uses, such as indoor greenhouse applications, are screened to determine if there is a
potential to effect non-target organisms through pesticide disposal. If not, data are not required
and an ecological assessment is not conducted.

Section 3 amendment actions are screened to determine if there
is an obvious change from the present labeled use. Those actions which indicate a change in the
use are sent to the science divisions for review.
In cases where screening-level ecological risk assessment results raise potential
concerns related to listed species, a species-specific evaluation is conducted to refine the
assessment.

After risk assessments are completed, the registration process includes a review of the
risk assessments and development of potential risk mitigation measures. A
registration determination is made based on the statutory standards of FIFRA and FFDCA. If the
application fails to meet these standards, the need for more or better data, labeling
modifications, and/or use restrictions is noted and these facts and communicated
to the applicant. If the
application is approved, EPA will establish a tolerance if the pesticide is intended for use on food
or feed and publish a notice in the Federal Register.

Reregistration is the review of older pesticides to ensure that they meet current health,
safety, and environmental standards. The goal is to update labeling and use requirements and
reduce risks associated with older pesticides, which were registered when the standards for
government approval were less stringent than they are today.

Under Section 4 of FIFRA as amended in 1988, EPA reviews older pesticides (those
initially registered before November 1, 1984) to ensure that they meet current scientific and
regulatory standards. This process, called reregistration, considers the human health and
ecological effects of pesticides and results in decisions to reduce risks that are of concern. EPA
also is reassessing tolerances (pesticide residue limits in food) to ensure that they meet the safety
standard established by FQPA. EPA has integrated reregistration and tolerance reassessment to
most effectively accomplish the goals of both programs.

Through the reregistration program, EPA is reviewing the human health and
environmental effects of groups of related pesticide active ingredients. When EPA completes the
reregistration review and risk management decision for a pesticide, the Agency generally issues a
Reregistration Eligibility Decision (RED) document. The RED summarizes the risk assessment
conclusions and outlines any risk reduction measures necessary for the continued registration of
the pesticide in the U.S.

EPA may also issue an Interim Reregistration Eligibility Decision (IRED) for a pesticide
that is undergoing reregistration, requires a reregistration eligibility decision, and also needs a
cumulative assessment under FQPA. The IRED, issued after EPA completes the individual
pesticide's aggregate risk assessment, presents an interim decision for the pesticide undergoing
reregistration. It may include risk reduction measures -- for example, reducing risks to workers
or eliminating uses that the registrant no longer wishes to maintain -- to gain the benefits of these
changes before the final RED can be issued following the Agency's consideration of cumulative
risks.

To be declared “eligible” for reregistration, pesticides must meet current scientific and
regulatory standards. The pesticide must have a substantially complete database and must not
cause unreasonable adverse effects to human health and the environment when used according to
Agency approved labeling directions and precautions.

In addition, all pesticides with food uses must meet the safety standard of Section 408 of
the FFDCA, as amended by FQPA. FFDCA as amended by FQPA also requires the reassessment
of all existing tolerances and tolerance exemptions within 10 years, to ensure that they meet the
safety standard of the new law.

Reducing risks is an important aspect of the reregistration program. EPA works with
stakeholders including pesticide registrants, growers and other pesticide users, environmental and
public health interest groups, the States, USDA and other Federal agencies, and others to develop
voluntary measures or regulatory controls needed to effectively reduce risks of concern. Almost
every RED includes some measures to reduce human health and/or ecological risks. The
possible ways of achieving risk reduction are extensive and include measures such as canceling
pesticide products or deleting uses; declaring certain uses ineligible or not yet eligible (and then
proceeding with follow-up action to cancel the uses or require additional supporting data);
phasing out uses; restricting use of products to certified applicators; limiting the amount or
frequency of use; improving use directions and precautions; adding more protective clothing and
equipment requirements; requiring special packaging or engineering controls; requiring notreatment
buffer zones; requiring spray drift labeling; employing ground water, surface water, or
other environmental and ecological safeguards; and other measures. Modeling results are often used as paret
of these modifications.

Conflicts or uncertainties that will be resolved by this project
---------------------------------------------------------------------
FIFRA is the federal statute that governs the sale, distribution, and use of pesticides in the United
States; it assigns EPA the authority to issue pesticide registrations or reregistrations, which are required
for use of the pesticides. To obtain a registration, an applicant must demonstrate that a pesticide will
perform its intended function and will not cause unreasonable adverse environmental effects. Once
granted, the registration requires that the pesticide be labeled with specific product information, directions
for use, and hazard information; the label specifies legal use of the pesticide.
The ESA is the federal statute that assigns FWS and NMFS the authority to designate species as
threatened or endangered—that is, to “list” species—and governs the activities that might affect listed
species. Under the ESA, federal agencies must ensure that their actions do not harm listed species or
jeopardize their existence. Accordingly, if EPA is deciding whether to register a pesticide, it must
determine whether the action “may affect” a listed species. If the answer is yes, EPA has the option of
initiating a formal consultation or conducting further analysis to determine whether the action is “likely to
adversely affect” listed species. If EPA determines that the action is not likely to affect listed species
adversely—and FWS or NMFS, as appropriate, agrees—no further consultation is required. However, if
EPA determines that the action is likely to affect a listed species adversely, a formal consultation is
required, and FWS or NMFS must determine whether the proposed action is likely to jeopardize the
existence of the listed species. The product of that determination is called a biological opinion (BiOp)
and is issued by FWS or NMFS.

Therefore, the US Fish and Wildlife Service (FWS) and the National Marine Fisheries Service (NMFS) are responsible for
protecting species that are listed as endangered or threatened under the Endangered Species Act (ESA) and for
protecting habitats that are critical for their survival. The EPA is responsible for registering or reregistering
pesticides under FIFRA and must ensure that pesticide use does not cause any unreasonable adverse effects
on the environment, which is interpreted to
include listed species and their critical habitats. The agencies have developed their own approaches to
evaluating environmental risk, and their approaches differ because their legal mandates, responsibilities,
institutional cultures, and expertise differ. Over the years, the agencies have tried to resolve their
differences but have been unsuccessful in reaching a consensus regarding their assessment approaches.
As a result, FWS, NMFS, EPA, and the US Department of Agriculture asked the National Research
Council (NRC) to examine scientific and technical issues related to determining risks posed to listed
species by pesticides. Specifically, the NRC was asked to evaluate methods for identifying the best
scientific data available; to evaluate approaches for developing modeling assumptions; to identify
authoritative geospatial information that might be used in risk assessments; to review approaches for
characterizing sublethal, indirect, and cumulative effects; to assess the scientific information available for
estimating effects of mixtures and inert ingredients; and to consider the use of uncertainty factors to
account for gaps in data. This report was published in NAS (2014).

The assessments conducted, either at the screening or the more refined species-specific
level, need to be based on a sound scientific process. This process entails using sound scientific
methods, developing adequate supporting tools such as databases, and conducing adequate peer
review to further strengthen the process. These
assessments necessarily address (1) fate and transport of pesticides in water, soil, and other
environmental media; (2) toxicity to wildlife and vegetation; (3) exposure to non-target
vegetation, aquatic life, birds, and other wildlife; and (4) effects on listed species. More refined assessment
may also be conducted on a case-by-case basis.

Rarely are toxicity data available for the species identified in the risk assessment
endpoints. In the majority of cases, the screening-level risk assessment process relies on a suite
of toxicity studies performed on a limited number of organisms in the following broad groupings:

- Birds (mallard duck and bobwhite quail) used as surrogate for terrestrial-phase
amphibians and reptiles,
- Mammals (laboratory rat),
- Freshwater fish (bluegill sunfish, rainbow trout, and fathead minnow) used as a surrogate
for aquatic phase amphibians,
- Freshwater invertebrates (Daphnia magna),
- Estuarine/marine fish (sheepshead minnow),
- Estuarine/marine invertebrates (Crassostrea virginica and Mysidopsis bahia),
- Terrestrial plants (corn, soybean, carrot (radish or sugar beet), oat (wheat or ryegrass),
tomato, onion, cabbage (cauliflower or brussels sprout), lettuce, cucumber), and
- Algae and aquatic plants (Lemna gibba, Skeletonema costatum, Anabaena flos-aquae,
Selenastrum capricornutum, Clorell vulgaris, Scenedesmus subspicatus)

Within each of these very broad taxonomic groups, an acute and a chronic endpoint are
selected from the available test data. The selection is made from the most sensitive species tested
within that organism group. If additional toxicity data for more species of organisms in a
particular group are available, the selection need not be limited to the species listed above, but
may be expanded to include data for other species/studies.
Available scientific information from alternate sources (e.g. searches conducted using the
ECOTOX database) is also examined for species within a
taxonomic group for which other taxa are typically used as surrogates. For example, fish data are
commonly used to evaluate impacts to amphibians. But, if toxicity data are available in the open
literature on amphibians, these data may be used instead of the data on the surrogate species. In
situations where such additional data are available, decisions are made regarding the quality and
utility of such information in the risk assessment (e.g., a review of the validity and reliability of
study protocols), which is consistent with the Agency’s risk assessment guidance. The extent to
which such additional data are either employed or rejected is described through a transparent,
concise discussion. Regardless of the extent of data beyond the regulation-required set of
toxicity studies, the risk assessment relies on selection of endpoints from the most sensitive
species tested in acceptable studies.

Exposures estimated in the screening-level risk assessment for non-target organisms are
likewise not specific to a given species. Aquatic organism (plant and animals) exposures are
based on a set of standardized water body assumptions (water body size, watershed size,
proximity to field, etc.) that result in high-end estimates of exposure.
Estimates of exposure for terrestrial birds and mammals assume that animals are in the treatment
area, and exposure estimates involve grouping taxa based on food preferences (e.g., obligate
insectivores, herbivores, granivores) and generic weight classes. Exposure for terrestrial plants
considers surface runoff from treated fields as well as direct application via pesticide spray drift.

Risk characterization integrates the results of exposure and toxicity data to evaluate the
likelihood of adverse ecological effects on non-target species. For most chemicals, the effects
characterization is based on a deterministic approach using one point on a concentration-response
curve (e.g., LC50). In this approach,the risk quotient (RQ) method is used to compare
exposure to toxicity. Estimated environmental concentrations (EECs) based on maximum
application rates are divided by acute and chronic toxicity values.

In cases where screening-level acute RQs for a given animal group equal or exceed the
endangered species acute LOC, the Agency uses the dose response relationship from the toxicity
study used for calculating the RQ to estimate the probability of acute effects associated with an
exposure equivalent to the EEC. This information serves as a guide to establish the need for and
extent of additional analysis that may be performed using Services-provided “species profiles” as
well as evaluations of the geographical and temporal nature of the exposure to ascertain if a not
likely to adversely affect determination can be made. The degree to which additional analyses
are performed is commensurate with the predicted probability of adverse effects from the
comparison of dose response information with the EECs. The greater the probability that
exposures will produce effects on a taxa, the greater the concern for potential indirect effects for
listed species dependant upon that taxa, and therefore, the more intensive the analysis on the
potential listed species of concern, their locations relative to the use site, and information
regarding the use scenario (e.g., timing, frequency, and geographical extent of pesticide
application).

When the Agency can, upon additional analysis at the screening level, support a not
likely to adversely affect determination, the basis for the conclusion is documented in the
endangered species section of the risk assessment. When the screening level assessment
indicates a not likely to adversely affect can not be determined with this level of refinement, the
findings and rationale are documented and additional analysis of the geographical and temporal
nature of the exposure, as well as more in-depth evaluations of the biological and ecological
requirements of potentially indirectly impacted species are addressed to ascertain whether a not
likely to adversely affect determination can be made.

On top of these issues, the NAS report suggests adding population models and the ability to do uncertainty analyses
to these combinations of calculations. Implementation of these suggested approaches requires
upgrading the constituent models used in the ecological risk process to an integrated implementation that can be run
in scalable environments. This approach is necessary in order to be able to run all the combinations of chemicals,
species, watersheds and application scenarios that must be considered when assessing the risks from a registered
chemical to endangered species.

Reasons one model is determined to be better than another for this application
---------------------------------------------------------------------
The program office uses them, after a review process...

Project/Task Description and Schedule (A6)
==================================================


Summary of all work to be performed, products to be produced, and the schedule for implementation
---------------------------------------------------------------------
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
---------------------------------------------------------------------------------------------------
The ubertool is developed in an iterative development environment, so that new releases of the web application are
deployed every 3 weeks at the conclusion of each sprint.

Schedule of anticipated start and completion dates for the milestones and deliverables, and persons responsible for each
-------------------------------------------------------------------------------------------------------------------------

- Code all constituent (OPP/ORD) models in Python and Fortran based on available code, users’ manuals, and existing
qapps into a single library (complete).
- Host all models in library on a back end rest server (bottle) so they can be called from a web browser session
(complete).
- Create front end instances (django) for all the models so that they can be fed input data and run in a web browser (complete).
- Create parameter crosswalk between all model inputs and outputs for qaqc purposes (complete).
- Create database system (mongodb) to record individual model inputs and outputs persistently for all user-based execution (complete).
- Initiate OEI/NCC application deployment checklist process (complete): http://cfint.rtpnc.epa.gov/adc/reviewcenter/index.cfm?ADCNumber=3146
- Deploy front and back end model services to multiple CGI servers (complete).
- Use parameter crosswalk as template to collect qaqc input/output test case scenarios, 10 per model (complete).
- Public demonstration of tool to industry at EFED workshop (October 29, 2014) (complete): https://www.federalregister.gov/articles/2014/10/08/2014-24026/spatial-aquatic-model-development-notice-of-public-meeting
- Submit system security plan to OEI (complete).
- Submit syscat categorizations for all models to OSIM/OEI (complete).
- Pass system vulnerability scans performed by NCC (complete).
- Add disclaimers regarding beta status of models (complete).
- Setup dns, apache and nginx configurations so that epa can route traffic to appropriate cgi cloud hosted implementations (complete).
- Submit firewall rule request for ports 80, 443 (22) to allow public access. (complete, but temporary), available on intranet and internet at http://qed.epa.gov/ubertool
- Public workshop with industry and others providing comment on current status of tool (April 29, 2015) (complete): https://www.federalregister.gov/articles/2015/04/03/2015-07645/spatial-aquatic-model-development-notice-of-public-meeting
- Implement betatester password protected input pages to restrict public (internet, not intranet) execution of models to those with a password (will complete on 6/12/2015).
- Resubmit permanent firewall rule request for internet access (June 2015).
- Migration from CGI NCC contract to CGI general services contract, redeploy all servers to more modern (more secure) EPA red hat enterprise linux implementations (July 2015).
- Implement qa/qc testing against previously gathered test cases (mostly complete, but being refactored for efficiency). Automate for daily execution.
- Ongoing Spatial Aquatic Model code changes in collaboration with EFED (ongoing).
- SSL encryption of all traffic (port 443) (Fall 2015).
- NERL web application clearance process (to be defined by David Kryak et al) (Winter 2015-2016).
- Remove betatester authentication on approved models (Spring 2016).
- Public rollout of ubertool (late Spring 2016).


Quality Objectives and Criteria for Model Inputs/Outputs (A7)
====================================================================

Project data quality objectives (DQOs), performance criteria, and acceptance criteria
---------------------------------------------------------------------
All model components will be developed using an appropriate approach for quality assurance and documentation.

Description of task that needs to be addressed and the intended uses of the output of the modeling project to achieve the task
---------------------------------------------------------------------
The EPA registers pesticides for use in the US under applicable federal laws. To assess potential risks, mathematical
models are used to predict pesticide concentrations in different media and ultimately predict effects to non-target
species.  The suite of models that the EPA uses has been in development since the 1980s, with a wide range of
algorithmic complexity and technical implementation from Fortran executables to Microsoft Excel spreadsheets. We have
updated these models to create an application programming interface (API) that is accessible via a web service
implementation. Hosted in the cloud, the application combines relevant spatial information, chemical properties,
ecological exposure parameters, pesticide use properties, and effects data into a decision support “dashboard.”
The system is a platform-as-a-service implementation and is available to users through the use of modern web
technologies that allow cloud-based ecological pesticide models and data to be accessed with a web browser.

The larger outcome is that scientists with original ideas, models, data, and tools no longer have to secure significant
resources for hardware and application programmers to ensure that “translational” research can find a use in regulatory
decision support structures. This availability will lead to better data and model selection decisions and a more robust,
defensible regulatory frameworks. The resulting dashboards can increase decision-making transparency and serve as a
conduit for translating science improvements to the regulatory process -- all while functioning in production mode as
a form of “Science-as-a-Service” to provide the necessary assessment tools for environmental regulation.

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

Environmental models may require the ability to scale their implementation. This may be in response to a need to
execute more complex, detailed applications and/or be responsive to multiple users in a distributed modeling setting.
Regardless, such implementations may require a combination of significant core computing capacity and concurrency
control that is difficult to achieve in a desktop environment. Scaling these models can present challenges, but
may be necessary for Monte Carlo simulation, for higher spatial resolution and/or geographical scale, long time
series modeling, and/or to account for multiple simultaneous users.

This hands-on workshop will allow users to deploy a combination of modern technologies that can address these
issues. Participants will quickly build a running instance on their laptop of the leading containerization technology,
Docker, in order to deploy a set of environmental models.  Container-based technologies separate the application
from the underlying infrastructure, just like virtual machines separate the host operating system from the underlying
hardware. These technologies allow for the ability to build and configure an environmental model once, and then
deploy and run the model anywhere. The core services consist of a daemon that is installed on a machine and a
client that interacts with the daemon. A typical workflow then consists of a containerized image that is layered
to contain the host operating system, environmental model(s), and all dependencies. Images are used to create
containers that can be started, stopped, moved or deleted. This technology is supported by a registry system that
allows for public or private access to repositories that store images as well as a system for automating building
images. This lightweight approach is portable and scalable, with the ability to launch and shut down additional
machines as needed.

To fully leverage this technology, the models in the containerization image will be in the form of application
programming interface (API) representation state transfer (RESTful) web services. We will address approaches for
accessing these endpoints and leveraging their deployment within cloud environments, providing Models-as-a-Service.
RESTful endpoints opens up a number of possibilities for scaling computations and allow for model interoperability
possibilities at both the computational/ algorithmic  level and from a user interface (mobile, desktop or web)
development standpoint.


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
github

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
A key component for science is reproducibility. So, the science infrastructure worthy of the award would not be a
“secret science” application executed in an infrastructure that only we hold the key to, instead the computations
would be (first internally, then) publicly available in a reproducible manner that facilitates the comparison of
model predictions to available data. The statistical comparison of model predictions and the data would therefore be
part of the same system. The only computational route for us in NERL to make scalable computations and large data
sets available to all-comers is via cloud-hosted web applications. Desktop applications do not have the ability to
scale and are not reasonably downloadable when they contain regional level high resolution data; OEI/OSIM
interpretations of EPA guidance memos they wrote prevents us from serving data and running models on our NERL machines;
and we do not have anywhere near the resources that it would take to have OEI/NCC/etc stand such a system up for us --
nor do we feel they could provide a capable science solution or a sufficient front end even if we gave them a
significant portion of our research resources. Therefore, I think we need to be the first to fully leverage the
cloud within the Agency for model execution purposes. The CGI cloud contract is OEI approved and OEI is under a lot
of pressure from outside the agency to show that they are migrating applications to the cloud.

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
PEP-8

Testing plans
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Plans for data dictionary (may not need to be a separate document)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Plans for a user’s manual
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Online

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
Models will be published as publicly consumable APIs. APIs function by linking different information sources in a
shared network of data and services. This ensures mutually beneficial sharing of authoritative data sets, services,
and infrastructures within and outside of the Agency in a controllable manner. EPA chemical exposure and effects
models have been developed at different times and based on different underlying technologies over the last 40 years,
there are a number of legacy codes that underlay important scientific processes. The resulting set of Agency models
differ in programming languages, deployment processes, operating systems, and other technical dependencies. These
structural differences have hindered their accessibility, transparency, interoperability and scientific use.
Modern API development that relies on REST services, remote procedure calls and cloud server infrastructures resolves
these difference and enhance service and model reuse by regulatory and scientific communities. This approach addresses
scientific web services security in a federally approved manner, provides “web analytics” -- offering a supplement to
journal metrics in documenting the impact of EPA models, and makes the algorithms more “discoverable” -- thereby
increasing their use.

Of significant scientific importance is that providing an API and the underlying web services via a cloud computing
environment provides computational scaling abilities not currently available for chemical modeling on the desktop by
leveraging a cloud computing infrastructure (CGI). The federal government has mandated a “Cloud First” strategy to
help federal agencies provide highly reliable, innovative services quickly and efficiently despite resource constraints.
Cloud computing allows for the pooling of computer servers into an integrated system even if those servers are running
different operating systems and applications with different technological dependencies. Computational power is
increased or decreased depending on real-time workload requirements, and the system is continually reconfigured to
meet new types of workloads. This scalability allows for other scientific programmers to leverage the tools, whether
they are scientific applications of the models themselves, providing dashboard services, or embedding them within
more complex regulatory workflows (e.g., ubertool). Cloud-based scientific applications include Monte Carlo
applications to examine parameter sensitivity and model uncertainty, frequentist and Bayesian approaches for model
calibration and selection/weighting, distributed spatial scaling of science algorithms, and/or data intensive
algorithms run at high temporal resolution.

Cloud-based API construction can enhance regulatory transparency, increase the impact of existing Agency science,
and greatly accelerate the translation of new science and algorithms to regulatory application. The EPA has the
opportunity to be in the vanguard due to the significant set of science models they “own”, the existing cloud
infrastructure, and significant progress already made for FIFRA/ESA ecological models (front end, back end).
Similar opportunities exist for human health models and ecological models for non-FIFRA/ESA applications.

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
All models included for FIFRA pesticide registration go through a Science Advisory Panel review by NIH and NSF
appointed external reviewers. (USFCR)


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

USFCR 2015. http://www.ecfr.gov/cgi-bin/text-idx?SID=4d543e597be707174b093d3907abd312&mc=true&tpl=/ecfrbrowse/Title40/40cfrv24_02.tpl#0
Accessed November 18, 2015.

USFWS and National Marine Fisheries Service (NMFS). 1998. Endangered Species Consultation Handbook:
Procedures for Conducting Consultation and Conference Activities Under Section 7 of the Endangered Species Act.
Final Draft. March 1998.
