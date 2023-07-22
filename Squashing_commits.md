
On your local branch...
```bash
git rebase -i master
```

- An editor pops up showing all commits marked as "picked".
- Starting from the bottom-up, change "pick" to "sqaush" for every commit you want to be squashed into first.
- Save and exit file (nano): `ctrl+s , ctrl+x`
- Second window appears showing all commit messages. Remove all messages except one with will hold the message of your single squashed commit.

```bash
git push origin <branch> --force
```
*Using the --force flag is necessary because the commit history of your branch has been rewritten due to the rebase.*
