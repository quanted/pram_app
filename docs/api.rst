API
-----------

Setting up a REST Server
+++++++++++++++++++++++++++++++++++++++
The REST server is powered by Bottle, whose advantages include:

1. A simple and lightweight web-framework for Python 
2. Distributed as a single file module
3. Has no dependencies other than the Python Standard Library

The bottle library can be downloaded `here <http://bottlepy.org/docs/dev/index.html>`_, and started as:


.. code-block:: shell

	Python your_bottle_script.py


Creating a REST API for a FORTRAN Model
++++++++++++++++++++++++++++++++++++++++++++++++++++
An example of your_bottle_script.py looks like:

.. code-block:: python

	from bottle import route, run, post, request, auth_basic
	def check(user, passwd):
	if user == rest_key and passwd == rest_secretkey:
		return True
	return False

	@route('/przm/<jid>', method='POST') 
	@auth_basic(check)
	def przm_rest(jid):
		for k, v in request.json.iteritems():
			exec '%s = v' % k
		all_result.setdefault(jid,{}).setdefault('status','none')
		from przm_rest import PRZM_pi_new
			result = PRZM_pi_new.PRZM_pi(noa, met, inp, run, MM, DD, YY, CAM_f, DEPI_text, Ar_text, EFF, Drft)
		return {'user_id':'admin', 'result': result, '_id':jid}
	run(host=host_ip, port=8080, debug=True)

#. **@route('/przm/<jid>', method='POST')** links a function to an URL path. In this case, we link the */przm/<jid>* path to the *przm_rest(jid)* function
#. **@auth_basic(check)** is a simple authentication check. You can also use a bottle plugin, `Cork <http://cork.firelet.net/>`_, to achieve this
#. **exec ‘%s = v’ % k** automatically assign variable names and values sent from the frond-end
#. **PRZM_pi()** acturally calls the FORTRAN executable
#. **run(host=host_ip, port=8080, debug=True)** starts a built-in REST server

An example of **PRZM_pi_new.py** looks like:

.. code-block:: python

	def PRZM_pi(noa, met, inp, run, MM, DD, YY, CAM_f, DEPI_text, Ar_text, EFF, Drft):
		import os
		import shutil
		import subprocess
		import zipfile
		from boto.s3.connection import S3Connection
		from boto.s3.key import Key
		from boto.s3.bucket import Bucket
		import string
		import random
	
		####Generate a random name for the temporary file folder####
		def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
			return ''.join(random.choice(chars) for x in range(size))

		####Setting up the working folder####
		name_temp=id_generator()
		cwd='/home/PRZM'
		src1=cwd+'/'+name_temp
		src2=src1+"/przm3123-3.exe"
		if not os.path.exists(src1):
			os.makedirs(src1)
		else:
			shutil.rmtree(src1)
			os.makedirs(src1)

		####Copy files to the temporary folder####
		shutil.copy(src+"/inpsrc1/"+run,src1)
		shutil.copy(src+"/inpsrc1/"+inp,src1)
		shutil.copy(src+"/przm3123-3.exe",src1)
		shutil.copy(src+"/inpsrc1/"+met,src1)

		####call the PRZM file####
		os.chdir(src1)
		a=subprocess.Popen(src2, shell=0)
		a.wait()
		print('done')

		####Post-processing output files and return some values for output page display####
		x_precip=[]
		for line in file('CPRZM31.hyd'):
			line = line.split()
			x_precip_temp = line[0]
			x_precip.append(x_precip_temp)

		####zip all the file####
		fname=os.listdir(src1)
		zout=zipfile.ZipFile("out.zip","w")
		for name in fname:
			if name !='przm3123-3.exe':
				zout.write(name)
		zout.close()

		####Upload output files to a cloud storage####
		conn = S3Connection(key, secretkey)
		bucket = Bucket(conn, 'przm')
		k=Key(bucket)

		name1='PRZM_'+name_temp+'.zip'
		k.key=name1
		k.set_contents_from_filename('out.zip')
		link='https://s3.amazonaws.com/przm/'+name1
		k.set_acl('public-read-write')

		return link, x_precip

