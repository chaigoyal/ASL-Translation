from os import listdir
import os
import random
import shutil
from skimage.transform import resize
from scipy import misc
from glob import glob
from PIL import Image, ImageOps
import string

class ImageDataset():
	def __init__(self, batch_size, height, width, data_directory):
		self.data_dir = data_directory
		self.batch_size = batch_size
		self.height = height
		self.width = width 
		self.filename_dict = {}

		# Enters filenames into a dictionary based off of the uppercase letter
		# 	ex. 'A' -> {'A0001_train.jpg', 'A0002_train.jpg',...}
		for letter in list(string.ascii_uppercase):
			self.filename_dict[letter] = glob(os.path.join(self.data_dir, letter, '*.jpg'))
		#self.data = #get data from the directory 
		#self.labels = #extract the labels from the data 
	
	#yield the next batch 
	def get_next_batch(self):
		yield batch_x, batch_y

	#resize the images so that they are all the same dimensions
	def resize_images(self):
		os.mkdir('standard_data')
		for letter in list(string.ascii_uppercase):
			os.mkdir('standard_data/' + letter)
			for filename in self.filename_dict[letter]:
				self.load_image(filename)

	#writes resized images to new directory
	def load_image(self, filename):
		letter, name = filename.split('/')[1:3]
		image = misc.imread(filename)
		image = resize(image, (self.height, self.width))
		misc.imsave(os.path.join('standard_data', letter, name), image)

	#randomly scale and rotate the images and add these new images to the dataset
	def augment_data(self):




			


