from search import *
from searchhistorydb import *

# this will return a tuple of root and extension
split_tup = os.path.splitext(filename)
print(split_tup)

# extract the file name and extension
FILENAME = split_tup[0]
fileextension = split_tup[1]

print("File Name: ", FILENAME)
print("File Extension: ", fileextension)


