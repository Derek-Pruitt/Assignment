# Author    Derek J Pruitt

# Python    3.8.3


import os
import time

modificationTime = os.path.getmtime("\python_projects\Assignment\PythonAssignment")

local_time = time.ctime(modificationTime)

for file in os.listdir("\python_projects\Assignment\PythonAssignment"):
    if file.endswith(".txt"):
        print(os.path.join("\python_projects\Assignment\PythonAssignment", file))
        print('Last modification time(Local Time):', local_time)


