# https://morvanzhou.github.io/tutorials/machine-learning/ML-intro/3-04-activation-function/

# 常用选择 
#  激励函数 (Activation Function)
# 想要恰当使用这些激励函数, 还是有窍门的. 
# 比如当你的神经网络层只有两三层, 不是很多的时候, 对于隐藏层, 使用任意的激励函数, 随便掰弯是可以的, 不会有特别大的影响. 
# 不过, 当你使用特别多层的神经网络, 在掰弯的时候, 玩玩不得随意选择利器. 因为这会涉及到梯度爆炸, 梯度消失的问题. 

# 最后我们说说, 在具体的例子中, 我们默认首选的激励函数是哪些. 
# 在少量层结构中, 我们可以尝试很多种不同的激励函数. 
# 在卷积神经网络 Convolutional neural networks 的卷积层中, 推荐的激励函数是 relu. 
# 在循环神经网络中 recurrent neural networks, 推荐的是 tanh 或者是 relu 