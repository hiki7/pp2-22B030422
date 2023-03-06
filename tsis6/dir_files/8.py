import os

ex = os.access(r"C:\Users\Yerzhan\Documents\GitHub\pp2-22B030422\tsis6\dir_files\test\test4.txt", os.F_OK)
print("Existence:", ex)
os.remove(r"C:\Users\Yerzhan\Documents\GitHub\pp2-22B030422\tsis6\dir_files\test\test4.txt")