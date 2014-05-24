#this is used on windows
#sys.argv[1] is the source directory
#sys.argv[2]  is the list need to copy
#sys.argv[3] is where you want to copy to

import os
import sys

dir_name= sys.argv[1]
os.system('dir /b/s ' + dir_name + ' > dir_list')
f =  file("dir_list", 'r')
all_list = f.read().lower()
f.close()
os.system('del dir_list')
lines = all_list.split('\n')

need_copy =  file(sys.argv[2], 'r').read().split('\n')
dest=sys.argv[3]
for nc in need_copy:
    if len(nc) > 0:
        need_copy = nc.lower()
        index = all_list.find(need_copy)
        if index == -1:
                print "can not find " + need_copy
        else:
                for line in lines:
                        ind =  line.find(need_copy)
                        if not ind == -1:
                                os.system("copy " + line + ' ' + dest)

