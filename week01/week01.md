## week 1(date:20190816-20190901)
###  Algorithm
#### leetcode 初级算法-数组篇
1. 存在重复元素（contains-duplicate）：https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/1/array/24/
题目描述:给定一个整数数组，判断是否存在重复元素。
如果任何值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false。
思路：
  
  1. 遍历两次数组。判断nums[i] 在后面的 i+1 -->nums.length-1 中是否重复。时间复杂度为O(n^2)。（超时未通过！）

  2. 使用hashmap。遍历一次数组,时间复杂度为O(n)，每次遍历判断nums[i] 是否在map 中，不在则put，如果存在则返回 true;（ps：可以使用hashset保存）
  代码:
  
    ```
    public boolean containsDuplicate(int[] nums) {
      Map<Integer,Integer> map =new HashMap<Integer,Integer>();
      for(int i=0;i<nums.length;i++){
          if(map.containsKey(nums[i])){
              return true;
          }else{
              map.put(nums[i],1);
        }
  }
  return false;
  }
  ```

2. 旋转数组
  题目描述：给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。要求使用空间复杂度为 O(1) 的 原地 算法。
  思路：
  1.将数组向右移动1位。遍历数组 i[1->n-1]与i[0]交换。实现数组元素向右移动一位。
  2.将步骤1执行k次。
  代码:

  ```
  public void rotate(int[] nums, int k) {
         for(int j=0;j<k;j++){
           for(int i=0;i<nums.length;i++){
           int t=nums[i];
           nums[i]=nums[0];
           nums[0]=t;
           }
         }
  
  }
  ```

  


### R
#### 微服务:https://martinfowler.com/articles/microservices.html:
word:
    1. definition ：定义
    2. term :学术、术语
    3. sprung :跳出
    4. particular :特别的
    5. independently :独立的
    6. deployable 可部署的
    7. precise :精确的
    8. characteristics :特征
    9. capability:能力
    10. automated :自动化
    11. intelligence ：智能
    12. decentralized ：去中心化的
    13. crowded:拥挤的
    14. streets：街道
    15. inclination:倾向
    16. a contemptuous glance:轻视
    17. appealing:吸引人的
    18. positive：积极地
    19. approach :处理
    20. developing :发展
    21. lightweight mechanism:轻量级的机制
    22. independently:独立的
    23. centralized :集中地
    24. storage :存储
    25. monolithic：整体的
    26. unit：单元
    27. logic：逻辑
    28. retrieve ：检索
    29. server-side：服务端
    30. divide up：分配
    31. laptop:便携式电脑
    32. production:产品
    33. load-balancer:负载均衡
    34. frustrations ：挫折
    35.a firm module boundary：坚固的模块边界
    36. principles ：原则

### T
- mybatis：
    -  <if test="input!=null and input!=''" /> 当input的数据类型为整数时，不能使用 input!=''进行判断，因为mybatis会将0当成''。
- spring mvc接收参数。
    - @RequestParam("name") ：url?name=xxx 接收name的值，默认required=true，必传。
    - @PathVariable ：@GetMapping("/testGet2/{paramName}") 获取url中占位符的值。
    - 使用对象接收参数： 前端使用form 表单提交。
    - @RequestBody ：需要 Content-Type=application/json 且参数为json字符串，(使用json.stringify()将js对象转为json字符串)

### S
#### 数据中台:
对数据中台的理解：
数据中台定义：对核心数据的管理、处理、展示。
出发点：核心数据是有价值的。（ps：不建设数据中台能发现得吧...，难道是相信以后人工智能通过数据发现价值。）
痛点：统一企业数据，方便分析企业核心业务。
难点：制定规范。需要整合梳理各个业务系统的表，抽象出统一的数据层为上层的数据展示分析等提供基础数据。需要各个部门直接的协调配合，将数据的分而治之转为中央集权。
建设方法论：
    1. 梳理整个企业的核心数据。指定指标，制定数据规范。
    2. 实现业务系统的数据更新，保证数据质量，根据规范制定数据原始指标。
    3. 开发数据生成工具。基于数据生成数据产品。