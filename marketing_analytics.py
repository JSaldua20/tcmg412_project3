import os
import urllib.request

FilePath = './http_access_log.txt'
FileExists = os.path.exists(FilePath)

if FileExists == False:
  print("You don't seem to have the data, downloading it now")
  url = "https://s3.amazonaws.com/tcmg476/http_access_log"
  urllib.request.urlretrieve(url, FilePath)
  
else:
  print ("It looks like you already have the file")

print ("Reviewing the data now")
TextFile = open("http_access_log.txt")
Log = TextFile.read()
LastYearCount = Log.count("1995")
print("Number of accsesses from 1995:", LastYearCount)
FirstYearCount = Log.count("1994")
print("Number of accsesses from 1994 and 1995:", FirstYearCount + LastYearCount)
