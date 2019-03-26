# https://morvanzhou.github.io/tutorials/machine-learning/ML-intro/2-6-GAN/

# 生成网络 
#  生成对抗网络 (GAN)
# 但是还有另外一种形式的神经网络, 他不是用来把数据对应上结果的, 而是用来”凭空”捏造结果, 这就是我们要说的生成网络啦. 
# GAN 就是其中的一种形式. 那么 GAN 是怎么做到的呢? 当然这里的”凭空”并不是什么都没有的空盒子, 而是一些随机数.

#  生成对抗网络 (GAN)
# 对, 你没听错, 我们就是用没有意义的随机数来生成有有意义的作品, 比如著名画作. 
# 当然, 这还不是全部, 这只是一个 GAN 的一部分而已, 这一部分的神经网络我们可以想象成是一个新手画家.


# GAN 应用 
#  生成对抗网络 (GAN)
# 甚至你还能玩点新花样, 比如让图片来做加减法, 戴眼镜的男人 减去 男人 加上 女人, 他居然能生成 戴眼镜的女人的图片. 
# 甚至还能根据你随便画的几笔草图来生成可能是你需要的蓝天白云大草地图片. 哈哈, 看起来机器也能有想象力啦. 
# 如果你想试着动手做一个 GAN 的实践, 却不知道如何做, 
# 不用担心, 我也为准备好了一个使用 Python 和他神经网络模块搭建的最简单的 GAN 实践代码.