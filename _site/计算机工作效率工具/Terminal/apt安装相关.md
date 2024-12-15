


sudo apt-get remove <application_name>


sudo apt-get purge <package-name>


查看安装
apt list --installed

查看安装时间
zgrep 'install ' /var/log/dpkg.log* | sort | cut -f1,2,4 -d' ' | grep we

