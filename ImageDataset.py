from os import listdir
import os
import random
import shutil

class ImageDataset():
	def __init__(self, batch_size, height, width, data_directory):
		self.batch_size = batch_size
		self.height = height
		self.width = width 
		#self.data = #get data from the directory 
		#self.labels = #extract the labels from the data 
	
	#yield the next batch 
	def get_next_batch(self):
		yield batch_x, batch_y

	#resize the image so that they are all the same dimensions
	def resize_image(self):



def add_files_to_directory(num_files):
	
	count = 1
	index = 0
	indices = []

	aug_data_dir = '/Users/rahuldesai/LocalDocs/Projects/ASL-Translation/ASL-Datasets/aug_dataset'
	directory = '/Users/rahuldesai/LocalDocs/Projects/ASL-Translation/ASL-Datasets/asl_alphabet_train'
	
	for folder in listdir(directory):
		print(folder)
		if folder not in listdir(aug_data_dir):
			os.mkdir(aug_data_dir + '/' + folder)
		else:
			sorted_list = listdir(aug_data_dir + '/' + folder)
			sorted_list.sort()
			last = sorted_list[-1]
			last_value = int(last[1:5])
		
		folder_dir = directory + '/' + folder
		filenames = listdir(folder_dir)
		
		while count <= num_files:
			index = random.randint(0, len(filenames) - 1)
			
			if index not in indices:
				indices.append(index)

				file_name = folder + str(last_value + count) + '_train.jpg'
				
				old_path = folder_dir + '/' + filenames[index]
				new_path = aug_data_dir + '/' + folder + '/' + file_name

				shutil.copy(old_path, new_path)
				count += 1
		
		count = 1
		indices = []
	
	print('Done.')

			


