#!/usr/bin/env python3
# Import additional Modules required
import shutil
import os

#Change directory to our working directory
os.chdir("/home/student/mycode/")

#Copy files to a backup with the .copy extn
shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")
#Copy directory to a backup
shutil.copytree("5g_research/", "5g_research_backup/")

