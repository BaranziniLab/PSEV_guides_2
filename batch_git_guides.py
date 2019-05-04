import numpy as np
import subprocess
import pandas as pd

for i in range(0,10):
	files = 'shortest_path_DB*%s.html'% i
	subprocess.call(['git', 'commit', files, '-m', '"%s"'%i])
	subprocess.call(['git', 'push'])



