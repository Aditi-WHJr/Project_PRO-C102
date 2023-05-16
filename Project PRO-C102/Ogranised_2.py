import os
import shutil

# .exe , .msi,  .gif, .png .jpg, .jpeg, .csv, .pdf , .xls , .xlsx , .ppt , .pptx

from_dir = "C:/Users/lenovo/Downloads"
to_dir = "C:/Users/lenovo/OneDrive/Desktop/Document_Files"

list_of_files = os.listdir(from_dir)
print(list_of_files)

# Move All Image files from Downloads Folder to Another Folder
for file_name in list_of_files:

    name, extension = os.path.splitext(file_name)
    

    if extension == '':
        continue
    if extension in ['.txt', '.pdf', '.doc', '.docx']:

        path_1 = from_dir + '/' + file_name                               
        path_2 = to_dir + '/' + "Document_Files"                           
        path_3 = to_dir + '/' + "Document_Files" + '/' + file_name   
        #print("path1 " , path1)
        #print("path3 ", path3)

        
        if os.path.exists(path_2):
          print("Moving " + file_name + ".....")

          # Move from path1 => path3
          shutil.move(path_1, path_3)

        else:
          os.makedirs(path_2)
          print("Moving " + file_name + ".....")
          shutil.move(path_1, path_3)

        