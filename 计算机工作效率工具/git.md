CI 问题 连续集成



# git command


## Branch


``` bash
#To see local branches, run this command:
git branch
#To see remote branches, run this command:
git branch -r
#To see all local and remote branches, run this command:
git branch -a
```

```bash
# delete branch locally
git branch -d localBranchName
# delete branch remotely
git push origin --delete remoteBranchName
```
[Source](https://www.freecodecamp.org/news/how-to-delete-a-git-branch-both-locally-and-remotely/ "TEST")



```bash
# create a new branch
git checkout -b new_branch
# push into remote repository
git push -u origin the_branch
```


### get remote info but not pull, including branches 
git fetch **remote name**

## Change remote url
```bash
# this is for checking 
git remote -v

# can set up using this line
git remote set-url origin https://github.com/USERNAME/REPOSITORY.git

# git add remote and give it a name
git remote add github https://github.com/TATOAO/daily_notebook.git

# first time push to define the remote (require login )
git push --set-upstream github master
```




## Branch

#### Merge
``` bash
# merge the current branch to the target 
git merge github/main --allow-unrelated-histories

```


#### Delete Branch
``` bash
# local delete
git branch -d fix/authentication

git push origin --delete fix/authentication

```

## Push remote


## git diff

``` bash

git diff code-origin/main

```
中文乱码问题
git diff 其实会调用 less
```
export LESSCHARSET=utf-8
```