

# check the token is valid


```bash
curl -H "Authorization: token YOUR_TOKEN_HERE" https://api.github.com/user
```


# check the token is valid for a project

```bash
curl -H "Authorization: token YOUR_TOKEN_HERE" \
     https://api.github.com/repos/OWNER/REPO
```
