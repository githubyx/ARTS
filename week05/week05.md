## week 5(date:20190913-20190929)

### Algorithm

##### leetcode 初级算法-链表篇

1. **删除链表的倒数第N个节点**：https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/6/linked-list/42/
	
	题目描述:
	
		给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
	思路  (时间复杂度：O(n) )：
	
		1. 求出链表的长度。
		2. 遍历链表，找到需要删除的节点的前一个节点，将它的next指向需要删除节点的下一个节点。
		3. 考虑特殊情况，删除的是第一个节点或删除的链表为空。

```java
    public ListNode removeNthFromEnd(ListNode head, int n) {
        if(n<=0||head==null){
            return head;
        }
        ListNode res = head;
        ListNode res1 = head;
        int length=0;
        int index=0;
       //获取链表的长度
        while(head!=null){
            length++;
            head=head.next;

        }
       if(length==1){
           res=null;
           return res;
       }
	   //删除头结点
      if(length==n){
           res=res.next;
           return res;
       }
        while(res1!=null){
            if(index+n+1==length){
                if(res1.next==null){
                    return res;
                }
                res1.next=res1.next.next;
                return res;
            }
            index++;
            res1=res1.next;
        }
        return  res;
    }
```

2. **反转链表**：https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/6/linked-list/43/ 

    题目描述:
	
		反转一个单链表。

    思路(时间复杂度：O(n) ）:

		1. 遍历链表，将节点的next指向前一个节点。
		2. 注意，存储原节点的顺序，需要存储之前的节点。


   ​	代码：

```java
      public ListNode reverseList(ListNode head) {
        ListNode l=head;
        ListNode res=null;
        while(l!=null){
            ListNode temp=l.next;     
            l.next=res;
            res=l;
            l=temp;
        }
        return res;
    }
```

   

### Review

#### Small world with high risks: a study of security threats in the npm ecosystem

##### ：https://blog.acolyer.org/2019/09/30/small-world-with-high-risks/

##### 单词:

1. risks  危险
2. threats 威胁
3. evolution 进化
4. packed  包含
5. quantify 量化
6. maintainers 维护者
7. defence 防御
8. rapidly 迅速
9. formal  通常
10. transitive 传递
11. privileges 权限
12. reliance  依赖
13. potential 潜在性的 
14. responsible 负责
15. concentration  集中
16. implicitly  隐式
17. rely  依赖
18. Vulnerabilities 漏洞
19. disclaimer 免责声明
20. manual  说明书
21. tough 难

##### 文章大意：

​	npm生态系统中的风险研究，npm是服务器与第三方JavaScript软件包的主要来源，是大型重要软件生态的核心。主要讲了npm中存在的几个风险。

1. npm中存在大量传递依赖，导致用户平均安装一个npm软件包需要隐式信赖80个其它软件包。

 	2. 一些受欢迎的软件包，需要依赖的软件包可以达到100000+的其他软件包。
 	3. npm软件包嫉妒具有影响力的维护者影响超过10000+的软件包，极易成为攻击的主要目标。
 	4. 由于存在传递依赖，一些软件包存在的影响是爆炸性的。


### Tips

- 微服务架构
  - 通信机制 **rpc** 、**RESTful**
  - 微服务务拆分：**领域驱动设计（DDD ）**
  - 配置中心：热更新，配置管理（阿波罗配置中心）
  - k8s网址：https://kuboard.cn/learning/k8s-basics/deploy-app.html
  - 分布式事务：**zcc**
  - 开发模式：**devops**
  - 并发控制：**熔断**、**舱体隔离**（资源保护）、**限流**、**回滚。**
  - Iass(基础设施)、Pass(平台)、Sass(软件)

### Share

##### ansible安装:

2、设置每个机器的hostname
hostnamectl --static set-hostname {hostname}
hostnamectl --static set-hostname master1
hostnamectl --static set-hostname master2
hostnamectl --static set-hostname master3
hostnamectl --static set-hostname deploy

3、准备K8s安装介质
将ansible-2019-7-22.zip文件复制到/etc，并执行解压缩
cd /etc
unzip  ansible-2019-7-22.zip

4. 安装Ansible
sudo easy_install pip
pip install ansible==2.6.12
pip install pip --upgrade -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
pip install ansible==2.6.12 -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com

在deploy节点配置免密码登陆

```
#更安全 Ed25519 算法
ssh-keygen -t ed25519 -N '' -f ~/.ssh/id_ed25519
#或者传统 RSA 算法
ssh-keygen -t rsa -b 2048 -N '' -f ~/.ssh/id_rsa

ssh-copy-id $IPs #$IPs为所有节点地址包括自身，按照提示输入yes 和root密码
例：
ssh-copy-id 192.168.100.106
```

5、准备Ansible配置文件

单机版本
cd /etc/ansible && cp example/hosts.allinone hosts
集群版本
cd /etc/ansible && cp example/hosts.m-masters.example hosts
vim hosts
验证ansible 安装：ansible all -m ping

注：配置Yum源服务器,然后执行脚本

1. 
2. ![1569546509078](pic\1569546509078.png)

2. ![1569546666728](pic\1569546666728.png)

3.  执行命令：/opt/app/mountcd.sh  

6、安装K8s

#一步安装
cd /etc/ansible
ansible-playbook 90.setup.yml

7、验证安装
kubectl version
kubectl get componentstatus # 可以看到scheduler/controller-manager/etcd等组件 Healthy
kubectl cluster-info # 可以看到kubernetes master(apiserver)组件 running
kubectl get node # 可以看到单 node Ready状态
kubectl get pod --all-namespaces # 可以查看所有集群pod状态，默认已安装网络插件、coredns、metrics-server等
kubectl get svc --all-namespaces # 可以查看所有集群服务状态
查看etcd服务：
etcdctl --ca-file=/etc/kubernetes/ssl/ca.pem --cert-file=/etc/kubernetes/ssl/kubernetes.pem --key-file=/etc/kubernetes/ssl/kubernetes-key.pem --endpoints=https://192.168.100.102:2379,https://192.168.100.103:2379,https://192.168.100.104:2379 cluster-health
systemctl status etcd

失败的话：ansible-playbook  99.clean.yml

8、K8S Dashboard
cd /etc/ansible
开启（用户名/密码）认证，使用 easzctl basic-auth -s 
BASIC_AUTH_USER: 'admin'
BASIC_AUTH_PASS: ‘18019244cd323c22'

Dashboard地址：kubectl cluster-info
kubernetes-dashboard is running at https://192.168.100.102:6443/api/v1/namespaces/kube-system/services/https:kubernetes-dashboard:/proxy

登录方式：
1、令牌登录（admin）
选择“令牌(Token)”方式登陆，复制下面输出的admin token 字段到输入框
kubectl -n kube-system describe secret $(kubectl -n kube-system get secret | grep admin-user | awk '{print $1}')

##### k8s中部署微服务:
1. 文件内容：G:\微服务学习相关\Day2\K8sCase

2. 上传docker镜像

3. 执行:docker load <./example-cloud-eureka.tar  && docker load <./example-db-example.tar && docker load <./example-gateway.tar  && docker load <./example-svc-example.tar   && docker load <./example-web-example.tar

4. 在控制台登录:http://192.168.20.128:32567
1. 创建命名空间：example
2. 导入工作负载 ![1569654943002](pic\1569654943002.png)
3. 导入kuboard_example.yaml文件
![1569655046078](pic\1569655046078.png)
4. 点击下一步，选择emptyDir，点击下一步![1569655082471](pic\1569655082471.png)

5. 登录控制台，上传exposewebsvc.yaml

6. 执行：kubectl create -f exposewebsvc.yaml -n example

7. 查看时候部署成功：docker images |grep example 或者 kubectl get pods -n example

8. 登录http://192.168.20.128:30008/，看到页面表示部署成功。


