# https://morvanzhou.github.io/tutorials/machine-learning/ML-intro/3-07-imbalanced-data/

# 这个简介视频的最后一种方法是让自己变得有创造力, 尝试修改算法. 
# 如果你用的是 Sigmoid 的激励函数, activation function, 他会有一个预测门槛, 
# 一般如果输出结果落在门槛的这一段,预测结果为梨, 如果落在这一段, 预测结果为苹果, 
# 不过因为现在的梨是多数派, 我们得调整一下门槛的位置, 使得门槛偏向苹果这边, 
# 只有很自信的时候, 模型才会预测这是苹果. 让机器学习,学习到更好的效果.