# https://morvanzhou.github.io/tutorials/machine-learning/ML-intro/3-03-choose-feature/
import matplotlib.pyplot as plt
import numpy as np
#定義400個樣本
gold, chihh = 400, 400 
#平均身高假設為40釐米加上一個隨機數，金毛隨機幅度稍微大些，吉娃娃小些

gold_height = 40 + 10 * np.random.randn(gold)
chihh_height = 25 + 6 * np.random.randn(gold)
#柱狀圖視覺化顯示這些高度資料，紅色金毛高度個數，藍色代表吉娃娃
plt.hist([gold_height, chihh_height], stacked=True, color=['r', 'b'])
plt.show()

# 同样还是这张图片, 如果我想让机器学习预测从 A 走到 B 的时间, 如果我有两种输入特征信息可以选, 
# 一种是 A, B的经纬度, 另一种是 AB间的距离. 虽然这些信息都属于地理位置的信息, 不过让计算机计算经纬度可能会比计算距离麻烦很多. 
# 所以我们在挑选特征信息的时候也要加上这一条, 避免复杂的信息. 
# 因为在特征与结果之间的关系越简单, 机器学习就能越快的学到东西.

# 所以, 在选择特征的时候,我们得要时刻回想起这三点. 
# 避免无意义的信息, 
# 避免重复性的信息, 
# 避免复杂的信息. 
# 这就是我们这次机器学习简介中所聊到的如何区分好用的特征. 