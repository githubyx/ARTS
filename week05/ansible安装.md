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

    #更安全 Ed25519 算法
    ssh-keygen -t ed25519 -N '' -f ~/.ssh/id_ed25519
    #或者传统 RSA 算法
    ssh-keygen -t rsa -b 2048 -N '' -f ~/.ssh/id_rsa
    
    ssh-copy-id $IPs #$IPs为所有节点地址包括自身，按照提示输入yes 和root密码
    例：
    ssh-copy-id 192.168.100.106

5、准备Ansible配置文件

单机版本
cd /etc/ansible && cp example/hosts.allinone hosts
集群版本
cd /etc/ansible && cp example/hosts.m-masters.example hosts
vim hosts
验证ansible 安装：ansible all -m ping

注：配置Yum源服务器,然后执行脚本

1. 
2. ![1569546509078](C:\Users\yx\AppData\Roaming\Typora\typora-user-images\1569546509078.png)

2. ![1569546666728](C:\Users\yx\AppData\Roaming\Typora\typora-user-images\1569546666728.png)

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

