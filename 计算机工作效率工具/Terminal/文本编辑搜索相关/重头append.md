
https://unix.stackexchange.com/questions/274493/how-do-i-insert-the-first-line-of-one-file-into-the-first-line-of-another

``` bash

$ cat file1
Jack and Jill
Went up the hill
To fetch a pail of water.

$ cat file2
Nursery Rhymes:
Epic Poems:
Classic Literature:

$ printf '%s\n' '0r !head -n 1 file2' x | ex file1

$ cat file1
Nursery Rhymes:
Jack and Jill
Went up the hill
To fetch a pail of water.

```