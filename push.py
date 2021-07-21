import subprocess
import os
import datetime

if __name__ == "__main__":
	result = subprocess.call(["git", "stage", "."])
	if result != 0:
		print("failed to stage with code", result)
		exit(result)
	result = subprocess.call(["git", "commit", "-m", datetime.datetime.now().strftime("automatic update %Y-%m-%d %H:%M")])
	if result != 0:
		print("failed to commit with code", result)
		exit(result)
	# result = subprocess.call(["git", "push"])
	# if result != 0:
	# 	print("failed to push with code", result)
	# 	exit(result)

	