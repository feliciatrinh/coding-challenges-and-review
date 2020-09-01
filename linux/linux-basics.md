# Linux Basics

## Basic Commands

- See the permissions of a file using `ls -l /path/to/file`:
```
$ ls -l filename
-rwxr-xr-x 1 10490 floppy 17242 May  8  2013 acroread
```
First `-` represents a regular file. It gives you a hint of the type of object it is. It can have these values:
- d (directory)
- c (character device)
- l (symlink)
- p (named pipe)
- s (socket)
- b (block device)
- D (door)
- \- (regular file)

`r` represents read permission.  
`w` represents write permission.  
`x` represents executable permission.  

First combo of `rwx` reps permission for the owner.  
Second combo of `rwx` reps permission for the group.  
Third combo of `rwx` reps permission for other.  

- `pwd` is print working directory; writes the full pathname of the current working directory to stdout

- `cd -` toggles between your last two visited locations

- `>` redirects out to a file, overwriting the file; `>>` redirects output to a file, appending the redirected output at
the end:
```
$ which bash > backup.sh
$ echo 'tar -czf mysite.tar.gz mysite' >> backup.sh
```

- `<` redirects standard input from a file instead of the keyboard.

File `input.txt` contains
```
pie
apple
cat
banana
```

`sort < input.txt` outputs:

```
apple
banana
cat
pie
```

- `echo` prints the string(s) to standard output. Use `-n` if you do not want to output the trailing newline.q

- `echo $?` prints the return value of the previously executed evaluation (0 is true, 1 is false).

```
$ a=1
$ b=2
$ [ $a -lt $b ]
$ echo $?
0
```

## Bash Scripting Basics
- The bash is a default interpreter on many GNU/Linux systems. To see what your default interpreter is, run `echo $SHELL`:
```
$ echo $SHELL
/bin/bash
```
- To locate a full path to bash's executable binary, use `which bash`:
```
$ which bash
/bin/bash
```
- `file` command can be used to identify a type of the file:
```
$ file hello-world.sh
hello-world.sh: Bourne-Again shell script, ASCII text executable
```

### Script Execution

Example script `hello-world.sh` prints "Hello World" using `echo` to the terminal output.

```
#!/bin/bash

echo "Hello World"
```
Remember that you can redirect the output of `which bash` while creating a new file using `which bash > hello-world.sh`.

- To execute a shell script, it first needs to be make executable using `chmod +x filename`. Then do `./filename`:
```
$ chmod +x hello-world.sh
$ ./hello-world.sh
Hello World
```

- Alternatively, you could execute bash scripts by calling the bash interpreter explicitly `bash filename.sh`, in which
case you do not need to make the shell script executable and you do not need to declare shebang directly within the
shell script

### Variables

- You can assign and use variables directly from the terminal:
```
$ a=4
$ b=3
$ echo $a
4
$ echo $b
3
$ echo $a + $b
4 + 3
$ echo $[$a + $b]
7
```

- You can use variables in scripts through command substitution to make scripts more useful. In num_files.sh:

```
#!/bin/bash

# This bash script is used to print the number of files in the given directory (recursive) with the given extension

user=$(whoami)
num_files=$(find $1 -type f -name *$2 | wc -l)

echo "$user, there are $num_files $2 files in $1."
```
After making `num_files.sh` executable using `chmod +x num_files.sh`, execute it:

```
$ ./num_files.sh resources/data/ .wav
felicia, there are 2620 .wav files in resources/data/.
```
Note, you can pass arguments to the script from the command line: $0, $1, $2 and so on. $0 is the name of the script
itself. $1 is the first argument. $2 is the second argument and so on.

### Functions

Example
```
#!/bin/bash

# This bash script prints the number of files and the number of directories in the user's home directory.

user=$(whoami)
input=/home/$user

function total_files {
    find $1 -type f | wc -l
}

function total_directories {
   find $1 -type d | wc -l
}

echo -n "Number of files:"
total_files $input
echo -n "Number of directories:"
total_directories $input
```

## Numeric and String Comparisons

| Description  | Numeric Comparison  | String Comparison  |
|---|---|---|
| less than  | -lt  | <  |
| less or equal  | -le  | N/A  |
| greater than  | -gt  | >  |
| greater or equal  | -ge  | N/A  |
| equal  | -eq  | =  |
| not equal  | -ne  | !=  |

If the return value is `0`, then the comparison evaluation is true. If the return value is `1`, then the comparison
evaluation is false.

```
$ a=1
$ b=2
$ [ $a -lt $b ]
$ echo $?
0
```

There must be a space after `[` and a space before `]`.

```
$ [ 'apple' = 'orange' ]
$ echo $?
1
```

Note: Use `==` with `[[ ]]` for pattern matching.

This example shows how you'd check if 'GNU/Linux is ...' contains the substring 'Linux'. `*` means match all characters.
```
[[ 'GNU/Linux is an operating system' == *"Linux"* ]]
```