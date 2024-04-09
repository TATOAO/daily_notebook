

CMCCAdmin


https://www.right.com.cn/forum/thread-8266942-1-1.html


1.使用光猫背后的普通用户名登录进光猫，浏览器复制以下链接打开

http://192.168.1.1/usr=CMCCAdmin ... md=1&telnet.gch

2.电脑启用 telnet



3. 通过telnet进入光猫



输入：

telnet 192.168.1.1

用户名、密码如下：
CMCCAdmin
aDm8H%MdA  

注意：密码默认不显示 不需要重复输入


4.查看一下登陆信息,可以看到账号密码全部进行了加密
sidbg 1 DB p DevAuthInfo

输入上面的命令后将会显示下面的内容：
<Tbl name="DevAuthInfo" RowCount="2">
<Row No="0">
<DM name="ViewName" val="IGD.AU1"/>
<DM name="Enable" val="1"/>
<DM name="IsOnline" val="0"/>
<DM name="AppID" val="1"/>
<DM name="User" val="******"/>
<DM name="Pass" val="******"/>
<DM name="Level" val="1"/>
<DM name="Extra" val=""/>
<DM name="ExtraInt" val="0"/>
</Row>
<Row No="1">
<DM name="ViewName" val="IGD.AU2"/>
<DM name="Enable" val="1"/>
<DM name="IsOnline" val="0"/>
<DM name="AppID" val="1"/>
<DM name="User" val="******"/>
<DM name="Pass" val="******"/>
<DM name="Level" val="2"/>
<DM name="Extra" val=""/>
<DM name="ExtraInt" val="0"/>
</Row>
</Tbl>
5. 修改CMCCAdmin用户的登录密码

输入下面的命令更改CMCCAdmin的密码：

sidbg 1 DB set DevAuthInfo 0 Pass admin

Pass后面是CMCCAdmin的登录密码

再输入下面的命令保存即可
sidbg 1 DB save
完成后即可使用CMCCAdmin+更改后的密码即可登录光猫后台。

祝各位使用愉快！


