矩阵元素查找
=============

# 一. 问题描述

> 有一个NxM的整数矩阵，矩阵的行和列都是从小到大有序的。请设计一个高效的查找算法，查找矩阵中元素x的位置。给定一个int有序矩阵mat，同时给定矩阵的大小n和m以及需要查找的元素x，请返回一个二元数组，代表该元素的行号和列号(均从零开始)。保证元素互异。测试样例：[[1,2,3],[4,5,6]],2,3,6，返回：[1,2]。

# 二. 求解

> 从右上角开始，每次将搜索值与右上角的值比较，如果大于右上角的值，则行+1，否则，则列-1。如下图显示了查找13的轨迹。首先与右上角15比较，13<15，所以列-1，然后与11比较，这是13>11，行+1，以此类推，最后找到13。算法复杂度O(n)，最坏情况需要2n步，即从右上角开始查找，而要查找的目标值在左下角的时候。

![image](https://github.com/ShaoQiBNU/Matrix-element-search/blob/master/images/1.jpg)

> 代码如下：

```python
class Finder:
    def findElement(self, mat, n, m, x):
        # write code here
        i=0
        j=m-1
        while i<n and j>=0:
            if mat[i][j]==x:
                return [i,j]
            elif mat[i][j]>x:
                j=j-1
            else:
                i=i+1
```
