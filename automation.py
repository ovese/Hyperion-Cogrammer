# create a an ideal file structure
# source folder at top level
# have source_file.py, main.py,.gitignore,readme.md, and
# requirements.txt
# models, routes, services, app.py

# open the main.py file

import os # helps us to get our files
import typing
from typing import List

# we need somethiung to store out file structure
# use a dictionany data structure to do this
file_struct = {
"src/":{
	"models/": None,
	"routes/": None,
	"serives/": None,
	"app.py": None
	},
	".gitignore": None,
	"dockerfile": None,
	"main.py": None,
	"readme.md": None,
	"requirements.txt": None
}

def create_filder(path: str, folder_path: str):
	os.mfdir(f'{path}/{folder_path}')

# use try-except to see if file exsists
def create_filder(path: str, folder_path: str):
	folder_path = f'{path}/{folder_path}'

	if(os.path.exists(folder_path)):
		return
	
	os.mkdir(folder_path)

def create_file(path: str, file_name: str):
 	with openm(f'{path}/{file_name}','w') as file:
	file.write("")

def generate_folder_structure(path: str, struct_dict: dict):
	# using recursion hgere
	for key in struct_dict:
		if(struct_dict[key] ==None):
			# generate or create the file
			...
		else:
		# if the if is negated or not true do this
		# vreate the file by calling the function itself
		# thats recursion
		generate_folder_structure(f'{path}/{key}', struct_duict[key])

def generate_structure(path: str, name: str):
	# we need to know if its a fodler or a file
	if name[-1] =='/':
		create_folder(path,name)
	else:
		create_file(path, name)

if __name__ ='__main__':
	# create_file('.',test.py')
	generate_file_structure('.', file_struct)



# web scraping can be done in python using selenium
