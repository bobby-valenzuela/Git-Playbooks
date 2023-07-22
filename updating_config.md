## Updated config info

Get current url
```bash
git config --get remote.origin.url
```
Note: The `--get` is implied anc can be ommitted.

<br />

Update current url
```bash
git config remote.origin.url <new_url>
```

<br />

### Bitbucket

Updating as bitbucket app password  
- Format: `https://<username>:<app_password>@bitbucket.org<repo_path>.git`
- Example: `https://<username>:<app_password>@bitbucket.org/myrepos/production.git`

<br />

[Get/Create App Password](https://bitbucket.org/account/settings/app-passwords/)
[Get Username](https://bitbucket.org/account/settings/)
