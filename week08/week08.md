## week 8(date:20191021-20191027)

### Algorithm

##### leetcode 初级算法-篇

1. **二叉树的层次遍历**：https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/7/trees/50/
	
	题目描述:
	
	​		给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。
   思路  ：
	
	​		题目为广度优先遍历，通过参数level控制数据的层次。

```java
class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> res=helper(root,0);
        return res;
        
        
    }
    List<List<Integer>> res =new ArrayList<List<Integer>>();
    public List<List<Integer>> helper(TreeNode root,int level) {
        if(res.size()==level){
            res.add(new ArrayList<Integer>());
        }
        res.get(level).add(root.val);
        
        if(root.left!=null){
            helper(root.left,level+1);
        }
        if(root.right!=null){
            helper(root.right,level+1);
        }
        return res;
    }
       
}
```

2. **验证二叉搜索树**：https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/7/trees/48/

    题目描述:
	
		将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。
		
    	本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
	
	思路(）:
	
    与二分查找相似。把数组劈开一半，中间的值赋给父节点，左边右边怎么半？继续递归！直到半边只有一个或者没有元素 就停下来。
    
```java
   	public TreeNode sortedArrayToBST(int[] nums) {
   		return ToBST(nums,0,nums.length-1);
   	}
   	public static TreeNode ToBST(int nums[],int left,int right){
   		if(left>right)return null;//、
   		int mid = (int)(left+right)/2;//二分中值
   		TreeNode root = new TreeNode(nums[mid]);
   		root.left = ToBST(nums,left,mid-1);//对左半部分进行递归
   		root.right = ToBST(nums,mid+1,right);//对右半部分进行递归
   		return root;
   	}
   ```
   

### Review

## Machine Learning Algorithms Explained - Decision Trees

##### ：https://blog.easysol.net/machine-learning-algorithms-1/

##### 单词:

1. decision  决定/决策
2. independently  独立
3. typically   通常
4. discrete or continuous  离散或连续
5. concept 概念
6. illustrate 阐明
7. measurements  测量值
8. represents 代表
9. pure 纯净
10. criteria  标准
11. determined  决定
12. subset 子集
13. quantitative  定量/量化
14. measure 测量
15. entropy  熵
16. impurity 不纯的
17. aggregate  合计
18. represents  表示
19. interpretable 解释


##### 文章大意：

介绍决策树。

		决策树是一种树形结构，其中每个内部节点表示一个属性上的测试，每个分支代表一个测试输出，每个叶节点代表一种类别。

分类树（决策树）是一种十分常用的分类方法。是一种监管学习，根据给定的训练数据集构造一个决策树模型，使得它能够对样本进行正确的分类。

决策树算法。

​     选择一个最优特征：根据这个特征将训练数据分割成子集，使得各个子集有一个在当前条件下最好的分类（若这些子集已能够被基本正确分类，则将该子集构成叶结点；若某个子集不能够被基本正确分类，则对该子集选择新的最优的特征，继续对该子集进行分割，构建相应的结点。）

​     如此递归下去，直至所有训练数据子集都被基本正确分类，或者没有合适的特征为止。

​    上面的生成过程容易发生**过拟合**问题，决策树解决过拟合的方法通常是对树进行剪枝，从而使得决策树具有更好的泛化能力。决策树的生成对应着模型的局部最优，剪枝则考虑了全局最优。

​		特征选择在决策树模型构建中起着至关重要的作用，常用的特征选择指标有：信息增益和信息增益比。这两个指标刻画了特征的分类能力。决策树常用的生成算法有两种：ID3和C4.5。

###### 优缺点

- 决策树的优势：

  - 可用于回归或分类
  - 可以图形化、容易解释
  - 可以指定为一系列规则，比其他模型更接近人类的决策
  - 预测很快

  决策树的缺点：

  - 通常最佳监督学习方法不具有竞争力
  - 容易过拟合
  - 在很小的数据集上往往无法很好地工作




### Tips

- 

### Share
**吴恩达机器学习视频**

机器学习概念：机器学习是一门人工智能的科学，该领域的主要研究对象是人工智能，特别是如何在经验学习中改善具体算法的性能。

分类：

- 监督学习：从给定的训练数据集中学习出一个函数，当新的数据到来时，可以根据这个函数预测结果。
	- 分类 ：用去预测离散型数据。
	- 回归：用于预测连续性数据
- 无监督学习：无监督学习与监督学习相比，训练集没有人为标注的结果。
  - 聚类

##### 机器学习算法：

1. 机器学习模型：

​	一个训练集通过一个算法得到一个函数（用于拟合测试数据）：

![img](D:\ARST\week08\pic\{494064CF-C28B-9E93-6E72-CDB665AE4904}.jpg)



2. 代价函数：

![img](D:\ARST\week08\pic\{B042A74F-86D2-6CFB-E302-AC17461388E0}.png)

​	说明： 代价函数表示拟合函数的预测值与实际值的误差。

​	通过求解代价函数的最小值，求出拟合函数的参数值，确定拟合函数。

​	如何求解参数，通过梯度下降法更新参数，知道代价函数的误差最小。

3. 梯度下降法

   ![img](D:\ARST\week08\pic\{9326D8DE-0D76-FE55-2D7D-F0FF4D3DD89B}.png)
   
   
   
   梯度下降法解释：假设你在一个山坡上，如何最快的走到山脚下，可以通过这种方式：环绕周围找到一个最陡峭的路径，向下走一步。重复这个步骤，直到走到山脚下。
   
   问题：梯度下降法可能会限于局部最优。



​		

