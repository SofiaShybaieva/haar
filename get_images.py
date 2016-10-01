import urllib2 as url
import cv2
import numpy as np
import os

def store_raw_images():
	if not os.path.exists('neg'):
		os.makedirs('neg')

	neg_images_link = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n09376198' # fish n02512053
	pic_num = 1

	neg_images_urls = url.urlopen(neg_images_link).read()

	for img_url in neg_images_urls.split('\n'):
		try:
			print 'retreiving ' + img_url + ' ...'
			file_name = 'neg/' + str(pic_num) + '.jpg'
			print file_name
			request = url.urlopen (img_url)
			
			with open(file_name, 'wb') as output:
				img_bytes = request.read()
				output.write (img_bytes)
			
			img = cv2.imread(file_name, cv2.IMREAD_GRAYSCALE)
			# should be larger than samples / pos pic (so we can place our image on it)
			resized_image = cv2.resize (img, (100,100))
			cv2.imwrite(file_name, resized_image)
			pic_num += 1
		except Exception as e:
			print str(e)


store_raw_images()