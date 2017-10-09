
# -*- coding:utf-8 -*-

import os
import json

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
fp = open("testss.txt",'w')
fp.writelines(createJson())  
fp.close()    