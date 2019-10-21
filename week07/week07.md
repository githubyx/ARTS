## week 7(date:20191014-20191020)

### Algorithm

##### leetcode 初级算法-篇

1. **二叉树的最大深度**：https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/7/trees/47/
	
	题目描述:
	
	​		给定一个二叉树，找出其最大深度。二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。 
   思路  (时间复杂度：O(n) )：
	
	1. 递归判断树的右边子树是否大于左子树，大于的话树的最大深度为右子树+1.否则为左子树+1;
	2. 递归结束条件为子树为空。

```java
        public int maxDepth(TreeNode root) {
        int len=0;
        if(root==null){
            return 0;
        }
        int rightMax=maxDepth(root.right);
        int leftMax=maxDepth(root.left);
        if(rightMax>leftMax){
            return rightMax+1;
        }else{
            return leftMax+1;
        }

    }
```

2. **验证二叉搜索树**：https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/7/trees/48/

    题目描述:
	
		假设一个二叉搜索树具有如下特征：
		节点的左子树只包含小于当前节点的数。
    	    节点的右子树只包含大于当前节点的数。
		所有左子树和右子树自身必须也是二叉搜索树。
	
	思路(）:
    
    ​	自己的代码未考虑（节点要大于右子树的值，节点要小于右子树的值）：

   ```java
       public boolean isValidBST(TreeNode root) {
           if(root==null){
               return true;
           }
           // if(root.left==null&&root.right==null){
           //    return true;
           // }
           if(root.left!=null&&root.right==null){
               if(root.left.val>=root.val){
                   return false;
               }
              return isValidBST(root.left);
           }
           if(root.right!=null&&root.left==null){
               if(root.right.val<=root.val){
                   return false;
               }
               return isValidBST(root.right);
           }
           if(root.right!=null&&root.left!=null){
                if(root.left.val>=root.val||root.right.val<=root.val){
                   return false;
               }
               return isValidBST(root.left)&&isValidBST(root.right);
           }
           return true;
       }
   ```
   
   ​	代码：

```java
  public boolean helper(TreeNode node, Integer lower, Integer upper) {
    if (node == null) return true;

    int val = node.val;
    if (lower != null && val <= lower) return false;
    if (upper != null && val >= upper) return false;

    if (! helper(node.right, val, upper)) return false;
    if (! helper(node.left, lower, val)) return false;
    return true;
  }

  public boolean isValidBST(TreeNode root) {
    return helper(root, null, null);
  }
```

   

### Review

## Machine Learning Algorithms Explained – K-Means Clustering

##### ：https://blog.easysol.net/machine-learning-algorithms-3/

##### 单词:

1. clustering 聚类
2. behind  背后
3. decision  决策
4. corresponding  相当的
5. hints 暗示
6. fixed  固定
7. cluster 类、簇
8. iterative 重复的
9. assign 分配
10. corresponding  相当的
11. Euclidean 欧几里得
12. correspond  一致
13. measurements  测量值
14. plot 绘制
15. decide  决定
16. traditional  传统
17. straightforward  直接
18. extreme 极端
19. ideal  理想
20. competitive  竞争力
21. completely  完全地


##### 文章大意：

介绍k-means的算法思路。

​		K均值通过随机定义*k个*质心开始。从那里开始，它以迭代（重复）步骤工作以执行两项任务：

1. 使用标准欧几里得距离将每个数据点分配给最接近的对应质心。用外行术语来说：数据点和质心之间的直线距离。
2. 对于每个质心，计算属于它的所有点的值的平均值。平均值成为质心的新值。

步骤2完成后，所有质心都有新值，这些新值对应于它们所有相应点的均值。这些新点将通过第一步和第二步产生另一组质心值。一遍又一遍地重复此过程，直到质心值没有变化为止，这意味着它们已被正确分组。或者，当满足先前确定的最大步骤数时，可以停止该过程。

**k-means算法的优缺点**

K-均值的优点：

- 广泛用于聚类分析的方法
- 容易理解
- 快速训练

K-均值的缺点：

- 欧几里德距离在许多应用中都不理想
- 性能（通常）与最佳聚类方法没有竞争力
- 数据中的细微变化会导致完全不同的聚类（高方差）
- 假定群集具有球形形状并且大小均匀




### Tips

- ***

    - 

### Share
**scrapy  爬虫框架入门**

scrapy 官网（https://scrapy.org/）

scrapy api（https://docs.scrapy.org/en/latest/）

一、 安装scrapy

​		1. 安装 python3（下载安装）

　　2. 安装 scrapy:   `pip install scrapy` 

二、 创建scrapy项目:**mp4ba**

​	项目目标：爬取：[http://www.mp4ba.com] 电影网站全部资源的磁力下载链接、网盘链接，保存为csv文件。

![1571666318368](.\pic\1571666318368.png)

 1. 在命令行输入命令：`scrapy startproject  mp4ba` 在当前文件夹生成项目。在spider 文件夹下新建文件**Mp4baSpider.py**

    ![1571664672091](.\1571664672091.png)



2. 编写Mp4baSpider.py 文件

   ```python
   import scrapy
   import logging
   from mp4ba.items import Mp4BaItem
   class Mp4baSpider(scrapy.Spider):
       name = "mp4ba"
       allowed_domains = ["www.mp4ba.com"]
       start_urls = [
           "http://www.mp4ba.com/"
       ]
   
       def parse(self,response):
           top_selector=response.xpath('/html/body/section/div[1]/nav/ul/li/a/@href')
           # yield scrapy.Request(url=top_selector.extract()[3],callback=self.indexMp4ba)
           for top_url in top_selector.extract():
               yield scrapy.Request(url=top_url,callback=self.indexMp4ba)
   
       def indexMp4ba(self, response):
           nextpage_selector=response.xpath('//*[@id="page"]/a[@class="nextpage"]/@href')
           for nextpage_url in nextpage_selector.extract():
               yield scrapy.Request(nextpage_url,callback=self.indexMp4ba)
   
           item_selector=response.xpath('/html/body/section/div[4]/div[1]/div/div[2]/ul/li/a/@href')
           for item_url in item_selector.extract():  
               yield scrapy.Request(url=item_url,callback=self.detailMp4)
   
   
       def detailMp4(self,response):
           baiduYun_selector=response.xpath('//*[@id="fadecon"]/div[4]/ul/li')
           cl_720p_selector=response.xpath('//*[@id="fadecon"]/div[3]/ul/li/div/a[2]/@href')
           bt_720p_selector=response.xpath('//*[@id="fadecon"]/div[3]/ul/li/div/a[1]/@href')
           mv_type=response.xpath('/html/body/section/div[2]/a[3]/text()').extract_first()
           bt_720p=bt_720p_selector.extract_first()
           cl_720p=cl_720p_selector.extract_first()
           name=response.xpath('//*[@class="info_tit"]/text()').extract_first()
           for i in baiduYun_selector:
               item=Mp4BaItem()
               item["type"]=i.xpath('text()').extract()[0].replace(" ","").replace("\n","").replace("\t","").replace("\r","").replace("：","")
               item["path"]=i.xpath('div[@class="btn-group cloud"]/a/@href').extract_first()
               item["code"]=i.xpath('div[@class="btn-group cloud"]/p/text()').extract_first()
               item["cl_720p"]=cl_720p
               item["bt_720p"]=bt_720p
               item["name"]=name
               item["mv_type"]=mv_type
               item["url"]=response.url
               yield item
   ```

   **解释说明：**

   			-  start_urls 为爬虫的入口，下载网页回调默认回调到**parse()** 方法，可以重写该方法。
   			-  response.xpath()  对返回的内容进行xpath选取html元素。
   			-  top_selector.extract() ： 对该元素获取列表值。
   			-  extract_first() ： 只获取一个值
   			-   scrapy.Request(nextpage_url,callback=self.indexMp4ba)  ：访问nextpage_url地址网页 并将内容返回给**indexMp4ba()** 方法

3. 编写item文件、确定需要爬取数据的模型。

   ```python
   # -*- coding: utf-8 -*-
   
   # Define here the models for your scraped items
   #
   # See documentation in:
   # https://doc.scrapy.org/en/latest/topics/items.html
   
   import scrapy
   
   
   class Mp4BaItem(scrapy.Item):
       # define the fields for your item here like:
       id=scrapy.Field()
       url=scrapy.Field()
       name=scrapy.Field()
       path=scrapy.Field()
       type=scrapy.Field()
       code=scrapy.Field()
       bt_720p=scrapy.Field()
       cl_720p=scrapy.Field()
       mv_type=scrapy.Field()
       pass
   
   class Mp4BaInfoItem(scrapy.Item):
       # define the fields for your item here like:
       id=scrapy.Field()
       name=scrapy.Field()
       bj=scrapy.Field()
       zy=scrapy.Field()
       lx=scrapy.Field()
       dq=scrapy.Field()
       yy=scrapy.Field()
       sysj=scrapy.Field()
       xkSjc=scrapy.Field()
       pc=scrapy.Field()
       pf=scrapy.Field()
       jj=scrapy.Field()
       pass
   
   ```

   解释说明

   - 继承：**scrapy.Item**
   - 编写类字段：**scrapy.Field()**

4. 根据需要修改setting.py 配置文件。

5. 执行命令保存数据到csv文件。

   1. 执行 `scrapy crawl mp4ba -o mp4ba.csv`
   2. excel直接打开乱码的话，修改文件编码为ANSI。