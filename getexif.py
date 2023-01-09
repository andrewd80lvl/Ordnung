import os
from exif import Image

def build_file_name(path,file_name):
    
    new_file_name = "";
    extension = path.rsplit('.',1)

    size =  os.path.getsize(path) # Получаем размер фотографии
    
    if(len(extension) == 2):
        new_file_name = file_name + "_" + str(size) + '.' + extension[1]

    return new_file_name


def exec_exif_data(date_time):

    ret = dict()

    str = date_time.replace(' ',':')    #Заменяем пробел на ':'

    t_list = str.split(':',3)
                
    ret['year'] = t_list[0]     # Год фотографии
    ret['month'] = t_list[1]    # Месяц фотографии    
    ret['day'] = t_list[2]      # День фотографии    

    str = str.replace(':','_')    # Заменяем в имени файла из имени файла 
    
    ret['file_name'] = str

    return ret

def get_exif_data(path):

    file_info = dict(); 
  
    try:
        with open(path, 'rb') as image_file:
            my_image = Image(image_file)
            
            if(my_image.has_exif):

                file_info['return'] = True
                file_info['datetime'] = my_image.get("datetime")
                file_info['model'] = my_image.get("model")

                file_info.update(exec_exif_data(my_image.get("datetime")))
                
                str = build_file_name(path,file_info["file_name"])
                if(len(str) != 0):
                    file_info["file_name"] = str
                else:
                    file_info['return'] = False
                    file_info['error'] = 'Ошибка получения расширения файла:' + path
                
            else:
                file_info['return'] = False
                file_info['error'] = 'Ошибка получения exif данных файла:' + path
           
            return file_info
           
    except Exception:
        
         file_info['return'] = False
         file_info['error'] = 'Ошибка получения exif данных файла:' + path
         return file_info
  
    finally:
         image_file.close()
 
                