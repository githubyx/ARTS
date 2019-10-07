1. 文件内容：G:\微服务学习相关\Day2\K8sCase

2. 上传docker镜像

3. 执行:docker load <./example-cloud-eureka.tar  && docker load <./example-db-example.tar && docker load <./example-gateway.tar  && docker load <./example-svc-example.tar   && docker load <./example-web-example.tar

4. 在控制台登录:http://192.168.20.128:32567
    1. 创建命名空间：example

    2. 导入工作负载 ![1569654943002](pic\1569654943002.png)

    3. 导入kuboard_example.yaml文件

       ![1569655046078](pic\1569655046078.png)

    4. 点击下一步，选择emptyDir，点击下一步![1569655082471](pic\1569655082471.png)





4. 登录控制台，上传exposewebsvc.yaml
5. 执行：kubectl create -f exposewebsvc.yaml -n example
6. 查看时候部署成功：docker images |grep example 或者 kubectl get pods -n example
7. 登录http://192.168.20.128:30008/，看到页面表示部署成功。