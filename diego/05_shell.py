import stat
import os

def cat(files):
  for f in files:
    try:
      f = open(f,'r')
      print(f.read())
    except FileNotFoundError:
      print("File not found")

def chmod(file,file_perm):
  perms = {
    # group
    0 : {
      7 : stat.S_IXGRP | stat.S_IWGRP | stat.S_IRGRP,
      6 : stat.S_IRGRP | stat.S_IWGRP,
      5 : stat.S_IRGRP | stat.S_IXGRP,
      4 : stat.S_IRGRP,
      2 : stat.S_IWGRP,
      1 : stat.S_IXGRP,
      0 : 0
    },

    # user
    1 : {
      7 : stat.S_IXUSR | stat.S_IWUSR | stat.S_IRUSR,
      6 : stat.S_IRUSR | stat.S_IWUSR,
      5 : stat.S_IRUSR | stat.S_IXUSR,
      4 : stat.S_IRUSR,
      2 : stat.S_IWUSR,
      1 : stat.S_IXUSR,
      0 : 0
    },

    # world
    2 : {
      7 : stat.S_IROTH | stat.S_IWOTH | stat.S_IXOTH,
      6 : stat.S_IROTH | stat.S_IWOTH,
      5 : stat.S_IXOTH | stat.S_IROTH,
      4 : stat.S_IROTH,
      2 : stat.S_IWOTH,
      1 : stat.S_IXOTH,
      0 : 0
    }
  }

  permission = 0
  for i,p in enumerate(file_perm):
    permission |= perms[i][int(p)]
  os.chmod(file,permission)


cat(["file1.txt"])
chmod("file1.txt","666")
