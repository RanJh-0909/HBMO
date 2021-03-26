"""
    Generate the initial solutions.
    生成初始解决方案
"""

__author__ = 'cristiprg'

from sortedcontainers import SortedSet  # http://www.grantjenks.com/docs/sortedcontainers/sortedset.html
from Solution import Solution
import random

MIN = -5
MAX = 5
NR_INITAL_SOLUTIONS = 1000
"""
初始解
"""


def generateInitialSolutions():
    """
        Aicia vine Honey Bee Colony in actiune.
        Deocamdata facem random
        艾西亚蜂群开始行动。现在，我们是随机的。
    :return:
        A SortedSet filled with random solutions
        充满随机解的分类集
    """
    solutions = SortedSet()
    for i in range(NR_INITAL_SOLUTIONS - 1):
        x = random.uniform(MIN, MAX)
        y = random.uniform(MIN, MAX)
        solutions.add(Solution(x, y))
    return solutions


def getSolutions():
    return generateInitialSolutions()