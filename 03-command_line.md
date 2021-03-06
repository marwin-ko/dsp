# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

Linux/Mac OSX
* pwd    => print working directory
* mkdir  => make directory
* cd     => change directory
* ls     => list directory
* rmdir  => remove directory
* pushd  => push directory
* popd   => pop directory
* cp     => copy a file or directory
* mv     => move a file or directory
* xargs  => execute arguments
* find   => find files
* grep   => find things inside files
* env    => look at your environment
* echo   => print some arguments
* export => export/set a new environment variable
* exit   => exit the shell
* sudo   => DANGER! become super user root DANGER!
* chmod  => change permission modifiers
* chown  => change ownership

---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

* ls      => lists directory contents
* ls -a   => list all files
* ls -l   => list with long format
* ls -lh  => list long format in human readable size
* ls -lah => list all files in long format in human readable size 
* ls -t   => sort by time & date
* ls -Glp => inhibit display of grop information, list with long format, displays directories with /

---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

My favorite `ls` option commands are:

1. ls -a  => lists all files
2. ls -c  => lists files by file timestamp
3. ls -d  => lists only directories
4. ls -R  => lists subdirectories as well
5. ls -u  => lists files by the file access time

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

The `xargs` reads items from the standard input, delimited by blanks or new lines, and executes the command one or more times with any initial arguments followed by the items read from standard input. The following example code (see below) finds a file_name in or below the directory_name and deletes them.
```
find /directory_name -name file_name -type f -print | xargs /bin/rm -f 
```

 

