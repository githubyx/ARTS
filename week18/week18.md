

## week 18(date:20190113-20200119)

### Algorithm

##### leetcode 中级算法-篇

1. **给定一个没有重复数字的序列，返回其所有可能的全排列**（https://leetcode-cn.com/explore/interview/card/top-interview-questions-medium/49/backtracking/93/）。

   示例:
   
   ```
   输入: [1,2,3]
   输出:
   [
     [1,2,3],
     [1,3,2],
     [2,1,3],
     [2,3,1],
     [3,1,2],
     [3,2,1]
   ]
   
   ```
   
   通用回溯模板（https://leetcode-cn.com/problems/permutations/solution/hui-su-suan-fa-xiang-jie-by-labuladong-2/）：
   
   ```
   for 选择 in 选择列表:
       # 做选择
       将该选择从选择列表移除
       路径.add(选择)
       backtrack(路径, 选择列表)
       # 撤销选择
       路径.remove(选择)
       将该选择再加入选择列表
   ```
   
   初始状态下，所有 next 指针都被设置为 `NULL`。
   
   思路:使用递归，确定递归子问题，是三个节点的时候，为左右节点设置next，分析可知，左节点的next为右节点。右节点的next为null或者为头结点的next的left节点。递归退出条件为当前节点的left或right为null。

```java
List<List<Integer>> res = new ArrayList<>();

List<List<Integer>> permute(int[] nums) {
    LinkedList<Integer> track = new ArrayList<>();
    backtrack(nums, track);
    return res;
}

// 路径：记录在 track 中
// 选择列表：nums 中不存在于 track 的那些元素
// 结束条件：nums 中的元素全都在 track 中出现
void backtrack(int[] nums, ArrayList<Integer> track) {
    // 触发结束条件
    if (track.size() == nums.length) {
        res.add(new ArrayList(track));
        return;
    }
    
    for (int i = 0; i < nums.length; i++) {
        if (track.contains(nums[i]))
            continue;
        // 做选择
        track.add(nums[i]);
        // 进入下一层决策树
        backtrack(nums, track);
        // 取消选择
        track.removeLast();
    }
}
```

### Review

### Activiti User Guide 2

##### Activiti User Guide：https://www.activiti.org/5.x/userguide/

end（ 3.17 Mapped Diagnostic Contexts）	

##### 单词:

1. optional 可选择的

2. instructions 指令

3. suitable  适当的

4. manually 手工

5. identity  身份

6. various  各式各样

7. upgrade 升级

8. specified 指定

9. counterparts 副本

10. activation 激活

11. exposes  暴露

12. additional  附加的

    介绍了如何升级数据库。作业的执行，历史记录的配置。配置邮件服务器，日志文件的配置、缓存的配置、日志文件的配置等等。


### Tips

- 
  

### Share

#### spring框架学习笔记三

#### 	一、Spring 的事务管理

​		**事务的四个特性**：

- 原子性（Atomicity）：事务是一个原子操作，由一系列动作组成。事务的原子性确保动作要么全部完成，要么完全不起作用。
- 一致性（Consistency）：一旦事务完成（不管成功还是失败），系统必须确保它所建模的业务处于一致的状态，而不会是部分完成部分失败。在现实中的数据不应该被破坏。
- 隔离性（Isolation）：可能有许多事务会同时处理相同的数据，因此每个事务都应该与其他事务隔离开来，防止数据损坏。
- 持久性（Durability）：一旦事务完成，无论发生什么系统错误，它的结果都不应该受到影响，这样就能从任何系统崩溃中恢复过来。通常情况下，事务的结果被写到持久化存储器中。

Spring 中有**两种事务管理**的方式，一种是编程式事务管理，另一种是声明式事务管理。

​		编程式事务管理：所谓编程式事务指的是通过编码方式实现事务，允许用户在代码中精确定义事务的边界。即类似于 JDBC 编程实现事务管理。管理使用 TransactionTemplate 或者直接使用底层的 PlatformTransactionManager。对于编程式事务管理，spring 推荐使用 TransactionTemplate。

​		声明式事务管理：管理建立在 AOP 之上的。其本质是对方法前后进行拦截，然后在目标方法开始之前创建或者加入一个事务，在执行完目标方法之后根据执行情况提交或者回滚事务。声明式事务最大的优点就是不需要通过编程的方式管理事务，这样就不需要在业务逻辑代码中掺杂事务管理的代码，只需在配置文件中做相关的事务规则声明(或通过基于@Transactional 注解的方式)，便可以将事务规则应用到业务逻辑中。

**编程式事务管理:**

```java
    public void transfer(final String outer,final String inner,final int money) {
        transactionTemplate.execute(new TransactionCallbackWithoutResult() {
            @Override
            protected void doInTransactionWithoutResult(TransactionStatus arg0) {
                accountDao.out(outer, money);
                int i = 1/0;
                accountDao.in(inner, money);
            }
        });
    }
```

```xml
     <!-- 配置事务管理器 ,管理器需要事务，事务从Connection获得，连接从连接池DataSource获得 -->
    <bean id="txManager" class="org.springframework.jdbc.datasource.DataSourceTransactionManager">
        <property name="dataSource" ref="dataSource"></property>
    </bean>
```

**声明事务管理**：

```xml
<!-- xml 1 事务管理器 -->
    <bean id="txManager" class="org.springframework.jdbc.datasource.DataSourceTransactionManager">
        <property name="dataSource" ref="dataSource"></property>
    </bean>
    <!-- 2 将管理器交予spring
        * transaction-manager 配置事务管理器
        * proxy-target-class
            true ： 底层强制使用cglib 代理
    -->
    <tx:annotation-driven transaction-manager="txManager" proxy-target-class="true"/>
```

```java
@Transactional(propagation=Propagation.REQUIRED , isolation = Isolation.DEFAULT)
@Service("accountService")
public class AccountServiceImpl implements AccountService{
    @Resource(name="accountDao")
    private AccountDao accountDao;

    public void setAccountDao(AccountDao accountDao) {
        this.accountDao = accountDao;
    }
    @Override
    public void transfer(String outer, String inner, int money) {
        accountDao.out(outer, money);
        //int i = 1/0;
        accountDao.in(inner, money);
    }

}
```