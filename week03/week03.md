## week 3(date:20190909-20190915)
###  Algorithm
##### leetcode 初级算法-字符串篇
1. 反转字符串：https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/5/strings/32/

   题目描述:编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 `char[]` 的形式给出。不要给另外的数组分配额外的空间，你必须**原地修改输入数组**、使用 O(1) 的额外空间解决这一问题。

   思路  (时间复杂度：O(n) )：

   找出数组的中间位置,分析数组长度为奇偶数的情况，可以将下标为【i】与【s.length/2-i-1】进行交换。

```java
    public void reverseString(char[] s) {
        int len=s.length;
        for(int i=0;i<len/2;i++){
            char temp=s[i];
            s[i]=s[len-i-1];
            s[len-i-1]=temp;
        }
    }
```

2. 字符串转换整数 (atoi):https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/5/strings/37/ 

   题目描述:
   	请你来实现一个 atoi 函数，使其能将字符串转换成整数。

   首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。

   当我们寻找到的第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字组合起来，作为该整数的正负号；假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成整数。

   该字符串除了有效的整数部分之后也可能会存在多余的字符，这些字符可以被忽略，它们对于函数不应该造成影响。

   注意：假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换。

   在任何情况下，若函数不能进行有效的转换时，请返回 0。

   思路(时间复杂度：O(n) ）:

    1.  删除空格，判断第一个字符的符号位。
    2.  判断每个字符是否是数字，如果是数字计算结果。不是数字直接返回结果，每次循环判断是否超过了最大整数，或者最小整数。


​	代码：

  ```java
public int myAtoi(String str) {
        long res=0;
        String strt=str.trim();
        if (strt.length() == 0){
            return 0;
        }
        int sign=1;
        int start=0;
        if(strt.charAt(0)=='-'){
            sign=-1;
            start++;
        }
        if(strt.charAt(0)=='+'){
            start++;
        }
        for(int i=start;i<strt.length();i++){
            if(strt.charAt(i)>'9'||strt.charAt(i)<'0'){
                return (int) res*sign;
            }
            if(strt.charAt(i)<='9'&&strt.charAt(i)>='0'){
                res=res*10+strt.charAt(i)-'0';
            }
            if(sign==1&&res>Integer.MAX_VALUE){
                System.out.print(Integer.MAX_VALUE);
                return Integer.MAX_VALUE;
            }
            if(sign==-1&&-res<Integer.MIN_VALUE){
                return Integer.MIN_VALUE;
            }
        }

        return (int) res*sign;
    }
  ```

### Review

#### Scalability! But at what COST?

##### ：http://dsrg.pdos.csail.mit.edu/2016/06/26/scalability-cost/

##### 单词:

1. scalability  可扩展性
2. the holy grail 圣杯
3. go over 复习
4. summary  总结
5. thoughts  想法
6. get around to 抽出时间来
7. take a summer break 放暑假
8. evaluated 评估
9. field  领域
10. research  调查
11. factor 因素
12. scale  拓展
13. magnitude 量级
14. despite 尽管
15. threshold  门槛
16.  refer to 涉及
17. predecessors  前任
18. sufficient 足够的
19. sufficient 充分的
20. unfortunately 不幸的
21. massive  大规模
22. argue 争论
23. variety 多种
24. get away with 侥幸逃脱
25. reap significant benefits.  显著获得好处

##### 文章大意：

大多数分布式计算研究，大多数都重视*可扩展性*，忽略性能如何随着使用更多计算资源而变化。如果一个系统具易于 *并行化的开销*，那么系统看起来可以很好地扩展，但是它的绝对性能很差。可以考虑通过牺牲可扩展性（即分布性），使用*更好的算法*，这可以显着加快计算速度，提高性能。大规模使用分布式的原因是，没法定义问题有多大，不使用分布式能否满足要求，分布式系统的性能提升成本较大。

### Tips

- ##### kettle：
  
     - kettle window下无法运行，可以试着修改Spoon.bat文件将
     
       `if "%PENTAHO_DI_JAVA_OPTIONS%"=="" set PENTAHO_DI_JAVA_OPTIONS="-Xms1024m" "-Xmx2048m" "-XX:MaxPermSize=256m"`修改为
     
       `if "%PENTAHO_DI_JAVA_OPTIONS%"=="" set PENTAHO_DI_JAVA_OPTIONS="-Xms512m" "-Xmx512m" "-XX:MaxPermSize=256m"`

- **windows网卡设置问题：**
  - windows下设置固定IP失败，系统会自动设置ip。解决方法：先禁用网卡，重启网卡。重新装网卡驱动。这些方式都不行，好像是由于操作系统引起的，建议重装系统。



### Share
##### Kettle简单使用说明:
1. **kettle简介：**Kettle是一款国外开源的ETL工具，纯java编写，可以在Windows、Linux、Unix上运行，[数据抽取](https://baike.baidu.com/item/数据抽取/218221)高效稳定。Kettle 中文名称叫水壶，该项目的主程序员MATT 希望把各种数据放到一个壶里，然后以一种指定的格式流出。下载地址：https://community.hitachivantara.com/s/article/data-integration-kettle

2. **kettle基础导数据流程：**

   ​		导入数据的基本流程如下图，可以分为三个步骤，首先建立源数据库和目标数据库的连接，然后建立源数据表和目标数据表的映射关系，最后建立作业任务，执行。

   ![](.\pic\pic.png)*

   **2.1 建立DB连接**

   ​	1.  导入需要了解数据库的驱动。将驱动jar包放到lib文件夹下。

   ​	2.  配置数据库连接![](.\pic\picdb.png)

   **2.2 建立steps**
   这一步实现源数据库和目标数据表的映射关系，它也有三个步骤
   **2.2.1 表输入**
   第一步：在【转换】里面，选择【核心对象】，接着双击【表输入】，或者选中将【表输入】拖拽到右侧空白区域。

   第二步：双击你拖进来的【表输入】，修改“步骤名称”，选择源数据，点击获取【获取SQL查询语句】，选择你想同步的表，点击确定后，就可以了。当然你也可以自己写sql语句

   **2.2.2 字段选择**
   第一步：在【转换】里面，拖拽【字段选择】到右侧空白区域。
   第二步：按住shift 拖动鼠标连接【客户基本信息输入】和 【字段选择】
   第三步：双击【字段选择】，添加【列映射】，建立源表和目标表中列字段的映射，如果字段名称相同，kettle会自动帮你选择，如果不同，则需要你自己选择对应关系

   第四步：这一步可选，当源数据字符集与目标字符集不同的时候需要做字符转换，如果一致，则直接跳过这一步

   **2.2.3 表输出**
   第一步：在【转换】拖拽【表输出】到右侧空白区域，按住shift 拖动鼠标连接【字段选择】和【基本信息输出】

   第二步：双击【表输出】，修改“步骤名称”，选择“数据库连接”，选择“目标表”，

   第三步：获取字段，因为在【字段选择】中已经做了匹配，所以这里可以全选，kettle可以帮你全部选择

   第四步： ctrl+s 保存 ktr文件

   **3 建立作业**
   	新建作业

   **3.1 设置START**
   拖拽【START】到右侧空白区域

   **3.2 配置作业转换**
   第一步：拖拽【转换】到右侧空白区域，并按住shift 拖动鼠标连线

   第二步：双击【转换】选择需要的ktr文件，保存即可。

   第三步：手工运行作业，点击下图红色圈圈里面的按钮。

   第四步：在下面的窗口查看日志。

   **3.3 定时执行**

   如果不想立即执行，那么可以选择制定的规则，让kettle定期执行。具体操作，可双击【START】，更改“类型”。

   运行的时候，选择Start Job at 【start】就可以了。