

### SQL 是怎么运作的




 
##### MapReduce

我们先理解一下 MapReduce, 

几个基础的概念和名词需要先记住：

1.首先 JobClient 是用户的终端, 发送一个 Job 的Jar 包 __(作业包)__ 到每个DataNode, (__数据节点)

2.然后把作业提到 JobTracker 服务器, 然后进入


##### 数据倾斜 (Hive)


首先要理解 Map -> Reduce 在sql 里的运作机制
