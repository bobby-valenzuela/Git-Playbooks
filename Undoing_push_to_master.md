# Undoing a push to master  

<br />

While on local master branch… undo last commit (so you can stash those changes later)
```bash
git reset --soft HEAD~1
```
*This undoes your last commit and moves the changes from that commit back to ‘staged’.*

<br />
<br />

Now that the changes from your last commit are staged again you can stash your changes
```bash
git stash save nameofcoolstash
```

<br />

Your local master branch should be how it was before you made any changes.  
Use git pull to pull the latest push (that you pushed to master) down to your local master branch.
```bash
git pull
```
*This also adds your latest commit hash into the git log (this is the commit where you pushed to master).*

<br />
<br />

List the log of your past commit. (Just showing last five with this code)
```bash
git log –n 5 –oneline
```

<br />

Find (and copy) the hash of the commit where you pushed to master (Should be the first (most recent) commit)  
Use git revert to undo the commit
```bash
git revert <hash> --no-commit -–no-edit
```
`–no-commit` = keep reverted changes staged
`–no-edit` = keep default commit msg  
*This will not merely undo but rather inverse the changes you pushed to the master branch. So this is a set of changes such that your previously commit will effectively be cancelled out by these changes once you commit. *

<br />
<br />

Now your local master branch will have all reverted stuff  
On your local master branch, stage and commit these changes.
```bash
git add -A 
git commit -m "Reverting push to master"
git push
```

<br />
Now, run git pull again – everything should be back the way it was

__Placing your code on a new branch__
```bash
git checkout -b <new_branch> && git stash apply
```
