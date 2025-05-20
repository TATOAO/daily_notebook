

# docker 权限问题

```bash
lwt@ubuntu-s-4vcpu-8gb-240gb-intel-sgp1-01:~$ docker container ls
permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Get "http://%2Fvar%2Frun%2Fdocker.sock/v1.49/containers/json": dial unix /var/run/docker.sock: connect: permission denied
lwt@ubuntu-s-4vcpu-8gb-240gb-intel-sgp1-01:~$
lwt@ubuntu-s-4vcpu-8gb-240gb-intel-sgp1-01:~$ sudo groups lwt
[sudo] password for lwt:
lwt : lwt sudo users docker
lwt@ubuntu-s-4vcpu-8gb-240gb-intel-sgp1-01:~$ ls -l /var/run/docker.sock
srw-rw---- 1 root docker 0 Apr 24 07:48 /var/run/docker.sock
lwt@ubuntu-s-4vcpu-8gb-240gb-intel-sgp1-01:~$
```


有时候设置了 docker groups 但用户还是无法直接使用docker 

You’re already in the `docker` group, and the socket has the right permissions (`rw` for owner and group, and the group is `docker`), so that part is set up correctly.

However, **your current session might not reflect the group membership yet**.

### Fix: Refresh your session
You can either:

#### ✅ Option 1: Log out and log back in
This will refresh your group memberships.

#### ✅ Option 2: Use `newgrp` to apply group changes without logging out:
```bash
newgrp docker
```
Then try running:
```bash
docker container ls
```

Let me know if that still doesn't work!



# tmux 启用之后设置需要重启

tmux kill-server


