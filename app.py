import os, sys, shutil
import hashlib, time

source = sys.argv[1]
replica = sys.argv[2]
interval = int(sys.argv[3])
logfile = sys.argv[4]

def hashfile(file):
    sha256 = hashlib.sha256()
    with open(file, 'rb') as f:
        while True:
            data = f.read()
            if not data:
                break
            sha256.update(data)
    return sha256.hexdigest()

def synchronizefiles():
    log = open(logfile, "a")
    source_folders = foldertree(source)[1]
    replica_folders = foldertree(replica)[1]
    #Subfolders new
    for fn in source_folders:
        if fn not in replica_folders:
            subfolder = os.path.join(replica, fn)
            if not os.path.isdir(subfolder):
                os.makedirs(subfolder)
                log.write("Folder created: "+subfolder+"\n")
                print("Folder created: "+subfolder) 
    #Subfolders to delete            
    for fd in replica_folders:
        if fd not in source_folders:
            subfolder = os.path.join(replica, fd)
            if os.path.isdir(subfolder):
                shutil.rmtree(subfolder)
                log.write("Folder deleted: "+subfolder+"\n")
                print("Folder deleted: "+subfolder) 
    sourcefiles = foldertree(source)[0]
    replicafiles = foldertree(replica)[0]
    #New and modified files
    for n in sourcefiles:
        n1 = source+"/"+n    
        if all([os.path.isfile(n1), not n in replicafiles]):
            shutil.copyfile(n1, replica+"/"+n)
            log.write("New file: "+n+"\n")
            print("New file: "+n)
        else:
            f1_hash = hashfile(n1)
            f2_hash = hashfile(replica+"/"+n)
            if f1_hash != f2_hash:
                shutil.copyfile(n1, replica+"/"+n)
                log.write("Copied modified file: "+n+"\n")
                print("Copied modified file: "+n)  
    #Deleted files             
    for d in replicafiles:
        d1 = replica+"/"+d
        if all([os.path.isfile(d1), not d in sourcefiles]):
            os.remove(d1)
            log.write("Deleted file: "+d+'\n')
            print("Deleted file: "+d)

def foldertree(folder):
   fileslist = []
   dirslist = []
   for root, dirs, files in os.walk(folder):
      for name in files:
         fileslist.append(os.path.relpath(os.path.join(root, name), folder))
      for name in dirs:
         dirslist.append(os.path.relpath(os.path.join(root, name), folder))   
   return fileslist, dirslist

def main():
    while True:
        synchronizefiles()
        time.sleep(interval)
        print("Synchronizing..")   

if __name__ == "__main__":
    main()