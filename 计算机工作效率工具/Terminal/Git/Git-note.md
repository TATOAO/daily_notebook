t # Github commant note


## Branch
```bash
# delete branch locally
git branch -d localBranchName
# delete branch remotely
git push origin --delete remoteBranchName

# rename  -m = modify

git branch -m new_branch_name





```
[Source](https://www.freecodecamp.org/news/how-to-delete-a-git-branch-both-locally-and-remotely/ "TEST")

``` bash

#To see local branches, run this command:
git branch
#To see remote branches, run this command:
git branch -r
#To see all local and remote branches, run this command:
git branch -a
```
## Push remote

[SO copy a branch](https://stackoverflow.com/questions/14998923/how-can-i-copy-the-content-of-a-branch-to-a-new-local-branch ":)")
```bash
# create a new branch
git branch new_branch
git checkout -b new_branch


git checkout -b new_branch old_branch

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



## Test jekyll locally
```bash
bundle exec jekyll serve
```

--
[Link](https://backlog.com/git-tutorial/cn/stepup/stepup1_3.html "猴子都懂的GIT入门")




## only git clone one subfolder

sparseCheckout
[SO only git clone subfolder](https://stackoverflow.com/questions/600079/how-do-i-clone-a-subdirectory-only-of-a-git-repository ":)")


mkdir <repo>
cd <repo>
git init
git remote add -f origin <url>

This creates an empty repository with your remote, and fetches all objects but doesn't check them out. Then do:

git config core.sparseCheckout true
Now you need to define which files/folders you want to actually check out. This is done by listing them in .git/info/sparse-checkout, eg:

echo "some/dir/" >> .git/info/sparse-checkout
echo "another/sub/tree" >> .git/info/sparse-checkout


## git grep 搜索

注意, 这个命令需要在和.git同级的目录里执行, 不然可能只会做子目录的搜索

```
git grep "xxxxx" $(git rev-list --all)
git branch -a --contains <target_id>

``` 


## Reset Change 

[SO git reset from the remote](https://stackoverflow.com/questions/1628088/reset-local-repository-branch-to-be-just-like-remote-repository-head ":)")

#### Direct replace the local by the remote


git fetch origin 
git reset --hard origin/master


git reset --hard HEAD~1
git push -f <remote> <branch>

#### save the local to the other branch first

git commit -a -m "saveing to other branch"
git branch my-saved-work



### 批量修改 git commit message

倒数三个
$ git rebase -i HEAD~3
把pick改成r
```
pick e499d89 Delete CNAME
pick 0c39034 Better README
pick f7fde4a Change the commit message but push the same commit.

# Rebase 9fdb3bd..f7fde4a onto 9fdb3bd
#
# Commands:
# p, pick = use commit
# r, reword = use commit, but edit the commit message
# e, edit = use commit, but stop for amending
# s, squash = use commit, but meld into previous commit
# f, fixup = like "squash", but discard this commit's log message
# x, exec = run command (the rest of the line) using shell
#
# These lines can be re-ordered; they are executed from top to bottom.
#
# If you remove a line here THAT COMMIT WILL BE LOST.
#
# However, if you remove everything, the rebase will be aborted.
#
# Note that empty commits are commented out

```

如果已经push, 改了commit message 之后push会有冲突,需要-f一下
git push origin branch -f





#  修改上一次的commit 内容
或者说沿用上一次的commit ， 但是继续修改一些东西
git commit —amend —no-edit

