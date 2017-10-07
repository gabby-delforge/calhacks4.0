import struct 
import matplotlib
import io


def convert(imgs, labels):
	#Remove header
	
	with open(imgs, 'rb') as openfile:
		header = openfile.read(4)
		header = struct.unpack("i", header)
		num_images = openfile.read(4)
		num_images = struct.unpack("i", num_images)
	print(num_images)
	#num_imgs = 
	#num_rows = 
	#num_cols = 

	#Splice imgs
	#Returns a list of lists, num_imgs long
	imgs_list = splice_imgs(imgs)

	#Splice labels
	#Returns a list of labels, num_imgs long
	labels_list = splice_labels(labels)

	#Merge into correct format
	#merged = 
	
	#return merged 


"""returns a list of lists where each nested list contains all the pixel values
for a particular image"""
def splice_imgs(img_file):
	result = []
	#make the file into a stream of bytes
	pixels_stream = open(img_file, 'rb')
	pixels_stream.read(4)
	pixels_stream.read(4)
	pixels_stream.read(4)
	pixels_stream.read(4)
	count = 1
	while len(result) < 10000:
		num_pixels = 0
		img_pixels = []
		while num_pixels < 784:
			_next = pixels_stream.read(1)
			pixel = struct.unpack("B", _next)
			print(pixel[0])
			img_pixels.append(pixel[0])

			num_pixels += 1
		print("i've reached the end of image " + str(count) + "!")
		count += 1
		result.append(img_pixels)
	return result



"""returns a list of integers where each integer matches with the number to be
read from the corresponding image"""
def splice_labels(labels_file):
	result = []
	labels_stream = open(labels_file)
	labels_stream.read(4)
	labels_stream.read(4)
	while len(result) < 60000:
		_next = labels_stream.read(1)
		label = struct.unpack("B", _next)
		print(label[0])
		result.append(label[0])
	return result





#DESIRED OUTPUT:
#List of tuples, each tuple containing a list of pixel values and a label
#[([1, 2, 3, 4], 5), ([1, 2, 3, 4], 5), ([1, 2, 3, 4], 5)]