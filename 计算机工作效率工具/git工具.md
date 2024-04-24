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

# create a branch from commit
git branch branch_name <commit-hash>
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


#### rename Branch

```bash
git branch -m new_name
# or 
git branch -m old_name new_name
```

## Push remote

``` 

git push origin lwt: master

```
冒号define 要从哪个branch push 到哪个branch


## git diff

``` bash

git diff code-origin/main

```

## git 中文乱码问题
git diff 其实会调用 less
```
export LESSCHARSET=utf-8
```


git commit 

```
git config --global i18n.commitencoding utf-8
git config --global i18n.logoutputencoding utf-8
git config --global gui.encoding utf-8
```


未解决git commit之后的返回还是乱码问题。


## cherry-pick

先git log 获取到对应的commit 的id

从 branch b pick branch a 的commit
```
git cherry-pick #commit-id#

```

[cherry-pick but no commit](https://stackoverflow.com/questions/5717026/how-to-cherry-pick-only-changes-to-certain-files ":)")
git cherry-pick -n <commit>


## git fetch / git pull

```
git fetch 
git log # 找到对应的新分支的id
git merge # id 


git pull 

```


## git grep

git grep <regexp> $(git rev-list --all)



## git status 中文乱码 /217/239/203...

git config --global core.quotepath false



## 保存密码

git config --global credential.helper store
