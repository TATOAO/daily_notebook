# Github commant note


## Branch
```bash
# delete branch locally
git branch -d localBranchName
# delete branch remotely
git push origin --delete remoteBranchName
```
[Source](https://www.freecodecamp.org/news/how-to-delete-a-git-branch-both-locally-and-remotely/ "TEST")

## Push remote


```bash
# create a new branch
git checkout -b new_branch
# push into remote repository
git push -u origin the_branch
```


## Change remote url
```bash
# this is for checking 
git remote -v

# can set up using this line
git remote set-url origin https://github.com/USERNAME/REPOSITORY.git
```

## Test jekyll locally
```bash
bundle exec jekyll serve
```

--
[Link](https://backlog.com/git-tutorial/cn/stepup/stepup1_3.html "猴子都懂的GIT入门")


