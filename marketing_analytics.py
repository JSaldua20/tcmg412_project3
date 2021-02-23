import os
import urllib.request

FilePath = './http_access_log.txt'
FileExists = os.path.exists(FilePath)

if FileExists == False:
  print("You don't seem to have the data, downloading it now")
  url = "https://s3.amazonaws.com/tcmg476/http_access_log"
  urllib.request.urlretrieve(url, FilePath)
  
