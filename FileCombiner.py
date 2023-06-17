import os
from pathlib import Path

# Determine newline insterts + number of input files
print("## NOTE: the chosen output file may not also be an input file to avoid loss of data ##")
line_break, remove_old = -1, -1
count = 0
while line_break < 0 or line_break > 1:
	line_break = int(input("Do you want to insert new lines between each file's input? (0 or 1): "))
while remove_old < 0 or remove_old > 1:
	remove_old = int(input("Do you want to delete input files after combining? (0 or 1): "))
if count == 0 or int(count) != count:
	count = int(input("Enter the number of files to combine: "))

inputs = []
for i in range(count):
	prompt = "Name of file " + str(i+1) + " (with extension): "
	temp = input(prompt)
	inputs.append(temp)
output = input("Name of output file (with extension): ")

with open(output, 'w') as outfile:
	for word in inputs:
		outfile.write(open(word).read())
		if line_break:
			outfile.write("\n")
		if remove_old:
			remove_msg = "Do you want to remove " + word + " (0 or 1)? "
			temp = int(input(remove_msg))
			if temp:
				os.remove(word)

print("Write complete.")
output_size = os.path.getsize(output)
size_msg = "Size of " + str(output) + ": " + str(f"{output_size:,d}") + " bytes"
print(size_msg)
path_name = Path.cwd()
ps = 0
for path, dirs, files in os.walk(path_name):
	for f in files:
		ps += os.path.getsize(os.path.join(path, f))
path_size = int(str(ps))
path_msg = "Size of " + str(path_name) + ": " + str(f"{path_size:,d}") + " bytes"
print(path_msg)

