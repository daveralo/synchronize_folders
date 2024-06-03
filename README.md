# Synchronization of two folders

Program that synchronizes two folders: source and replica. The program maintain a full, identical copy of source folder at replica folder. 
* Synchronization is in one-way: after the synchronization content of the replica folder is modified to exactly match content of the source folder. 
* Synchronization is performed periodically.
* File creation/copying/removal operations are logged into a file and to the console output.

The program receives 4 arguments:
1. Source folder path
2. Replica folder path
3. Synchronization interval in seconds
4. Log file name.

For example:

```
python app.py /folder/source/ /folder/replica/ 5 log.txt
```

I used the following libraries ans methods:
* [os.walk()](https://www.w3schools.com/python/ref_os_walk.asp) method: To get the file and directory names in a directory tree by walking the tree.
* [hashlib.sha256()](https://docs.python.org/3/library/hashlib.html) method: To create a SHA-256 hash object. I used it to compare files if any changed.
* [os.makedirs](https://www.w3schools.com/python/ref_os_makedirs.asp) method: To create a directory recursively. 
* [shutil.rmtree](https://docs.python.org/3/library/shutil.html) method: To delete an entire directory tree.
* [shutil.copyfile](https://docs.python.org/3/library/shutil.html) method: To copy files.
* [os.remove](https://www.w3schools.com/python/ref_os_remove.asp) method: To remove file of the specified path.
* [time.sleep](https://docs.python.org/3/library/time.html#time.sleep) method: To suspend execution of the calling thread for the given number of seconds.
