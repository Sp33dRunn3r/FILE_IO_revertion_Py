##FILE I/O

my_file = open('test.txt', mode='r') # Read only
my_file = open('test.txt', mode='r+') # Read and write
my_file = open('test.txt', mode='w') # Write only
my_file = open('test.txt', mode='a') # Append

print(my_file.read()) # read the file
print(my_file.readline()) # read a single line
print(my_file.readlines()) # read all lines

my_file.close() # Manually close the file

with open('test.txt') as my_file: # More efficient file closing
    print(my_file.readlines())
