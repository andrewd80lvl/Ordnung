from genericpath import isdir
from importlib.resources import path
import os
import sqlite3
import getexif
import archive

#Каталог из которого будем брать файлы
root_directory = 'E:\\temp'

def get_file_dir(path_dir):
 
    #Получаем список файлов в переменную 
    files = os.listdir(path_dir)
      
    for file in files:

        path = os.path.join(path_dir,file)
        
        if(os.path.isdir(path)):
            get_file_dir(path)
        else:
            ret = getexif.get_exif_data(path)
            
            #Если найдены exif данные
            if(ret['return']):
                archive.copy_to_archive(path,ret)
            else:
                print(ret['error'])    
                
    
get_file_dir(root_directory)