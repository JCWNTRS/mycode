#!/usr/bin/env python3
#Import useful modules
import shutil
import os
#Change to working directory
os.chdir('/home/student/mycode/')
#Move raynor.obj to ceph_storage
shutil.move('raynor.obj', 'ceph_storage/')
#Request new filename for kerrigan.obj
xname = input('What is the new name for kerrigan.obj? ')
#Move and rename kerrigan.obj to ceph_storage
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)
