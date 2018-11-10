
class ImageDataset():
	def __init__(self, num_batches, height, width):
		self.num_batches = num_batches
		self.height = height
		self.width = width 
		self.data = #get data from the directory 
		self.labels = #extract the labels from the data 
	
	#yield the next batch 
	def get_next_batch(self):
		yield batch_x, batch_y

	#resize the image so that they are all the same dimensions
	def standardize(self):


	#randomly scale and rotate the images and add these new images to the dataset
	def augment_data(self):

