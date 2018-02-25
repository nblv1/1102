#for key, value in os.environ.items():
#print(key, '--->', value)

import os

dir_name = "temp"
#os.mkdir(dir_name)

INITHIAL_PATH = os.path.abspath('.')
temp_dir = dir_name + os.sep
print(INITHIAL_PATH)

#with open(dir_name + os.sep + 'file1.txt', 'w'):
 #   pass
#with open(dir_name + os.sep + 'file2.txt', 'w'):
 #   pass

#os.chdir(temp_dir)
print(os.path.abspath('.'))

os.remove(temp_dir)