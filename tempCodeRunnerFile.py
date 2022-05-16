import urllib.request
import os
import shutil

#Step 0 : Create a list of urls of images
#CallLISTcreationscript(searchterm)


#Step 1 : Create folder + Download images from list into it

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

newpath = "ignoredspace/imgstobezipped/"



if not os.path.exists(BASE_DIR+"/"+newpath):
    print("Dir Created")
    os.makedirs(newpath)
else:
    print("already exists")

imgurl = "https://i.pinimg.com/originals/ca/54/62/ca5462afe308041935434a7b654fa364.jpg"
imgname = "downloadedpy"
imgtype = ".jpg"
urllib.request.urlretrieve(imgurl, newpath+imgname+imgtype)

#Step 2 : Zip the folder



foldername = "Ziparchx"
shutil.make_archive(foldername, 'zip', newpath)

#Step 3 : Contact bot to upload Zip to requesting user
#CallBOTscript(zipfoldername,messageid)




