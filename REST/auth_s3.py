import os


def auth_check():
	import base64
	import keys_Picloud_S3
	
	api_key=keys_Picloud_S3.picloud_api_key
	api_secretkey=keys_Picloud_S3.picloud_api_secretkey
	base64string = base64.encodestring('%s:%s' % (api_key, api_secretkey))[:-1]
	return {'Authorization' : 'Basic %s' % base64string, 'Content-Type' : 'application/json'}

def setHTTPHeaders():
	"""
	If AWS requires authentication provide the key
	"""
	if os.environ['UBERTOOL_REST_SERVER'] == 'http://54.83.18.251:80':
		http_headers = auth_check()
	elif os.environ['UBERTOOL_REST_SERVER'] == 'http://localhost:80':
		http_headers = auth_check()
	else:
		http_headers = {'Content-Type' : 'application/json'}

	return http_headers
