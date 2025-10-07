# write to file
outfile = open('sample.txt','w')
outfile.write('Python is fun to learn.\n')
outfile.write('Write another line.\n')
outfile.close()



# append to file
outfile = open('sample.txt','a')
outfile.write('Using append to add a line.\n')
outfile.close()



# read from file using read()
print(f'\nRead file using read():')
infile = open('sample.txt','r')
contents = infile.read()
print(contents)
infile.close()


# read from file using readlines()
print(f'\nRead file using readlines():')
infile = open('sample.txt','r')
lines = infile.readlines()
for line in lines:
    print(line.strip('\n'))
infile.close()



# read from file using readline()
print(f'\nRead file using readline():')
infile = open('sample.txt','r')
line = infile.readline()
while  line:
    print(line.strip('\n'))
    line = infile.readline()

#infile.close()
    
# read from file using readline() for loop
print(f'\nRead file using for loop:')
infile.seek(0) # move the cursor to the beginning of the file
for line in infile:
    print(line.strip('\n'))
infile.close()



# using with to read/write file   
print(f'\nDisplay file contents using with:')
with open('sample.txt','a') as outfile:
    outfile.write('Add line using with open.\n')
with open('sample.txt','r') as infile:
    for line in infile:
        print(line.strip('\n'))

   
# write to binary file
print(f'\nRead from binary file:')
lst = [num for num in range(10)]
import pickle as pk
with open('sample.dat','wb') as bin_file:
    pk.dump(lst,bin_file)

# read from binary file
with open('sample.dat','rb') as bin_file:
    data = pk.load(bin_file)

print(f'\nRead from binary file:')
print(data)


# read jason file using nasa open api
# You might get the following error:
#[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1028)
# Locate Python 3.13 (or other version) folder and run Install Certificates.command to fix the issue.

import urllib.request
import urllib.error
import json

try:
    url = 'https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY'
    with urllib.request.urlopen(url) as infile:
        data = json.load(infile)
    
    print(data)

except urllib.error.URLError as e:
    print(e.reason)
except urllib.error.HTTPError as e:
    print(e.code)
except json.JSONDecodeError as e:
    print(e.msg)
