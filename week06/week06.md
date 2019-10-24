## week 6(date:20190930-20191015)

### Algorithm

##### leetcode 初级算法-链表篇

1. **合并两个有序链表**：https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/6/linked-list/44/
	
	题目描述:
	
		将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
	思路  (时间复杂度：O(n) )：
	
		1. 使用两个指针分别指向l1和l2，当l1的值大于等于l2,l2的指针加一，否者l1指针加一。将数值存到结果链表res中。
		2. 只到其中一个链表为空，则将另一个链表剩余的链直接加到结果链表res中。

```java
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode res=new ListNode(0);
        ListNode curr=res;
        while(l1!=null||l2!=null){
            if(l1==null){
                curr.next=l2;
                break;
            }            
            if(l2==null){
                curr.next=l1;
                break;
            }
            if(l1.val>=l2.val){  
                curr.next=l2;
                curr=curr.next;
                l2=l2.next;
            }else{
                curr.next=l1;
                curr=curr.next;
                l1=l1.next;
            }
            
        }

        return res.next;
        
    }
```

2. **回文链表**：https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/6/linked-list/45/

    题目描述:
	
		请判断一个链表是否为回文链表。

    思路(时间复杂度：O(n) ）（参考别人的解答）:

		1. 使用快慢指针确定，链表的中间位置。
		2. 翻转链表前半部分
    	3. 判断是否是回文链表
    	注意： 无法翻转整个链表，然后进行回文判断，翻转链表过程中会导致原链表结构被破坏。

   ​	代码：

```java
public boolean isPalindrome(ListNode head) {
        if (head == null || head.next == null) {
            return true;
        }
        //快慢指针找到链表的中点
        ListNode fast = head.next.next;
        ListNode slow = head.next;
        while (fast != null && fast.next != null) {
            fast = fast.next.next;
            slow = slow.next;
        }

        //翻转链表前半部分
        ListNode pre = null;
        ListNode next = null;
        while (head != slow) {
            next = head.next;
            head.next = pre;
            pre = head;
            head = next;
        }
        //如果是奇数个节点，去掉后半部分的第一个节点。

        if (fast != null) {
            slow = slow.next;
        }
        //回文校验
        while (pre != null) {
            if (pre.val != slow.val) {
                return false;
            }
            pre = pre.next;
            slow = slow.next;
        }

        return true;
        
    }
```

   

### Review

#### 150 successful machine learning models: 6 lessons learned at Booking.com

##### ：https://blog.acolyer.org/2019/10/07/150-successful-machine-learning-models/

##### 单词:

1. previously  以前
2. summary 摘要
3. explicitly 明确的
4. enumerated  枚举
5. inferred  推测
6. interpretation 解释
7. Model performance 模型性能
8. matters 问题
9. feedback 反馈
10. trials  尝试 
11. impact  影响
12. efforts 努力
13. conclusion  结论
14. iterative 迭代
15. fundamental 基本
16. integrated 结合
17. disciplines 记录
18. tempted 诱惑
19. interpret  解释
20. investing 投资
21. recommendations  建议
22. guest 客人
23. overwhelming 压倒性的
24. categories 分类


##### 文章大意：

介绍六个课程的大体介绍。
1. 引入机器学习模型的项目可带来强大的业务价值
2. 模型绩效与业务绩效不同
3. 明确要解决的问题
4. 预测服务延迟很重要
5. 尽早获得有关模型质量的反馈
6. 使用随机对照试验测试模型对业务的影响
在 booking.com 模型分为六大类。
旅行者偏好模型、旅行者上下文模型、空间导航模型、用户界面优化模型、内容策划模型、内容增强模型。


### Tips

- ##### 算法：
    - 对象的赋值分为浅拷贝和深拷贝。
    - 链表的合并可以通过定义两个指针提高性能。
    
- **linux 命令**

    - `ps -ef |grep java` 查看java进程
    - `kill -9 进程号`  关闭进程
    - `tail -f xxx`  刷新查看文件
    - `find / -name xxx.jar`  查看文件位置

### Share
linux 学习记录
一、linux 系统分类
    1. Debian系主要有Debian，Ubuntu，Mint等及其衍生版本；
    2. RedHat系主要有RedHat，Fedora，CentOs等，
    3. 其它有Slackware，Gentoo，Arch linux，LFS，SUSE等。
    - RedHat 系列
        1 常见的安装包格式 rpm包,安装rpm包的命令是“rpm -参数”
        2 包管理工具 yum
        3 支持tar包
    - Debian系列
        1 常见的安装包格式 deb包,安装deb包的命令是“dpkg -参数”
        2 包管理工具 apt-get
        3 支持tar包
二、Linux的基础知识
    1. Linux系统的组成：
        - linux内核（linus 团队管理）
        - shell：用户与内核交互的接口（常用(默认)的就是bash(bourne again shell)）
        - 文件系统：ext3、ext4等。windows 有 fat32 、ntfs
        - 第三方应用软件
    2. Linux 基本目录结构：
        - bin 存放二进制可执行文件(ls,cat,mkdir等)
        - boot 存放用于系统引导时使用的各种文件
        - dev 用于存放设备文件
        - etc 存放系统配置文件
        - home 存放所有用户文件的根目录
        - lib 存放跟文件系统中的程序运行所需要的共享库及内核模块
        - mnt 系统管理员安装临时文件系统的安装点
        - opt 额外安装的可选应用程序包所放置的位置
        - proc 虚拟文件系统，存放当前内存的映射
        - root 超级用户目录
        - sbin 存放二进制可执行文件，只有root才能访问
        - tmp 用于存放各种临时文件
        - usr 用于存放系统应用程序，比较重要的目录/usr/local 本地管理员软件安装目录
        - var 用于存放运行时需要改变数据的文件
    3. Linux 命令基本格式：
        cmd [options] [arguments]，options称为选项，arguments称为参数
            一般来说，后面跟的选项如果单字符选项前使用一个减号-。单词选项前使用两个减号--
            这是一般的情况，有些命令还是不归属这种规律的(相对较少)~~~
            例子：ls -a和ls -all，a 单个字符使用一个-，一个单词all 使用两个--
        在Linux中，可执行的文件也进行了分类：
            内置命令：出于效率的考虑，将一些常用命令的解释程序构造在Shell内部。
            外置命令：存放在/bin、/sbin目录下的命令
            实用程序：存放在/usr/bin、/usr/sbin、/usr/share、/usr/local/bin等目录下的实用程序
            用户程序：用户程序经过编译生成可执行文件后，可作为Shell命令运行
            Shell脚本：由Shell语言编写的批处理文件，可作为Shell命令运行
    4. 通配符
    在Linux中的通配符(在搜索的时候挺有用的)
        *：匹配任何字符和任何数目的字符
        ?：匹配单一数目的任何字符
        [ ]：匹配[ ]之内的任意一个字符
        [! ]：匹配除了[! ]之外的任意一个字符，!表示非的意思
    
5. 文件的类型
    我们常见的就是普通文件，目录和符号链接。其他的了解一下即可。
    Linux下文件的类型：
        - 普通文件 -
            - 目录 d
            - 符号链接 l
            - 硬链接： 与普通文件没什么不同，inode 都指向同一个文件在硬盘中的区块
            - 软链接： 保存了其代表的文件的绝对路径，是另外一种文件，在硬盘上有独立的区块，访问时- 替换自身路径(简单地理解为 Windows 中常见的快捷方式)。
            - 字符设备文件 c
            - 块设备文件b
            - 套接字s
            - 命名管道p

三、常用的命令

1. 常用的文件、目录操作命令
        tips:输入命令的时候要常用**tab键**来补全
这是我们使用得最多的命令了，Linux最基础的命令！
    可用 **pwd**命令查看用户的当前目录
    可用 **cd** 命令来切换目录
    **.**表示当前目录
    **..** 表示当前目录的上一级目录（父目录）
    **-**表示用 cd 命令切换目录前所在的目录
    **~** 表示用户主目录的绝对路径名
    绝对路径：**/**
    相对路径 ：不以斜线（/）开头
    **ls**：显示文件或目录信息
    **mkdir**：当前目录下创建一个空目录
    **rmdir**：要求目录为空
    **touch**：生成一个空文件或更改文件的时间
    **cp**：复制文件或目录
    **mv：**移动文件或目录、文件或目录改名
    **rm**：删除文件或目录
    **ln：**建立链接文件
    **find**：查找文件
    **file/stat**：查看文件类型或文件属性信息
    **cat**：查看文本文件内容
    **more**：可以分页看
    **less**：不仅可以分页，还可以方便地搜索，回翻等操作
    **tail -10**： 查看文件的尾部的10行
    **head -20**：查看文件的头部20行
    **echo**：把内容重定向到指定的文件中 ，有则打开，无则创建
    管道命令 **|** ：将前面的结果给后面的命令，例如：ls -la | wc，将ls的结果加油wc命令来统计字数
    重定向 **>** 是覆盖模式，**>>** 是追加模式，例如：echo "Java3y,zhen de hen xihuan ni" > qingshu.txt把左边的输出放到右边的文件里去
    
2. 文件解压缩操作
压缩的方式也是有好几种，我们常用的有下面这三种：

    **gzip**
    **bzip2**
    **tar**
常用的压缩的命令就有：

    ****gzip filename**
    **bzip2 filename**
    tar -czvf filename**
常用的解压命令有：

    **gzip -d filename.gz**
    **bzip2 -d filename.bz2**
    **tar -xzvf filename.tar.gz**
   
3. 正则表达式

    1. grep命令

    grep(global search regular expression)是一个强大的文本搜索工具。grep 使用正则表达式搜索文本，并把匹配的行打印出来。

    格式：`grep [options] PATTERN [FILE...]`

    - PATTERN 是查找条件：**可以是普通字符串、可以是正则表达式**，通常用单引号将RE括起来。
    - FILE 是要查找的文件，可以是用空格间隔的多个文件，也可是使用Shell的通配符在多个文件中查找PATTERN，省略时表示在标准输入中查找。
    - grep命令不会对输入文件进行任何修改或影响，可以使用输出重定向将结果存为文件

    例子：

    - 在文件 myfile 中查找包含字符串 mystr的行

      - `grep -n mystr myfile`

    - 显示 myfile 中第一个字符为字母的所有行

      - `grep '^[a-zA-Z]' myfile`

    - 在文件 myfile 中查找首字符不是 # 的行（

      即过滤掉注释行

      ）

      - `grep -v '^#' myfile`

    - 列出/etc目录（包括子目录）下所有文件内容中包含字符串“root”的文件名

      - `grep -lr root /etc/*`

4. **Shell变量 和 Shell环境**

    在Windows下有用户的环境变量，系统的环境变量。在Linux一样也是有的。

    Shell 变量大致可以**分为三类**：

    - 内部变量

      ：由系统提供，用户只能使用不能修改。

      - ?
      - GROUPS

    - **环境变量**：这些变量决定了用户工作的环境，它们不需要用户去定义，可以直接在 shell 中使用，其中某些变量用户可以修改。

    - 用户变量

      ：由用户建立和修改，在 shell 脚本编写中会经常用到。

      - 变量赋值（定义变量）
        - `varName=Value`
        - `export varName=Value`
      - 引用变量`$varName`

    Shell变量的**作用域**：

    - **局部变量**的作用范围仅仅**限制在其命令行所在的Shell或Shell脚本文件中**；
    - **全局变量**的作用范围则包括**本Shell进程及其所有子进程**。
    - 局部变量与全局变量**互换**：可以使用 `export` 内置命令将局部变量设置为全局变量。 可以使用 `export` 内置命令将全局变量设置为局部变量。

    **export命令**：

    - 显示

      当前Shell可见的全局变量

      - `export [-p]`

    - 定义变量值的同时声明为全局变量

      - `export <变量名1=值1> [<变量名2=值2> ...]`

    - 声明已经赋值的某个（些）

      局部变量为全局变量

      - `export <变量名1> [<变量名2> ...]`

    - 声明已经赋值的某个（些）

      全局变量为局部变量

      - `export -n <变量名1> [<变量名2> ...]`

    Shell环境变量：

    - 环境变量定义 Shell 的**运行环境**，保证 Shell 命令的正确执行。
    - Shell用环境变量来确定查找路径、注册目录、终端类型、终端名称、用户名等。
    - 所有环境变量**都是全局变量**（即可以传递给 Shell 的子进程），并可以由用户重新设置。

    四、VI编辑器**

    相信没有用过Linux的同学在看一些段子的时候都会看到过两个编辑器：

    - vim
    - emacs

    下面我们学习如何简单使用vi。vi 是 “Visual interface” 的简称，它可以执行输出、删除、查找、替换、块操作等众多文本操作，而且**用户可以根据自己的需要对其进行定制，这是其他编辑程序所没有的**。

    - vi可以看做成我们Windows下的记事本
    - vim 即 Vi IMproved，vi 克隆版本之一

    使用Vi来编辑文件：

    Vi有三种模式：

     - 普通模式

     - 插入模式

     - 命令行模式

       ![img](.\pic\vim-vi-workmodel.png)

    **1. 普通模式**

    - `G`用于直接跳转到文件尾
    - `ZZ`用于存盘退出Vi
    - `ZQ`用于不存盘退出Vi
    - `/和？`用于查找字符串
    - `n`继续查找下一个
    - `yy`复制一行
    - `p`粘帖在下一行，P粘贴在前一行
    - `dd`删除一行文本
    - `x`删除光标所在的字符
    - `u`取消上一次编辑操作（undo）

    

    **2. 插入模式**

    在 Normal 模式下输入插入命令 `i、 a 、 o`进入insert模式。用户输入的任何字符都被vim**当做文件内容保存起来**，并将其显示在屏幕上。

    - 在文本输入过程中，若想回到Normal模式下，按 Esc 键即可。

    **3. 命令行模式**

    Normal 模式下，用户按冒号 `:`即可进入 Command 模式，此时 vim 会在显示窗口的最后一行 (屏幕的最后一行) 显示一个 “:” 作为 Command 模式的提示符，等待输入命令。

    - `:w` 保存当前编辑文件，但并不退出
    - `:w` newfile 存为另外一个名为 “newfile” 的文件
    - `:wq` 用于存盘退出Vi
    - `:q!` 用于不存盘退出Vi
    - `:q`用于直接退出Vi （未做修改）

    **设置Vi环境:**

    - :set autoindent 缩进,常用于程序的编写
    - :set noautoindent 取消缩进
    - :set number 在编辑文件时显示行号
    - :set nonumber 不显示行号
    - :set tabstop=value 设置显示制表符的空格字符个数
    - :set 显示设置的所有选项
    - :set all 显示所有可以设置的选项


