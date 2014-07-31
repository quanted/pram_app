Architecture
------------
ubertool stuff

Technology stack
+++++++++++++++++
smaller point

Front-end server
++++++++++++++++++

Back-end server
++++++++++++++++
The primary component on the back-end server is Amazon Elastic Compute Cloud (EC2) since it: hosts the platform for data transfer between the front and back-end through Representational state transfer (REST) application programming interface (API); creates the environment for models to be executed; generates reports and documents; hosts a NoSQL database (MongoDB) to manage user history; and runs a Python-based task queue management system (Celery). Other elements on AWS include Simple Storage Service (S3) and Simple Queue Service (SQS), where the former is designed to store model output files for the long term and the latter manages requests generated from batch model runs.

.. figure:: /images/back_end_1.png
    :width: 400pt
    :align: center
    :height: 300pt
    :alt: alternate text
    :figclass: align-center

    Structure of the Back-end Server

The REST API for übertool is built on Bottle, a lightweight Web Server Gateway Interface (WSGI)-based Python framework [1]_. Bottle contains a single file and has no dependencies other than the Python Standard Library. While some full-stack web frameworks (e.g., Django and web2py) support a number of activities through build-in modules (e.g., interpreting requests, producing responses, storing data persistently, etc.), Bottle could achieve these features through plug-ins which enables developers to customize web applications easily. Conceptually, the REST API performs as a “hub” on the back-end server which receives requests and inputs from the front-end, distributes requests by invoking different functions, and transfers outputs to the front-end for display. All data transmitted over the REST API follow the JavaScript Object Notation (JSON) format commonly used in modern web applications [2]_. Three types of APIs are created: 1) executing legacy FORTRAN models; 2) generating reports based on model outputs (PDF and HTML format); and 3) exchanging information between a non-relational database, MongoDB. A noSQL database was preferred over a relational database because it is convenient to modify the existing data structure (e.g., introducing new fields, changing structure, etc.); has fast query speed, and is easy to scale horizontally through automatic sharing and building replications [3]_.



.. [1] Hellkamp, M. (2014). "Bottle."  0.12. from http://bottlepy.org/docs/dev/index.html.
.. [2] Crockford, D. (2009). "Introducing json." Available: http://www.json.org.
.. [3] Amol. (2014). "Web Frameworks for Python."   Retrieved March 14th, 2014, from https://wiki.python.org/moin/WebFrameworks.

D4EM server
+++++++++++++

Public deployment
++++++++++++++++++

EPA intranet deployment
+++++++++++++++++++++++++
