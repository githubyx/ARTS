## week 8(date:20191028-20191103)

### Algorithm

##### leetcode 初级算法-篇

1. **第一个错误的版本**：https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/8/sorting-and-searching/53/

   题目描述:

```
你是产品经理，目前正在带领一个团队开发新的产品。不幸的是，你的产品的最新版本没有通过质量检测。由于每个版本都是基于之前的版本开发的，所以错误的版本之后的所有版本都是错的。

假设你有 n 个版本 [1, 2, ..., n]，你想找出导致之后所有版本出错的第一个错误的版本。

你可以通过调用 bool isBadVersion(version) 接口来判断版本号 version 是否在单元测试中出错。实现一个函数来查找第一个错误的版本。你应该尽量减少对调用 API 的次数。
```

思路(）:

通过二分查找如何在每次操作中减少一半的搜索空间，以此减少时间复杂度。

- isBadVersion(mid) 返回 false，因此我们知道mid 左侧（包括自身）的所有版本都是正确的。所以我们令 min=mid+1，把下一次的搜索空间变为[mid+1,right]

- isBadVersion(mid) 返回 true，因此我们知道mid 右侧（不包括自身）的所有版本的不可能是第一个错误的版本。所以我们令 right=mid，把下一次的搜索空间变为 [left,mid]。

  

```java
public class Solution extends VersionControl {
    public int firstBadVersion(int n) {
        int min=0;
        int max=n;
        while(min<max){
            int mid=min+(max-min)/2;
            if(!isBadVersion(mid)){
                min=mid+1;
            }else{
                max=mid;
            }
        }

        return min;
    }
}
```


### Review

## Machine Learning Algorithms Explained - Random Forests

##### ：https://blog.easysol.net/machine-learning-algorithms-2/

##### 单词:

1. forests 森林
2. ensemble 整体
3. aggregate  集合/聚合
4. Bias-Variance Tradeoff 偏差方差平衡
5. bias and variance 偏差 和 方差
6. illustrate  举例
7. spread out  分布
8. simplifying assumptions 简单假设
9. capacity  能力
10. complex  复杂
11. accurate 准确
12. individual  个体
13. generalize  概括
14. preferences 偏好
15.  varied 改变
16. biased  偏见
17. correlated 相关
18. criteria  标准
19. extreme  极端
20. recommended  推荐


##### 文章大意：

机器学习算法解释：随机森林

		随机森林是一个包含多个决策树的分类器，并且其输出的类别是由个别树输出的类别的众数而定。

任何机器学习模型都有两个来源：偏差和误差

***偏差***是一种错误，当算法做出太多简化假设时，会导致它预测与实际值不同的值。

***方差***是由于算法对训练数据集中的微小变化敏感而导致的错误；较高的方差意味着算法将更受数据细节的影响。

决策树算法。

  随机森林是一种**减少方差**的方法。决策树的特点是高方差和低偏差。随机森林通过汇总各个决策树的不同输出来减少可能导致决策树错误的方差。通过多数决策树的表决，我们可以找到大多数单棵树给出的平均输出，从而**平滑方差**，这样该模型就不太可能产生远离真实值的结果。

**随机森林**的**随机**的含义：随机挑选训练数据的**不同子集**来训练每个单独的决策树，并且使用从数据中随机选择的属性来拆分每个决策树的每个节点。通过引入随机性的元素，创建**彼此不相关的模型**。

###### 优缺点

- 随机森林的优势：

  - 不需要特性标准化
  - 可并行化：可以并行训练单个决策树
  - 被广泛使用的
  - 减少过度拟合

  决策树的缺点：

  - 不容易解释
  - 不是最先进的方法




### Tips

- 

### Share
#### **吴恩达机器学习视频2**

##### 矩阵向量介绍：

矩阵加减法，[2,3]-[1,1]=[1,2]

矩阵乘法：

![](pic\{356AA650-7E2D-A1B2-6A1D-F5AB8302CCAE}.png)

单位矩阵：对角线都为1 其他都为0；

逆矩阵：逆矩阵与该矩阵相乘为单位矩阵。

#### 多元线性回归

假设函数：h(x)

![img](pic\{9326D8DE-0D76-FE55-2D7D-F0FF4D3DD89B}.png)

**多元线性回归参数**的更新规则，左侧为一元线性回归，右侧为多元线性回归参数更新规则。

![img](pic\{C37AC158-FF6A-D264-3B52-EAAA203C57B9}.png)

特征缩放： 将特征范围缩放到 -1<x<1 之间，需要考虑特征值得范围。

##### 多元梯度下降法：

学习率的设置，当代价函数不收敛时（随着x增加，y无法一直下降），考虑使用更小的学习率。

学习率过小会导致，收敛速度变慢。学习率的选取可以考虑3的倍数（0.01,0.03,0.1,0.3...1）。

![](pic\{CAAFAAE1-D583-B72B-3233-5CA902F69FAC}.png)

多项式回归： 使用参数替换，可以方便实现，如下图。对于特征例如房子的长宽，可以使用房子的面积代替。

![img](pic\{DDB6DCA3-519E-0827-FBFB-A0AB33CB26EE}.png)



​		

