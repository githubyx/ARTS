## week 3(date:20190916-20190923)

### Algorithm

##### leetcode 初级算法-字符串篇

1. **整数反转**：https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/5/strings/33/

   题目描述:

   ​	给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

   ​	**注意:**假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31,  2^31 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
   
   思路  (时间复杂度：O(n) )：
   
   1. 将数字转化为字符数组，判断数字的符号位。
     2. 根据符号位依次反转数组，将反转后的数组计算结果。
     3. 判断数组范围是否在[−2^31,  2^31 − 1]范围

```java
    public int reverse(int x) {
        String rt=String.valueOf(x);
        char[] rtc=rt.toCharArray();
        long res=0;
        int sign=1;
        int start=0;
        if(rt.charAt(0)=='-') {
            sign = -1;
            start++;
        }
       	//反转除符号位以外的整数
        for(int i=start;i<(rtc.length+start)/2;i++){
            char t=rtc[i];
            rtc[i]=rtc[rtc.length-i+start-1];
            rtc[rtc.length-i+start-1]=t;
        }
        //计算反转后的结果
        for(int i=start;i<rtc.length;i++){
            res=res*10+rtc[i]-'0';
        }
        if(res*sign<Integer.MIN_VALUE||res*sign>Integer.MAX_VALUE)
            return 0;
        return (int)res*sign;
    }
```

2. **验证回文字符串**：https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/5/strings/37/ 

   题目描述:
   	给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

   思路(时间复杂度：O(n) ）:

   1. 遍历字符串，将数字与字母保存到StringBuilder 中。
   2. 判断字符串是否是回文串，即是否是轴对称。
   
   
   ​	代码：

```java
  public boolean isPalindrome(String s) {
        s=s.toLowerCase();
        StringBuilder stringBuilder=new StringBuilder();
        if(s==null||s.length()==0)
            return true;
        for(int i=0;i<s.length();i++){
            if((s.charAt(i)>='a'&&s.charAt(i)<='z')||(s.charAt(i)>='0'&&s.charAt(i)<='9')){
                stringBuilder.append(s.charAt(i));
            }
        }
        for(int i=0;i<stringBuilder.length()/2;i++) {
            if(stringBuilder.charAt(i)!=stringBuilder.charAt(stringBuilder.length()-1-i)){
                return false;
            }
        }
        return true;
    }
```
3. **最长公共前缀** :https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/5/strings/40/

   题目描述:
   	编写一个函数来查找字符串数组中的最长公共前缀。如果不存在公共前缀，返回空字符串 `""`。

   思路(时间复杂度：O(n^2) ）:

   1. 找出数组长度最短的数组。
   2. 遍历该数组的下标。
   3. 如果其他数组的值与该数值一致且下标是起始位置则添加该值。

   代码：

   ```java
       public String longestCommonPrefix(String[] strs) {
           if(strs.length<1){
               return "";
           }
           StringBuilder stringBuilder=new StringBuilder();
           //记录最短的字符串
           String t=strs[0];
           for(int i=0;i<strs.length;i++){
               if(strs[i].length()<t.length()){
                   t=strs[i];
               }
           }
           if(t.length()==0){
               return "";
           }
           int start=0;
           for(int i=0;i<t.length();i++){
               char tc=t.charAt(i);
               int flage=1;
               for(int j=0;j<strs.length;j++){
                   if(tc!=strs[j].charAt(i)){
                       flage=-1;
                   }
               }
               //判断下标是否是起始位置
               if(flage==1&&start==i){
                   stringBuilder.append(tc);
                   start++;
               }
           }
   
           return stringBuilder.toString();
   
       }
   ```

   

### Review

#### The secret-sharer: evaluating and testing unintended memorization in neural networks

##### ：https://blog.acolyer.org/2019/09/23/the-secret-sharer/

##### 单词:

1. unintended  无意识的
2. memorization  记忆
3. neural    神经
4. broader  广泛
5. implications   影响
6. consequences  结果
7. accompanying  陪伴
8. Disclosure  披露
9. particular  特别的
10. sequences  序列
11. sensitive  敏感
12. rare 稀有
13. assume 假定
14. precise  精确
15. accident 事故
16. revealing  揭示
17. Compose 组成
18. scale 规模
19. demonstration 示范
20. sufficiently  充分的
21. capacity  记忆
22. strategy  战略
23. greedy  贪婪的
24. fascinating 迷人
25. threshold 阈值
26. prevent 预防

##### 文章大意：

在分类或预测自然语言文本序列的神经网络模型中，会暴露敏感信息，即使敏感或私人训练数据文本非常少见，人们也能训练有素的模型可以发现一些敏感信息。使用这些模型的用户可能偶然或有意输入某些文本前缀导致模型补全信息，导致敏感信息泄露。

### Tips

- ##### Oracle：

  - 创建多个实例，需要连接某个实例 需要设置：`export ORACLE_SID=orclyx`

  - startup 失败报错

    `ORA-01078: failure in processing system parameters`
    `LRM-00109: could not open parameter file '/u01/app/oracle/product/11.2.0/db_1/dbs/initorclyx.ora'`

    需要在在 /u01/app/oracle/product/11.2.0/db_1/dbs/下找不到initorclyx.ora文件,于是去$ORACLE_HOME/admin/igorclyx/pfile下，找到文件init.ora.1242014234024，然后将文件拷贝到/u01/app/oracle/product/11.2.0/db_1/dbs/目录下，并重命名为initorclyx.ora后，问题解决！




### Share

##### Linux （[RedHat](http://www.linuxidc.com/topicnews.aspx?tid=10) Enterprise Linux 6.9）安装oracle 11g:

1. **VMWare 安装RedHat** 

   1. `下载VMWare软件并安装、下载RedHat镜像

   2. 配置好虚拟机设置后启动虚拟机。

      1. 想要使用xshell在物理机连接的。需要设置。

         ![](pic\1568616311991.png)

         2. 在步骤5中可以设置dhcp连接，在ifconfig中查看ip，进行连接。或者`vi /etc/sysconfig/network-scripts/ifcfg-ens* `，【ifcfg-ens*】为网卡名称

            修改为`BOOTPROTO=dhcp`

   3. 进入系统安装界面，选择第一个项目【install or upgrade an existing system】

   4. 选择第一个选项开始安装，当出现[Disc Found]选择skip跳过检查Iso镜像.

   5. 然后点击下一步，选择语言，选择键盘语言,然后选择第一个选项。

   6. 系统问你是否丢弃磁盘数据，这里选择丢弃.

   7. 然后系统提示分区操作，这里我们选择最后一个，即手动创建分区.

   8. 新建分区步骤如下:

      1：点击创建，在挂载点处选择/boot，这个用于存储引导信息，其他选项默认

      2：点击创建，挂载点为空，文件格式选择swap，大小设置为你物理机RAM的1或2倍，这个分区相当于windows下的虚拟内存.

      3：点击创建，在挂载点处选择/，这个就是你的Home文件夹了，大小选择”使用全部可用空间”.

   9.  点击下一步，选择第一个选项，安装系统到硬盘。这里需要注意一下，如果是使用U盘装物理机系统的朋友，这个选项把/dev/sda改为/dev/sdb,这里的a表示你的第一块硬盘，b表示第二的启动介质，因为系统会把硬盘作为第一引导介质，所以在物理机安装真实系统的朋友要注意了，而且还要把镜像在写入后再拷贝一份到U盘.

   10. 点击下一步，这里根据自己的工作需要进行选择，这里我选择基础服务器.

   11. 点击下一步开始安装.

2. **安装oracle**：详细查看oracle静默安装.md。


