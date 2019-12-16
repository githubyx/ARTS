## week 14(date:20191209-20191215)

### Algorithm

##### leetcode 中级算法-篇

1. **两数相加**：https://leetcode-cn.com/explore/interview/card/top-interview-questions-medium/31/linked-list/82/

   题目描述:
   
   给出两个 **非空** 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 **逆序** 的方式存储的，并且它们的每个节点只能存储 **一位** 数字。
   
   如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
   
   您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
   
   **示例:**
   
   ```
   输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
   输出：7 -> 0 -> 8
   原因：342 + 465 = 807
   ```
   
   思路:

```java
public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode res=new ListNode(0);
        ListNode abc=res;
        int over=0;
        while(l1!=null||l2!=null){
            if(l1==null){
                int val;
                if(l2.val+over>9){            
                    val=l2.val+over-10;
                    over=1;
                }else{
                    val=l2.val+over;
                    over=0;
                }
                res.next=new ListNode(val);
                l2=l2.next;
                res=res.next;        
                continue;
            }
            if(l2==null){
                int val;
                if(l1.val+over>9){            
                    val=l1.val+over-10;
                    over=1;
                }else{
                    val=l1.val+over;
                    over=0;
                }
                res.next=new ListNode(val);
                l1=l1.next;
                res=res.next;
                continue;
            }
 
            if(l1.val+l2.val+over>9){         
                res.next=new ListNode(l1.val+l2.val+over-10);
                l1=l1.next;
                l2=l2.next;
                res=res.next;
                over=1;

            }else{  
                res.next=new ListNode(l1.val+l2.val+over);
                l1=l1.next;
                l2=l2.next;
                res=res.next;
                over=0;
            }

        }
        if(over==1){
            res.next=new ListNode(1);
        }
        return abc.next;
    }

```

### Review

## Deep Learning Tutorial for Beginners 2

### Artificial Neural Network (ANN)

##### ：https://www.kaggle.com/kanncaa1/deep-learning-tutorial-for-beginners

##### 单词:

1. slope 斜坡
2. derivative  导数/派生物
3. term  学术
4. hyperparameter  超参数
5. mathematic 数学的
6. gradients 渐变
7. conclusion 结论
8. artificial  人造的
9. tuned 调整
10. scaling 缩放比例
11. basically 主要的
12. hidden  layer   隐藏层
13.  pretty 漂亮的
14. stick  坚持
15. 

​    介绍了ANN 人工神经网络。深度学习（deep learning）deep的含义是有多少隐藏层。

- 两层神经网络,中间的为隐藏层，头尾分别为输入层和输出层。

  ![1576422941404](assets/1576422941404.png)

  对于图像的案例，有4096个输入层，对于a1来说每个输入层，使用线性函数进行求和后，经过一个激活函数，生成a1。a1与其他a2,a3 经过线性函数求和到输出层，输出层经过激活函数,判断分类类型。

### Tips

- 

### Share

##### 《疯狂Java讲义（第2版）》 读书笔记三

#### **一、多线程**

- ###### 线程概述

  - 进程和线程
  - 进程的特性（独立性、动态性、并发性）
  - 线程也被称作轻量级进程。线程是进程的执行单元，线程不拥有系统资源。与该进程所拥有的的全部资源。
  - 线程是独立运行的、抢占式的。

- ###### 线程的创建与启动

  - Java多线程实现的多种方式

  1. 继承Thread类创建线程

     1. 重写run**方法
     2. 使用start()启动线程。

  2. 实现Runnable接口创建线程（可以共享同一线程类的实例属性）

     1. 定义Runable接口实现类、重写run方法。
     2. 创建Runable实现类实例，并且以此实例作为Thread的target来创建Thread对象。`new Thread(Runnable实现类的对象)`
     3. 调用线程对象的start()方法启动该线程。

  3. 使用Callable和Future创建线程

     特点

     1. 提供了call()方法可以作为线程执行体，比run()方法更强大。
        1. 可以有返回值
        2. 可以抛出异常

     创建线程步骤：

     	1. 创建Callable接口的实现类，并实现call()方法，该call()方法作为线程执行体，并且有返回值。
      	2. 创建Callable实现类的实例，使用FutureTask类包装Callable对象，该FutureTask对象封装了该Callable对象的call()方法的返回值。
      	3. 使用FutureTask对象作为Thread对象的target创建并且启动新线程。
      	4. 调用FutureTask对象的get()方法获得子线程执行结束后的返回值。

 - ###### 线程的生命周期

   ​	线程的生命周期主要包括新建、就绪、阻塞、运行、死亡。下面是**线程状态的转化图**：

   ​	![1575804771146](assets/1575804771146.png)

- ##### 控制线程

  - join()方法：让一个进程等待另一个进程的完成。
  - sleep()方法：让当前的线程暂停一段时间，并且进入阻塞状态。
  - yield()方法：让当前的线程暂停，不会阻塞线程，只是进入就绪状态，让线程调度器重新调度一次。
  - 线程优先级：线程的优先级1-10,数值越大优先级越高。可以使用setPriority()设置优先级。

- ##### 线程同步

  线程调度具有随机性，多线程访问同一个数据，容易出现线程安全问题。

  - **使用 synchronized 关键字**（可以修饰方法、代码块，不能修饰构造器、属性等）
    - 同步代码块
    - 同步方法
  - 使用同步锁Lock()方法（使用ReentrantLock对象实例在方法体中的开始lock.lock锁定，方法体执行结束lock.unlock()解锁）

- ##### 线程通信（需要使用同步监视器，需要使用synchronized修饰。可以是同步代码块或者同步方法。如果使用Lock对象，则需要使用Condition控制线程通信。）

  - wait() :使当前线程等待，直到其他线程调用该同步监视器的notify()或者notifyAll()方法唤醒该线程。
  - notify()：唤醒等待单个线程，如果有多个，随机选择其中一个。
  - notifyAll()：方法唤醒等待所有线程。

- ##### 线程池

  系统启动一个新线程的成本比较高，为了提高性能，使用线程池可以很好提高性能。对于多cpu，使用**ForkJoinPool**将一个任务分解成多个小任务并行计算，将多个小任务的结果合并成总的计算结果。

  使用线程池执行线程任务的步骤

  1. 调用Executors类的静态工厂方法创建ExecutorService对象，该对象代表线程池。

  2. 创建Runnable实现类或Callable的类实例作为线程执行体。

  3. 调用ExecutorService对象的submit() 方法提交Runnable实现类或Callable的类实例

  4. 使用ExecutorService对象的shutdown()方法关闭线程池。

     

  

