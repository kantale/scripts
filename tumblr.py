"""

Copyright (c) 2013, Alexandros Kanterakis, alexandros.kanterakis@gmail.com
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met: 

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer. 
2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution. 

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

The views and conclusions contained in the software and documentation are those
of the authors and should not be interpreted as representing official policies, 
either expressed or implied, of the FreeBSD Project.

"""

"""

Safe in a file pw.py:

pw = {
	'CONSUMER_KEY' : 'API_KEY',
	'CONSUMER_SECRET' : 'SECRET_KEY',
	'oauth_callback' : 'A callback URL', # You should be able to read the posted values. A possible value: www.microsoft.com/callback , don't overuse ;)
}


"""

import urllib
import urllib2
import oauth2
import pickle
import time
import json

import urlparse

def fetch_page(url, verbose = False):
	if verbose:
		print "Fetching: " + url
	try:
		fp = urllib2.urlopen(url)
		ret = fp.read()
		fp.close()
	except urllib2.HTTPError:
		print '   FAIL import'
		ret = ''

	return ret


def fetch_content(url, values, verbose=False):
	data = urllib.urlencode(values)

	request_url = '%s?%s' % (url, data)

	return fetch_page(request_url, verbose=verbose)

def fetch_dict(url, values, verbose=False):
	content = fetch_content(url, values, verbose=verbose)
	return json.loads(content)

def fetch_json(url, values, indent=4, verbose=False):
	content = fetch_dict(url, values, verbose=verbose)

	return json.dumps(content, indent)

def request(blogname, values, path=0, use_oauth = False, apply=lambda x : x, verbose=False):

	from pw import pw

	url = 'http://api.tumblr.com/v2/blog/%s/posts' % (blogname)
	api_key = pw['CONSUMER_KEY']
	
	new_values = {'api_key' : api_key}
	for key in values:
		new_values[key] = values[key]

	if use_oauth:
		oauth_parameters = get_oauth_parameters(blogname, values, verbose=verbose)
		for key in oauth_parameters:
			new_values[key] = oauth_parameters[key]

	content = fetch_dict(url, new_values, verbose=verbose)
	tmp_content = content

	for x in path:
		tmp_content = tmp_content[x]
	return apply(tmp_content)

def get_all_posts(blogname, use_oauth = False, verbose = False):
	posts = get_posts_number(blogname, use_oauth, verbose=verbose)

	ret = []

	for banch in range(0, posts, 20):
		values = {'offset': banch, 'limit':20}

		ret += request(blogname, values, path = ['response', 'posts'], use_oauth=use_oauth, verbose=verbose)

	ret.reverse()
	return ret

def get_posts_number(blogname, use_oauth=False, verbose=False):
	values = {'limit' : 1}

	return request(blogname, values, path = ['response', 'total_posts'], apply = lambda x:int(x), use_oauth = use_oauth, verbose=verbose)

def save_posts_to_file(blogname, filename, use_oauth=False, verbose=False):
	all_posts = get_all_posts(blogname, use_oauth, verbose=verbose)

	fp = open(filename, 'w')
	pickle.dump(all_posts, fp)
	fp.close()

def get_oauth_access_tokens():

	from pw import pw	

	REQUEST_TOKEN_URL = 'http://www.tumblr.com/oauth/request_token'
	AUTHORIZATION_URL = 'http://www.tumblr.com/oauth/authorize'
	ACCESS_TOKEN_URL = 'http://www.tumblr.com/oauth/access_token'
	CONSUMER_KEY = pw['CONSUMER_KEY']
	CONSUMER_SECRET = pw['CONSUMER_SECRET']

	consumer = oauth2.Consumer(CONSUMER_KEY, CONSUMER_SECRET)
	client = oauth2.Client(consumer)

	resp, content = client.request(REQUEST_TOKEN_URL, "GET")

	request_token = dict(urlparse.parse_qsl(content))

	print "Request Token:"
	print "    - oauth_token        = %s" % request_token['oauth_token']
	print "    - oauth_token_secret = %s" % request_token['oauth_token_secret']

	oauth_callback = pw['oauth_callback']

	goto_url = '%s?oauth_token=%s&oauth_callback=%s' % (AUTHORIZATION_URL, request_token['oauth_token'], oauth_callback)

	print "Goto: ", goto_url
	oauth_verifier = raw_input('What is the PIN? ')

	token = oauth2.Token(request_token['oauth_token'], request_token['oauth_token_secret'])
	token.set_verifier(oauth_verifier)
	client = oauth2.Client(consumer, token)

	resp, content = client.request(ACCESS_TOKEN_URL, "POST")
	access_token = dict(urlparse.parse_qsl(content))

	print "Access Token:"
	print "    - oauth_token        = %s" % access_token['oauth_token']
	print "    - oauth_token_secret = %s" % access_token['oauth_token_secret']
	print

	print "Save these values to pw['access_oauth_token'] and pw['access_oauth_token_secret']"

	return access_token

def get_oauth_parameters(blogname, api_parameters, verbose=False):

	from pw import pw

	access_token = get_oauth_access_tokens()


	CONSUMER_KEY = pw['CONSUMER_KEY']
	CONSUMER_SECRET = pw['CONSUMER_SECRET']

	oauth_token = access_token['oauth_token']
	oauth_token_secret = access_token['oauth_token_secret']

	api_key = pw['CONSUMER_KEY']

	token = oauth2.Token(key=oauth_token, secret=oauth_token_secret)
	consumer = oauth2.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)

	params = {
		'oauth_consumer_key' : consumer.key,
		'oauth_token' : token.key,
		'oauth_signature_method' : 'HMAC-SHA1',
		'oauth_timestamp': int(time.time()),
		'oauth_nonce': oauth2.generate_nonce(),
	 	'oauth_version': '1.0',
	}

	url = 'http://api.tumblr.com/v2/blog/%s/posts?api_key=%s&%s' % (blogname, api_key, urllib.urlencode(api_parameters))
	if verbose:
		print 'Seeking authentication for: %s' % (url)

	req = oauth2.Request(method="GET", url=url, parameters=params)

	signature_method = oauth2.SignatureMethod_HMAC_SHA1()
	req.sign_request(signature_method, consumer, token)

	return req

if __name__ == '__main__':

	#Example:
	#save_posts_to_file('my_public_blog.tumblr.com', 'my_public_blog_backup.txt')
	#save_posts_to_file('my_private_blog.tumblr.com', 'my_private_blog_backup.txt', use_oauth=True)

	pass