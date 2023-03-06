import string, os

os.chdir(r"C:\Users\Yerzhan\Documents\GitHub\pp2-22B030422\tsis6\dir_files\letters")

for letter in string.ascii_uppercase:
   with open(letter + ".txt", "w") as f:
       f.writelines(letter)