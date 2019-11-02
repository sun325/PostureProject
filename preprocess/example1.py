#Following is an example of how to create a robust function for preprocessing images.
#Things to add in this file: Classes and Other opertaions.
#Please add how will you handle classes as well, before moving forward.
#Data consists of two part, label and image. We need to save label as well. 

def preprocess_images(IMAGE_FOLDER="", OPT_FILE=""):
	#To store all the data in list, we can convert this list into numpy array and store it later on.
	DATA = []
	for fname in os.listdir(IMAGE_FOLDER):
		#Read the content of the image file
		img = cv2.imread(os.path.join(path_train,fname))
		#Exception handling: If img is none than the file may not be image file
		if img is not None:
			#All preprocessing should be here
			#Do not load any libraries here
			#Please use the variable name 'img' for input and output of all preprocessing tasks. Until it becomes necessary
			#Convert the image to grey scale
			img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
			#Write the convertedimage to the output directory
			DATA.append(img)
	DATA = np.array(DATA)
	np.save(OPT_FILE)
