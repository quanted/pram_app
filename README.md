ubertool_eco
============

eco submodule for ubertool

Outside of PyCharm - running servers from command line:
#to run the front end server on local port 8080
cd ubertool_eco
python manage.py runserver 8080
visit http://127.0.0.1:8080/ in your browser

#optional: run mongo
mongod --dbpath “c:\path\to\MongoDB\data”
#runs mongo with database in mongo\journal, you create the target data directory

#to run the back end server
cd ubertool_ecorest/REST_UBER
python bottle_local.py