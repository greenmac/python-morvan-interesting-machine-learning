# https://morvanzhou.github.io/tutorials/machine-learning/ML-intro/2-2-CNN/

# 池化(pooling) 
#  卷积神经网络 CNN (Convolutional Neural Network)
# 研究发现, 在每一次卷积的时候, 神经层可能会无意地丢失一些信息. 
# 这时, 池化 (pooling) 就可以很好地解决这一问题. 而且池化是一个筛选过滤的过程, 
# 能将 layer 中有用的信息筛选出来, 给下一个层分析. 同时也减轻了神经网络的计算负担 (具体细节参考). 
# 也就是说在卷集的时候, 我们不压缩长宽, 尽量地保留更多信息, 压缩的工作就交给池化了,这样的一项附加工作能够很有效的提高准确性. 
# 有了这些技术,我们就可以搭建一个属于我们自己的卷积神经网络啦.

# 流行的 CNN 结构 
#  卷积神经网络 CNN (Convolutional Neural Network)
# 比较流行的一种搭建结构是这样, 从下到上的顺序, 首先是输入的图片(image), 经过一层卷积层 (convolution), 
# 然后在用池化(pooling)方式处理卷积的信息, 这里使用的是 max pooling 的方式. 
# 然后在经过一次同样的处理, 把得到的第二次处理的信息传入两层全连接的神经层 (fully connected),这也是一般的两层神经网络层,
# 最后在接上一个分类器(classifier)进行分类预测. 这仅仅是对卷积神经网络在图片处理上一次简单的介绍. 