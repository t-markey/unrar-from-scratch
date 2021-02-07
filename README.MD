# Unrar from scratch (ish) 

Unpacking a rar file on a mac with python .  More fun than the app store !

## Getting Started

The first move was to install the unrar module using pip,

```bash
$ pip install unrar
```

This pyhton module (and most solutions i saw)  depends on a library from https://www.rarlab.com/rar_add.htm .  Here is direct download :  http://www.rarlab.com/rar/unrarsrc-5.2.6.tar.gz This will be an exectuable once it is compiled .


I hadn't worked with C++ in a while (9 years.. ?) so the following was very usedful to me: https://hiltmon.com/blog/2015/09/28/the-simple-c-plus-plus-makefile-executable-edition/ . Specifically the section called 'Using the Makefile' all the way at the bottom.

Next is to  ```$ cd ``` into the unrar directory we just downloaded. Run ```$ make clean```followed by ```$ make -j```

I had to open the makefile (```$ vi makefile ```) and remove the -D flag and also changed the path from local to bin . Was getting a 62 and 72 error before I did this .

```
install-unrar:
			install -D unrar $(DESTDIR)/bin/unrar
```

changed to 

```
install-unrar:
			install unrar $(DESTDIR)/local/unrar
```

Next installing the executable:

```
$sudo make install
```

Now depending on your paths and where you saved it , you may need to at that to your paths.

```
$ echo $PATH
```
This list should include the path from the makefile. I had to add usr/local to my list of paths : ```$ sudo vi /etc/paths``` will open the list in vim.  For those that might not know, vim has different editing modes. Pressing i puts you into insert mode with allows you to edit the text.  To finish and save you will press <kbd>esc</kbd>, then <kbd>:</kbd> ,followed by <kbd>w</kbd><kbd>q</kbd> , and finally <kbd>enter</kbd>.  The w saves and the q exits vim.

The usual place for an executable like this would be usr/bin , but I wasnt able to move any files into that directory at this point because of security features implemented by apple. See here for explanation : https://superuser.com/questions/933019/sudo-cant-create-file-in-usr-bin-in-el-capitan/1000037


## Putting it all together

At this point all the dependancies should be there and we are ready to rest.  Have a Rar file ready to test with.  This link has more information if you are interested in the other methods from the rarfile module : https://python-unrar.readthedocs.io/en/v0.3/rarfile.html#rarfile-objects . If there is an error about partial data from one of the elements or 'bad rar file' that is probably from the module not being able to access the Rar library we complied above becuase of a path issue.

```
   $ cd ~/[the directory of your test.rar file]
   $ python3
   >>> import rarfile
   >>> file  = rarfile.RarFile('test.rar')
   >>> file.extractall()
   >>> file.close()
   ```
   
 Now you should have all the extraced files in your current directory.  As a bonus, if you have a sketchy rar file and would like to see the contents you can run the follwing before you do extractall(): 
 
```
  >>>> file.namelist()
```

Thank you for reading!



## Resources and Acknowledgments
https://www.rarlab.com/rar_add.htm

https://pypi.org/project/unrar/

https://python-unrar.readthedocs.io/en/v0.3/

https://hiltmon.com/blog/2015/09/28/the-simple-c-plus-plus-makefile-executable-edition/

https://pypi.org/project/unrar/

https://vsoch.github.io/lessons/unrar-python/





