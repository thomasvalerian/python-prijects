import os
import posixpath
import sys

if len(sys.argv) == 4:
  dirPath = sys.argv[1] #'./2137_barista_cafe/'
  frmExt = sys.argv[2] #'js'
  toExt = sys.argv[3] #'jscript'

  if posixpath.isdir(dirPath):

    for item in os.walk(dirPath):
        #print(item)
        curDir,subDires,subFiles = item
        #print(curDir,subFiles)
        for subFil in subFiles:
            #print(subFil)
            #print(posixpath.join(curDir,subFil))
            absPath = posixpath.join(curDir,subFil)
            if absPath.endswith(frmExt):
                #print(absPath)
                print('----------###----------')
                #print(posixpath.splitext(absPath))
                file,ext = posixpath.splitext(absPath)
                destFilName = f"{file}.{toExt.lstrip('.')}"
                #print(absPath,destFilName)
                os.rename(absPath,destFilName)
  else:
      print(f'given path ( {dirPath} ) is not a dir')
        #break
else:
    print(f"Error  usage: python3 extChanger.py dir_name from_extension toExtension)
