- [General and Logging](#general-and-logging)
- [Branches](#branches)
- [Branches: Undoing](#branches-undoing)
- [Commits: Undoing](#commits-undoing)
- [Commits](#commits)
- [Stashing](#stashing)

# General and Logging


Fetch + Merge changesinto local
```bash
git pull
```
This is the same as git fetch ＜remote＞ followed by git merge origin/＜current-branch＞.

<br />

View reflog
```bash
git reflog
```

<br />

Point local repo to remote repo
```bash
git config --global user.name "Your Name"
```

<br />

Clone remote repo to local directory
```bash
git clone <repo url>
```

<br />

Log: Log x number (5) of last commits
```bash
 git log –n 5 –oneline
```

<br />

Log: Log x number (25) of last commits – prettify
```bash
 git log -n 25 --decorate --graph --oneline
```

<br />

Log: Log x number (5) of last commits – prettify
```bash
 git log -n 5 --decorate --graph --oneline
```

<br />

Log: Activity in last week/by author
```bash
git log --oneline  --after="last week" 
```

```bash
git log --oneline  --after="last week" --author="Bobby Valenzuela"
```

<br />

Log: Show commits and their code changes
```bash
git log -p
```

<br />

View differences in file (unstaged changes)
```bash
 git diff
```

<br />

View differences in file (staged changes)
```bash
 git diff --staged
```

<br />

Log since some date	
```bash
git log --pretty=medium  --after "Tue Jan 31 2023"
```

<br />

## Git blame
Line Number based (from-to)
```bash
git blame script.pl  -L 31023,3105
```

<br />

Regex Based
```bash
git blame <file>  -L ^/<regex>/    
git blame script.pl  -L ^/function\\scoolFunction/    
```

<br />

With single-quotes:
```bash
git blame script.pl  -L '/^function coolFunction/'   
```

<br />

# Branches

Create branch
```bash
git branch <branchname>
```

<br />

Create & switch to branch
```bash
git checkout –b branchname
```

<br />

Switch to previously checked-out branch
```bash
git checkout –
```

<br />

Show current branch
```bash
git branch | grep -E '*'
```
or
```bash
git branch –show-current
```

<br />

Merge a branch into master
```bash
git merge <branchname>
```
Note: Can’t be on merging branch.

<br />

Renaming local branch to the new name
```bash
git branch -m <old-name> <new-name>
```

<br />

Checkout branch starting at a specific commit 
```bash
git branch <branchname> <commit hash>
```

<br />

Get remote branch with changes unstaged
```bash
git pull origin myremotebranch –no-commit
```

<br />

Pull master branch to local
```bash
git pull origin master

```

<br />

## Branches: Undoing

<br />

Reset local branch to state of remote:  

```bash
git reset --hard origin/master
```

<br />

Delete a local branch: 
```bash
git branch -d localBranchName
```

<br />

Show branch history: 
```bash
git show-branch
```
or
```bash
git show-branch <Branch name>
```

<br />

Show branch history: 
```bash
git show-branch
```


<br />

Unstage (git V3+) you can use . instead of file_path to unstage all staged files in pwd
```bash
git restore --staged <file_path>
```

<br />

Branch tracking: Create new local branch which tracks a remote branch
```bash
git branch --track <new_branch> origin/<remote_branch>
```
or (preferred) 
```bash
git checkout --track origin/<remote_branch>
```

<br />

Set tracking on existing branch to remote branch
```bash
git branch --set-upstream-to=origin/<branch> DEV-1117
```

<br />


# Commits: Undoing

Remove last commit (keep changes - back to staged/uncommitted)
```bash
git reset --soft HEAD~1
```

<br />

Or you can specify a commit hash to go back to
```bash
git reset --soft 2b504bee
```

<br />

Remove last commit (lose changes)
```bash
git reset --hard HEAD~1
```
<br />


Or you can specify a commit hash to go back to
```bash
git reset --soft 2b504bee
```
<br />


Unstage all staged changes 
```bash
git reset index.html
```
```bash
git reset . 
```

<br />

Undo all unstaged changes (pre 2.23) 
```bash
git checkout -- index.html
```
```bash
git checkout -- .
```

<br />

Undo all unstaged changes (git 3.0+) [Might need to download snap]
```bash
git restore index.html
```
```bash
git restore .
```

<br />

Revert a commit and stage changes
```bash
git revert <hash> --no-commit -–no-edit
```

<br />

Revert a merge commit and stage changes
```bash
git revert <hash> -m 1 --no-commit ```
```
'-m 1': means restore to state one merge commit prior.

<br />

Rebase local changes
```bash
rebase <branch>
```
*Keeps a linear git history free of merge commits. Should only be done for editing local changes. Do not do for any commits already pushed to repo.* 

<br />

Make changes and apply them to last commit (such as editing commit message)
```bash
git commit --amend```
```
*Quite literally overwrites previous commit. If ran with no changes made, will default to letting you change description.*
*__\[WARNING]: Avoid amending commits that have already been pushed to a repo.__*

<br />

# Cherrypicking

Cherrypick and no commit (save code to stage)
```bash
git cherry-pick –no-commit <hash>
```

<br />

<br />

__If you want to commit every UP TO and  including specific commit, I’ve had success cherry-picking in order all the commits individually.Or.. see below__

<br />

Cherrypick succession of commits (no commit)
```bash
git cherry-pick –no-commit <from hash>^..<to hash>
```
*This does all at once – not in succession – so could lead to conflicts. (see here) . If so just abort and try again. `git cherry-pick --abort`*

<br />

Other way to do this - just do all individually in order
```bash
git cherry-pick –no-commit <hash1> <hash2> <hash3> …
```

<br />

# Commits


Stage file(s)
```bash
git add filename
```

<br />

Stage all
```bash
git add –A
```

<br />

Stage only some changes to a file (step through changes)
```bash
git add –p <filename>
```
*'p' – “prompt” for changes to stage.*

<br />

Remove something from git index (so it's no longer tracked)

*Useful in case you’ve committing something and now that file/folder will not be respected by the .gitignore file. Remove that item from the git index with git rm –cached <item> then push up your .gitignore file.*
```bash
git rm -r --cached <folder>
```
```bash
git add .gitignore
```
<br />

```bash
git commit -m "fixed gitignore"
```
*Note: others who pull down from the repo will .have this file/folder removed altogether – use catiously. Or, just have others*

<br />

Commit all changes from a given file
```bash
git commit filename –m “message here”
```
<br />

Stage and Commit all changes
```bash
git commit –am “message here”
```
<br />

See what’s about to push (Committed not yet pushed)
```bash
git diff --stat --cached [remote/branch]
```
example:
```bash
git diff --stat --cached origin/master
```
<br />

Change the msg of the last commit
```bash
git push –-amend –m “updated msg!”
```
<br />

Include more staged changes to last commit
```bash
git add .
```
```bash
git commit –-amend –m “updated msg!”
```
<br />

Push local changes to remote repo
```bash
git push –u origin master
```
*Note: -u is short for upstream*

<br />

Push local changes to remote repo on new branch
```bash
git push –-set-upstream origin newbranchname
```
*Note: Here, origin specifies origin of this commit (local working branch)*

<br />

Push Single commit
```bash
git push urlto e55b5f:master
```
<br />


# Stashing

Save stash annotated with a message
```bash
git stash push –m Some mewssage 
```
<br />

Save stash annotated with a message
```bash
git stash save my message...
```
<br />

Stash a single file (no msg)
```bash
git stash save –- myfile.py
```
<br />

List of current stashes
```bash
git stash list
```
<br />

Show most recent stash content
```bash
git stash show -p
```
<br />

Show stash content by index
```bash
git stash show –p stash@{2}
```
<br />

```bash
git stash show –p –-index 2
```
<br />

Show most recent stash by index (preferred)
```bash
git stash show –p 2
```
<br />

Delete entire stash
```bash
git stash clear
```
<br />

Delete single stash
```bash
git stash drop stash@{3}
```
<br />


Apply and Pop: Can use curly brace or index notation 
Apply a specific stash and remove from stash list
```bash
git stash pop --index 2
```
<br />

Apply the most recent stash
```bash
git stash apply
```
<br />

Apply a specific stash
```bash
git stash apply --index 2
```
<br />

Undelete a specific stash
```bash
git fsck --no-reflog | grep dangling | cut -d " " -f 3
```
^ The above will return a hash and you can git stash apply that hash id

<br />

