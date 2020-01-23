

## week 17(date:20190106-20200112)

### Algorithm

##### leetcode 中级算法-篇

1. **填充每个节点的下一个右侧节点指针**：

   题目描述:
   
   给定一个**完美二叉树**，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：
   
   ```
   struct Node {
     int val;
     Node *left;
     Node *right;
     Node *next;
   }
   ```
   
   填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 `NULL`。
   
   初始状态下，所有 next 指针都被设置为 `NULL`。
   
   思路:使用递归，确定递归子问题，是三个节点的时候，为左右节点设置next，分析可知，左节点的next为右节点。右节点的next为null或者为头结点的next的left节点。递归退出条件为当前节点的left或right为null。

```java
class Solution {
    public Node connect(Node root) {
        if(root==null){
            return root;
        }
        root.next=null;
        connnectHelper(root);
        return root;
    }
        
    public void connnectHelper(Node node){
        
        Node lnode=node.left;
        Node rnode=node.right;
        if(lnode!=null){
            lnode.next=rnode;
            if(node.next==null){
                rnode.next=null;
            }else{
                rnode.next=node.next.left;
            } 
            connnectHelper(lnode);
            connnectHelper(rnode);
        }else{
            return;
        }
        成       ·	1 安琪·  }
}
```

### Review

### Activiti User Guide

##### Activiti User Guide：https://www.activiti.org/5.x/userguide/

end（ 3.3. Database configuration）	

##### 单词:

1. distributed 发布

2. distribution 发行版

3. Experimental  实验性的

4. stable 稳定的

5. individually 个别的

6. Alternatively 或者

7. concepts 概念

8. functionality 功能

9. obtain  获得

10.  form  形成

11. getting insight on  深入

12. in fact  事实上

13. leveraging  利用

14. practice  实践

15. transactions  处理

    介绍了如何安装activiti，下载activiti-explorer.war复制到Tomcat的webapps目录中。启动tomacat，

    打开浏览器登录http://localhost:8080/activiti-explorer，默认为h2数据库。配置文件**activiti.cfg.xml**的数据库配置等。

    

### Tips

- 
  

### Share

#### spring框架学习笔记二

#### 	一、spring 的自动扫描与自动装配

​		通常你可以在 xml 配置文件中，声明一个 bean 或者 component ，然后 Spring 容器会检查和注册你的 bean 或 component 。Spring 支持自动扫描 bean 或 component ，你可以不必再在 xml 文件中繁琐的声明 bean ，Spring 会自动扫描、检查你指定包的 bean 或 component 。

```java
package com.shiyanlou.spring.services;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import com.shiyanlou.spring.dao.CustomerDAO;

@Component
public class CustomerService 
{
    @Autowired
    CustomerDAO customerDAO;

    @Override
    public String toString() {
        return "CustomerService [customerDAO=" + customerDAO + "]";
    }
}
```

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:context="http://www.springframework.org/schema/context"
       xsi:schemaLocation="
            http://www.springframework.org/schema/context
            http://www.springframework.org/schema/context/spring-context.xsd
            http://www.springframework.org/schema/beans 
            http://www.springframework.org/schema/beans/spring-beans.xsd">

    <context:component-scan base-package="com.shiyanlou.spring"/>

</beans>
```

##### 自动扫描组件的注释类型

有 4 种注释类型，分别是：

1. @Component ——表示一个自动扫描 component
2. @Repository ——表示持久化层的 DAO component
3. @Service ——表示业务逻辑层的 Service component
4. @Controller ——表示表示层的 Controller component

##### 自动装配bean

Spring 支持 5 种自动装配模式，如下：

- no —— 默认情况下，不自动装配，通过 `ref` attribute 手动设定。
- byName —— 根据 Property 的 Name 自动装配，如果一个 bean 的 name ，和另一个 bean 中的 Property 的 name 相同，则自动装配这个 bean 到 Property 中。
- byType —— 根据 Property 的数据类型（ Type ）自动装配，如果一个 bean 的数据类型，兼容另一个 bean 中 Property 的数据类型，则自动装配。
- constructor —— 根据构造函数参数的数据类型，进行 byType 模式的自动装配。
- autodetect —— 如果发现默认的构造函数，用 constructor 模式，否则，用 byType 模式。

##### 二、spring基于注解的配置

  		1. **@Autowired** 可以用来装配 bean，可以写在字段上，或者方法上。@Autowired 默认按类型装配，默认情况下要求依赖对象必须存在，如果要允许 null 值，可以设置它的 required 属性为 false。
                		2. **@Qualifier**这个注解通常和@Autowired 一起使用，当你想对注入的过程做更多的控制，@Qualifier 可以帮助你指定做更详细配置。一般在两个或者多个 bean 是相同的类型，spring 在注入的时候会出现混乱
            		3. **基于java的配置：**Spring 中为了减少 XML 配置，可以声明一个配置类类对 bean 进行配置，主要用到两个注解@Configuration 和@bean

##### 三、spring框架的AOP

 Spring **AOP** 即 Aspect-oriented programming，面向切面编程，是作为**面向对象编程**的一种**补充**，专门用于处理系统中分布于各个模块（不同方法）中的**交叉关注点**的问题。简单地说，就是一个**拦截器**（ interceptor ）拦截一些处理过程。

例如，当一 个 method 被执行，Spring AOP 能够劫持正在运行的 method ，在 method 执行前或者后加入一些额外的功能。

在 Spring AOP 中，支持 4 种类型的通知（ Advice ）：

- **Before advice** - method 执行前通知
- **After returning advice** - method 返回一个结果后通知
- **After throwing advice** - method 抛出异常后通知
- **Around advice** - 环绕通知，结合了以上三种

在 Spring AOP 中，有 3 个常用的概念，Advices 、 Pointcut 、 Advisor ，解释如下：

- **Advices** ：表示一个 method 执行前或执行后的动作。
- **Pointcut** ：表示根据 method 的名字或者正则表达式去拦截一个 method 。
- **Advisor** ： Advice 和 Pointcut 组成的独立的单元，并且能够传给 proxy factory 对象。