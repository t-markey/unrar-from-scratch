import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "unrar"))



from unrar import rarfile


rar = rarfile.RarFile('018- Harperactive -  Harp Shaped Box.rar')
print(rar.namelist())
rar.printdir()


