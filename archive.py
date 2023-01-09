import os

#Каталог архива
archive_directory = "E:\\PhotoArchive"

def copy_to_archive(path_source,photo_info):

    #Проверка копируемого фото в архиве
    path_dir = os.path.join(archive_directory,photo_info['year'],photo_info['month'],photo_info['day'])

    print(path_dir)

    #Проверка директории в архиве
    if not os.path.isdir(path_dir):
        os.makedirs(path_dir)

    path_file = os.path.join(path_dir,photo_info["file_name"])

    if(os.path.exists(path_file)):
        #Файл есть в архиве, удаляем файл из папки "разбора"
        os.remove(path_source)
        
        print("Фотография уже есть в архиве, удаляем из исходной папки: " + path_source)

    else:
        #Файла нет в архиве, переносим в архив
        os.replace(path_source,path_file)
        print("Переносим фотографию  в архив: " + path_source)

    

    return 
