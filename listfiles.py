import os 
# directory/folder path
dir_path = r'C:\Users\Dell\rsna pneumonia\rsna-pneumonia-detection-challenge\Target_0NN_PNGs'

# list to store files
res = []
csv_text =""
# Iterate directory
for file_path in os.listdir(dir_path):
    # check if current file_path is a file
    if os.path.isfile(os.path.join(dir_path, file_path)):
        # add filename to list
        csv_text =csv_text+ file_path+"\n" 
# print()
f = open("file_name.csv", "a")
f.write(csv_text)
f.close()