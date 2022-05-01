# importing packages
import requests
from bs4 import BeautifulSoup
import os
import time

# Creating the directory
response = input("Do you want to store the file in the same directory(Y) or different directory(N): ")
if response == "Y" or response == "y":
    directory = input("Enter the folder name: ")
    try:
        path = os.mkdir(os.path.join(os.getcwd(), directory))
        os.chdir(os.path.join(os.getcwd(), directory))
    except OSError:
        print("Directory already created")
        os.chdir(os.path.join(os.getcwd(), directory))
    else:
        print("Successfully created the directory")
elif response == "N" or response == "n":
    directory = input("Enter the directory: ")
    access_rights = 0o755
    try:
        os.mkdir(directory, access_rights)
        os.chdir(directory)
    except OSError:
        print("Directory already created")
        os.chdir(directory)
    else:
        print("Successfully created the directory")
else:
    print("Wrong input")

# URL
url = "https://this-person-does-not-exist.com/en"

# Creating the starting and ending variable
print("Please keep the numbers in the order of thousands(1000s) ")
cur_dir = os.getcwd()
os.mkdir(os.path.join(os.getcwd(), 'Profile_pic_' + '1'))
os.chdir(os.path.join(os.getcwd(), 'Profile_pic_' + '1'))
# Whole part below this will be run in a loop
count = 1
initial_time = time.time()
for i in range(1, 1001):
    # Giving request to the url
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    # Searching the image with the id name
    images = soup.find(id='avatar')
    u = "https://this-person-does-not-exist.com"
    s = str(images['src'])
    name = u + s
    # Downloading and saving the file
    with open(str(i) + '.jpg', 'wb') as f:
        im = requests.get(name)
        f.write(im.content)
    print(count, ' file sent')
    r.close()
    count += 1
print("1000 files sent. Time Taken= ", time.time() - initial_time)
