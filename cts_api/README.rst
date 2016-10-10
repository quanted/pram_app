========
cts_api
========

CTS REST API 

Quick start
-----------

1. Add "cts_api" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'cts_api',
    ]

2. Update os.environ with calculator URLs:

    os.environ.update({
	'CTS_EPI_SERVER': '*.*.*.18',
	'CTS_EFS_SERVER': '*.*.*.12',
	'CTS_JCHEM_SERVER': '*.*.*.12',
	'CTS_SPARC_SERVER': 'http://204.46.160.69:8080',
	'CTS_TEST_SERVER': '*.*.*.16',
    })

3. Include the polls URLconf in your project urls.py like this::

    url(r'^api/cts', include('cts_api.urls')),

6. Visit http://134.67.114.1/api/cts/ for API docs.