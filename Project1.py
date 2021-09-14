# IMPORTING OS & SHUTIL FOR BETTER FOLDER MANAGEMENT
import os,shutil

# CREATING DICTIONARY CONSISTING OF EXTENSION NAMES & TYPES
dict_extension = {
	'audio_extension' : ('.mp3','.m4a','.wav','.flac','.MP3'),
	'video_extension' : ('.mp4','.mkv','.MKV','.flv','.mpeg','.ts'),
	'document_extension' : ('.doc','.pdf','.txt','.PDF'),
	'image_extension' : ('.jpg','jpeg','.png')
}

# GIVEN SOURCE & RESULTANT FOLDER LOCATION 
folderpath = input("Enter folder location : ")

# FUNCTION FOR FILE CLASSIFICATION & ENLISTING BASED ON EXTENSION TYPE
def file_type(folderpath,file_extension):
	file=[]
	for items in os.listdir(folderpath):
		for files in file_extension:
			if items.endswith(files):
				file.append(items)
	return file
	
	#list comprehension (CHOICE)
	return [items for items in os.listdir(folderpath) for files in file_extension if items.endswith(files)]
	

# CREATING FOLDERS & MOVING DIFFERENT EXTENSIONS BY REASSIGNING PATH 
for extension_type,extension_tuple in dict_extension.items():
	folder_name=extension_type.split("_")[0].title()
	folder_path = os.path.join(folderpath,folder_name)
	if os.path.exists(folder_path):
		pass
	else:
		if len(file_type(folderpath,extension_tuple)) > 0:
			os.mkdir(folder_path)
	for item in file_type(folderpath,extension_tuple):
		item_path=os.path.join(folderpath,item)
		item_new_path=os.path.join(folder_path,item)
		shutil.move(item_path,item_new_path)