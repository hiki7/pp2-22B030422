import os

existence = os.access(r"C:\Users\Yerzhan\Documents\GitHub\pp2-22B030422\tsis6\dir_files\test\Thomas.pdf", os.F_OK)
readability = os.access(r"C:\Users\Yerzhan\Documents\GitHub\pp2-22B030422\tsis6\dir_files\test\Thomas.pdf", os.R_OK)
writability = os.access(r"C:\Users\Yerzhan\Documents\GitHub\pp2-22B030422\tsis6\dir_files\test\Thomas.pdf", os.W_OK)
exucatability = os.access(r"C:\Users\Yerzhan\Documents\GitHub\pp2-22B030422\tsis6\dir_files\test\Thomas.pdf", os.X_OK)

print("Exist:", existence)
print("Readable:", readability)
print("Writable:", writability)
print("Exucatable:", exucatability)