
# -*- coding:utf-8 -*-

import os
import json
import shutil 

jsonT = {
  "images" : [
    {
      "idiom" : "universal",
      "filename" : "test@2x.png",
      "scale" : "2x"
    },
    {
      "idiom" : "universal",
      "filename" : "test@3x.png",
      "scale" : "3x"
    }
  ],
  "info" : {
    "version" : 1,
    "author" : "xcode"
  }
}


def createJson():
    json_str = json.dumps(jsonT)
    return json_str

print createJson()



# os.mknod("testaaa.txt") 
# fp = open("Contents.json",'w')
# fp.writelines(createJson())  
# fp.close()    

newFile = "Content.json"
dirname = 'icon/'+ newFile

shutil.copyfile("sample.json",newFile)



# shutil.move(newFile,dirname)


def store(data):
    with open(newFile, 'w') as json_file:
        json_file.write(json.dumps(data))

def load():
    with open(newFile) as json_file:
        data = json.load(json_file)
        return data

if __name__ == "__main__":

    data = load()
    
    for index in range(len(data)):
          data["images"][index]["filename"] = "test name"+ "@"+data["images"][index]["scale"]+".png"
    store(data)

    print data["images"]