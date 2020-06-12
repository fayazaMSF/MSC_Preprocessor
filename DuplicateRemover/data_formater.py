# import os
# arr = os.listdir("C:\\Users\\ffayaza\\Documents\\Data\\PROJECT_DATA\\TEST_DATA\\formated_data\\October\\18102018")
# print(arr)
import glob

read_files = glob.glob("C:\\Users\\ffayaza\\Documents\\Data\\PROJECT_DATA\\TEST_DATA\\formated_data\\December\\03122018\\*.txt")

with open("C:\\Users\\ffayaza\\Documents\\Data\\PROJECT_DATA\\TEST_DATA\\formated_data\\December\\03122018\\result_03122018.txt", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())
