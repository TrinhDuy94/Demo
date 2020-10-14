import wget, os
from os import path

file = input("File name: ")
url = input("URL: ")
local = input("LOCAL: ")
try:
	if(path.exists(local+"/"+file)==True):
		os.remove(local+"/"+file)
		wget.download(url,local)
	else:
		wget.download(url,local)
	print("Done!")
except:
	print("Failed")