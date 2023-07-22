# Fixing a merge conflict

Suppose your branch 'DEV-123' is showing as conflict in the remote repo, but not showing as conflcited locally. We need to overwrite our local branch with a copy of the branch as it appears in the repo. Doing this will allow us to fix up those conflicts and push up the updated branch.

## Reset local branch
```bash
git pull && git branch -D <branch_name> && git checkout -b <branch_name>
```

<br />
Note: You could also rename the branch with 
```bash
git pull && git branch -m <branch_name> ORIG_BRANCH && git checkout -b <branch_name>
```

<br />

## Pull down conflict and fixes changes
```bash
git pull origin <branch_name> --no-commit
```

<br />

## Push up updated branch
Once all conflicts have been fixed you can add files to be stages, committed, and pushed.
```bash
git add -A . && git commit -m '<message>' && git push origin <branch_name>
```