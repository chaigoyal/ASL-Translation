
from os import listdir
import os
import random
import shutil
from skimage.transform import resize
from scipy import misc
from glob import glob
from PIL import Image, ImageOps
import string

def add_stanfordfiles_to_directory(num_files):
	
	
	aug_data_dir = '/Users/rahuldesai/LocalDocs/Projects/ASL-Translation/ASL-Datasets/new_data'
	directory = '/Users/rahuldesai/LocalDocs/Projects/ASL-Translation/ASL-Datasets/Stanford/E'
	
	for folder in listdir(directory):

		count = 1
		index = 0
		indices = []
		last_value = 0
		print(folder)
		
		if folder.capitalize() not in listdir(aug_data_dir):
			os.mkdir(aug_data_dir + '/' + folder.capitalize())
		else:
			sorted_list = listdir(aug_data_dir + '/' + folder.capitalize())
			sorted_list.sort(key=lambda x: int(x.split("_")[0][1:]))
			last = sorted_list[-1]
			last_value = int(last.split("_")[0][1:]) 
		
		folder_dir = directory + '/' + folder
		filenames = listdir(folder_dir)
		
		while count <= num_files:
			index = random.randint(0, len(filenames) - 1)
			
			if index not in indices:
				indices.append(index)
				if filenames[index].split("_")[0] == "color":
					file_name = folder.capitalize() + str(count + last_value) + '_train.jpg'
					
					old_path = folder_dir + '/' + filenames[index]
					new_path = aug_data_dir + '/' + folder.capitalize() + '/' + file_name

					shutil.copy(old_path, new_path)
					count += 1
		
	
	print('Done.')

def train_test_split(test_split):

	data_dir = '/Users/rahuldesai/LocalDocs/Projects/ASL-Translation/ASL-Datasets/Final_Dataset'
	
	train_dir = '/Users/rahuldesai/LocalDocs/Projects/ASL-Translation/ASL-Datasets/train_data'
	test_dir = '/Users/rahuldesai/LocalDocs/Projects/ASL-Translation/ASL-Datasets/test_data'
	
	folders = [f for f in listdir(data_dir) if not f.startswith('.')]

	for folder in folders:

		print(folder)

		folder_dir = data_dir + '/' + folder

		if folder not in listdir(train_dir):
			os.mkdir(train_dir + '/' + folder)

		if folder not in listdir(test_dir):
			os.mkdir(test_dir + '/' + folder)

		files = listdir(folder_dir)
		
		test_count = int(len(files) * test_split)
		train_count = int(len(files) * (1 - test_split))

		assert abs((test_count + train_count) - len(files)) <= 1, "Train {0} and test {1} data was not split correctly. Should sum to {2}".format(test_count, train_count, len(files))

		indices = []
		count = 0

		while count <= test_count:
			index = random.randint(0, len(files) - 1)
			if index not in indices:
				indices.append(index)
				
				old_path = folder_dir + '/' + files[index]
				new_path = test_dir + '/' + folder + '/' + files[index]
				shutil.copy(old_path, new_path)
				
				count += 1

		count = 0 
		print("Start Training")

		while count <=  train_count:
			index = random.randint(0, len(files) - 1)
			if index not in indices:
				indices.append(index)
				
				old_path = folder_dir + '/' + files[index]
				new_path = train_dir + '/' + folder + '/' + files[index]
				shutil.copy(old_path, new_path)
				
				count += 1
			elif len(indices) == len(files):
				break
		print("Done.")


def add_kagglefiles_to_directory(num_files):
	
	
	aug_data_dir = '/Users/rahuldesai/LocalDocs/Projects/ASL-Translation/ASL-Datasets/new_data'
	directory = '/Users/rahuldesai/LocalDocs/Projects/ASL-Translation/ASL-Datasets/Kaggle100'
	
	for folder in listdir(directory):

		count = 1
		index = 0
		indices = []
		last_value = 0
		print(folder)
		
		if folder.capitalize() not in listdir(aug_data_dir):
			os.mkdir(aug_data_dir + '/' + folder.capitalize())
		else:
			sorted_list = listdir(aug_data_dir + '/' + folder.capitalize())
			sorted_list.sort(key=lambda x: int(x.split("_")[0][1:]))
			last = sorted_list[-1]
			last_value = int(last.split("_")[0][1:]) 
		
		folder_dir = directory + '/' + folder
		filenames = listdir(folder_dir)
		
		while count <= num_files:
			index = random.randint(0, len(filenames) - 1)
			
			if index not in indices:
				indices.append(index)
				file_name = folder.capitalize() + str(count + last_value) + '_train.jpg'
					
				old_path = folder_dir + '/' + filenames[index]
				new_path = aug_data_dir + '/' + folder.capitalize() + '/' + file_name

				shutil.copy(old_path, new_path)
				count += 1	
	
	print('Done.')