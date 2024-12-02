


# install

yum install -y postgres
apt install -y postgres

change PATH

```
export PATH=$PATH/usr/bin/postgresql/12/bin/
```

# start service

service postgresql start

# set up password


ALTER USER user_name WITH PASSWORD 'new_password';
OR 
sudo -u postgres psql -c "ALTER USER postgres PASSWORD '<new-password>';"

-- if is a root user
su -c "psql -c \"ALTER USER postgres PASSWORD 'new-password';\"" - postgres

