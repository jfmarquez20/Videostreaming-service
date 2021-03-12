import numpy as np
import cv2
import dropbox
from dropbox.files import WriteMode
import os
from glob import iglob
import sys

def send(name):
	access_token = 'argujKJ8vYAAAAAAAAAADEVUqK7tGG98eoOgIARge4QG_ssu8A44phq0rYPbZWLs'   #User token
	dbx = dropbox.Dropbox(access_token)
	print ('Linked account: ', dbx.users_get_current_account())
	cwd_dir = os.getcwd()
	record = name

	for filename in iglob(os.path.join(cwd_dir, record)):
		print filename
		try:
			file = open(filename, 'rb')
			backuppath = "/" + record 
			response = dbx.files_upload(file.read(), backuppath, mode=WriteMode('overwrite'))
			print "Recording has been uploaded succesfully:", response
			file.close()
			#os.remove(filename)
		except Exception, e:
			print ('Error %s' % e)