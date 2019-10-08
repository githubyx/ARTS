## week 6(date:20190930-20191006)

### Algorithm

##### leetcode 初级算法-链表篇

1. **合并两个有序链表**：https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/6/linked-list/44/
	
	题目描述:
	
		将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
	思路  (时间复杂度：O(n) )：
	
		1. 使用两个指针分别指向l1和l2，当l1的值大于等于l2,l2的指针加一，否者l1指针加一。将数值存到结果链表res中。
		2. 只到其中一个链表为空，则将另一个链表剩余的链直接加到结果链表res中。

```java
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode res=new ListNode(0);
        ListNode curr=res;
        while(l1!=null||l2!=null){
            if(l1==null){
                curr.next=l2;
                break;
            }            
            if(l2==null){
                curr.next=l1;
                break;
            }
            if(l1.val>=l2.val){  
                curr.next=l2;
                curr=curr.next;
                l2=l2.next;
            }else{
                curr.next=l1;
                curr=curr.next;
                l1=l1.next;
            }
            
        }

        return res.next;
        
    }
```

2. **回文链表**：https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/6/linked-list/45/

    题目描述:
	
		请判断一个链表是否为回文链表。

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

#### The secret-sharer: evaluating and testing unintended memorization in neural networks

##### ：https://blog.acolyer.org/2019/09/23/the-secret-sharer/

##### 单词:

1. unintended  无意识的

##### 文章大意：

在

### Tips

- ##### Oracle：

  - 





### Share

2. 


