## redhat 安装oracle11g静默安装教程：

软件包：

1**、安装JDK**

将JDK1.7考入到系统中，进入JDK压缩文件存放目录中，执行tar –zxvf 文件全名，解压后JDK1.7自动安装（JDK1.7不需要执行BIN文件，只需要解压即可）

 

**2****、安装依赖包**

利用终端进入RPM存放的文件夹内，执行-- rpm -ivh *.rpm --nodeps  --force，将依赖包进行安装

 

**3****、创建分组及用户**

/usr/sbin/groupadd oinstall

/usr/sbin/groupadd dba

 

**4****、创建oracle用户**

/usr/sbin/useradd -g oinstall -G dba oracle

passwd oracle

 

**5****、修改 vi /etc/sysctl.conf 文件，加上如下参数**

```
fs.aio-max-nr = 1048576 

fs.file-max = 6815744 

kernel.shmall = 2097152 

kernel.shmmax = 536870912 

kernel.shmmni = 4096 

kernel.sem = 250 32000 100 128 

net.ipv4.ip_local_port_range = 9000 65500 

net.core.rmem_default = 262144 

net.core.rmem_max = 4194304 

net.core.wmem_default = 262144 

net.core.wmem_max = 1048586
```

应用配置使其生效：/sbin/sysctl -p

 

**6****、修改 vi /etc/security/limits.conf 文件，加上下面的参数**

```
oracle           soft    nproc   2047 

oracle           hard   nproc   16384 

oracle           soft    nofile  1024 

oracle           hard    nofile  65536
```

 

**7****、修改 vi /etc/profile文件，加入如下参数**

```
if  [ $USER = "oracle" ];  

then         

if  [ $SHELL = "/bin/ksh" ];  

then     ulimit -p 16384    ulimit -n 65536         

else     ulimit -u 16384 -n 65536         

fi 

fi
```

 

**8****、创建Oracle安装目录**

mkdir -p /u01/app/oracle

mkdir -p /u01/app/oradata

mkdir -p /u01/app/oraInventory

 

**9****、切换至oracle用户，增加如下配置**

su  - oracle

vim ~/.bash_profile

```
# Oracle Settings

TMP=/tmp; export TMP

TMPDIR=$TMP; export TMPDIR

ORACLE_BASE=/u01/app/oracle; export ORACLE_BASE

ORACLE_HOME=$ORACLE_BASE/product/11.2.0/db_1; export ORACLE_HOME

ORACLE_SID=orcl; export ORACLE_SID

SQLPATH=$ORACLE_HOME/sqlplus/admin; export SQLPATH

ORACLE_TERM=xterm; export ORACLE_TERM

EDITOR=vi; export EDITOR

PATH=$PATH:$ORACLE_HOME/bin:$HOME/myShell;

export PATH

LD_LIBRARY_PATH=$ORACLE_HOME/lib:/lib:/usr/lib; export LD_LIBRARY_PATH

CLASSPATH=$ORACLE_HOME/JRE:$ORACLE_HOME/jlib:$ORACLE_HOME/rdbms/jlib;

export CLASSPATH
```

执行source ~/.bash_profile 命令使其生效

 

**10****、创建oraInst.loc文件**

vim /etc/oraInst.loc

在文件内编辑

```
inventory_loc=/u01/app/oraInventory

inst_group=oinstall
```

赋予文件用户、组，以及权限

chown -R oracle:oinstall /etc/oraInst.loc

chmod -R 775 /etc/oraInst.loc

 

**11****、将安装包文件解压至/app目录下**

解压后路径为/app/database

 

**12****、将oracle静默安装所需的应答文件拷贝至/u01/app/oracle文件夹下**

cp /app/database/response/* /u01/app/oracle

 

**13****、修改应答文件权限**

chown -R oracle:oinstall /u01/app

chmod -R 775 /u01/app

 

**14****、设置主机名**

 

**15****、配置db_install.rsp数据库软件安装文件**

vim /u01/app/oracle/db_install.rsp 

 

修改内容如下：

```
oracle.install.option=INSTALL_DB_SWONLY     　　　　　　　 //安装类型,只装数据库软件

ORACLE_HOSTNAME=db             　　　　　　　　　　　　   //主机名称（命令hostname查询）

UNIX_GROUP_NAME=oinstall       　　　　　　　　　　　　   // 安装组

INVENTORY_LOCATION=/u01/app/oraInventory  　　　　　　//INVENTORY目录（**不填就是默认值,本例此处需修改,因个人创建安装目录而定）

SELECTED_LANGUAGES=en,zh_CN            　　　　　　　　 // 选择语言（默认en）

ORACLE_HOME=/u01/app/oracle/product/11.2.0/db_1  　　　  // oracle_home *路径根据目录情况注意修改 

ORACLE_BASE=/u01/app/oracle                       　　　               // oracle_base *注意修改

oracle.install.db.InstallEdition=EE          　　　　　　　              // oracle版本

oracle.install.db.isCustomInstall=false      　　　　　　　           //自定义安装，否，使用默认组件

oracle.install.db.DBA_GROUP=dba              　　　　　　　       //dba用户组

oracle.install.db.OPER_GROUP=oinstall        　　　　　　　     //oper用户组

oracle.install.db.config.starterdb.type=GENERAL_PURPOSE     //数据库类型

oracle.install.db.config.starterdb.globalDBName=orcl                  //globalDBName

oracle.install.db.config.starterdb.SID=orcl  　　　　　　　         //SID（**此处注意与环境变量内配置SID一致）

oracle.install.db.config.starterdb.memoryLimit=81920                //自动管理内存的内存(M,总内存的40%)

oracle.install.db.config.starterdb.password.ALL=orcl                   //设定所有数据库用户使用同一个密码

SECURITY_UPDATES_VIA_MYORACLESUPPORT=false       　 //（手动写了false）

DECLINE_SECURITY_UPDATES=true　　　　　　　　　　　   // **注意此参数 设定一定要为true
```

 

**16****、在oracle用户下执行数据库（不包含实例）安装**

/app/database/./runInstaller -silent -force -ignorePrereq -responseFile /usr/local/oracle/db_install.rsp

以上为一行

\##参数说明  

-silent 静默模式

-force 强制安装

-ignorePrereq忽略warning直接安装。

-responseFile读取安装应答文件。

##备注 需要等待一会等控制台打出日志路径。

 

**17****、执行后根据页面提示去tail -f 打印安装日志**

 

**18****、配置监听netca.rsp文件**

```
INSTALL_TYPE=""custom""                                    //安装类型选择 custom

LISTENER_NUMBER=1                                         //监听数量

LISTENER_NAMES={"LISTENER"}                        //监听名称

LISTENER_PROTOCOLS={"TCP;1521"}               //监听网络连接类型及端口号

LISTENER_START=""LISTENER""       
```

​                  

 

**19****、静默安装监听**

$ORACLE_HOME/bin/netca -silent -responseFile /u01/app/oracle/netca.rsp

 

**20****、修改 $ORACLE_HOME/bin/dbstart文件  （待验证）**

ORACLE_HOME_LISTNER=$ORACLE_HOME

 

**21****、创建数据库，修改 dbca.rsp 文件**

```
RESPONSEFILE_VERSION = "11.2.0"                                          //数据库版本号，默认值即可

OPERATION_TYPE = "createDatabase"                                      //创建类型为创建数据库

GDBNAME = "orcl"                                                                       //全局名

SID = "orcl"                                                                                   //实例名

TEMPLATENAME = "New_Database.dbt" 

SYSPASSWORD = "system" 

SYSTEMPASSWORD = "system" 

DATAFILEDESTINATION ="/u01/app/oradata/" 

RECOVERYAREADESTINATION="/u01/app/oracle/flash_recovery_area" 

STORAGETYPE=FS 

CHARACTERSET = "ZHS16GBK"

MEMORYPERCENTAGE = "40" 

SCRIPTDESTINATION ="/u01/app/oracle/admin/ora10g/scripts"     //待验证

EMCONFIGURATION=”LOCAL”

SYSMANPASSWORD = "system" 

DBSNMPPASSWORD = "system"
```

**22****、创建实例**

dbca -createDatabase -silent -responseFile /u01/app/oracle/database/response/dbca.rsp