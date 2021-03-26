"""
    In clasa asta bagam mancarurile.
"""
__author__ = 'cristiprg'

from sortedcontainers import SortedSet  # http://www.grantjenks.com/docs/sortedcontainers/sortedset.html
import math
import random

def FUNCTIA(x, y):
    c1 = 20
    c2 = 0.2
    c3 = 2*math.pi

    return -c1 * math.exp(-c2 * math.sqrt(1/2 * (x**2 + y**2))) - \
        math.exp(1/2 * (math.cos(c3*x) + math.cos(c3*y))) + c1 + math.e


class Solution:
    """
    The bee.
    """
    def __init__(self, x=None, y=None):
        self.x = x or 0
        self.y = y or 0

        self.speedReductionFactor = 0.5  # S(t+1) = alpha * S(t), deci, intre 0 si 1 (pag 665)
        self.energyReductionAmount = 45  # E(t+1) = E(t) - gamma, deci intre 0 si 100? Gandim in procente aici?

        self.speed = 100  # ???
        self.energy = 100  # 100%???

        self.probabilityToMateDroneThreshold = 0.10

    def __lt__(self, other):
        if isinstance(other, Solution):
            return self.getFitness() < other.getFitness()
        else:
            raise Exception("Class Soultion compared with other class.")

    def getFitness(self):
        """
        :return:
            The fitness function of this solution.
            这个解的适应度函数。
            Acuma, o consideram diferenta fata de 0, pentru ca stim deja ca minimul e 0 ... si care mai ii rostu' atunci?
            INTREBARE: ce functie de fitness am alege daca nu stim ca raspunsul este 0?

            V2: tot functia lui Gauss daca tot stim ca raspunsul (parametrul b) este 0.
            现在，我们考虑它和O的区别，因为我们已经知道最小值是0。。。那是什么意思？

            问题：如果我们不知道答案是0，我们会选择什么适应度函数？
        """
        return math.exp(-(FUNCTIA(self.x,self.y)**2)/100)  # c=100 ca sa fie numere mai normale

    def probabilityToMateDrone(self, drone):
        """
        与雄峰交配的概率
        Computes to probability that this solution (the queen, hopefully) will pick
        the drone in the mating dance.
        计算出蜂王在婚飞过程中会选择与雄峰交配的概率
        :param drone:
        传入参数 雄峰
        :return: a float in interval [0, 1] representing the probability.
        返回一个[0, 1]之间的浮点数表示概率
        """
        if isinstance(drone, Solution):
            return math.exp(-abs(self.getFitness() - drone.getFitness()) / self.speed)
        else:
            raise Exception("Drone not of type Solution")

    def nextIteration(self):
        """
        Supposing this is the queen, the following parameters have to updated at each iteration:
            speed,
            energy
           假设这是蜂王，蜂王的飞行速度和能量必须在每一次迭代中更新
        :return:
        """
        self.speed *= self.speedReductionFactor
        self.energy -= self.energyReductionAmount

    def numberOfBroodsWithDrone(self, drone):
        """
        Computes the number of broods this queen makes with the drone based on:
        根据以下公式计算蜂王与无人机的孵卵数：
            The queen's energy
            The drone's fitness value
            A random float number in interval [0, 1]
        :param drone:
        :return: An non-negative integer
        返回一个非负整数
        """
        return int(self.energy * drone.getFitness() * random.uniform(0, 1))

    def createBroods(self, drone):
        """
        Provides a set of solutions derived from this queen. Runs the genotypes combination
        algorithm for each new brood.
        提供了一组由此派生的解决方案。为每个新的孵卵运行基因型组合算法。
        :param drone:
        :return: A sorted set of solutions.
        返回一组排序的solutions
        """
        if not isinstance(drone, Solution):
            raise Exception("Drone not of type Solution")

        nr_broods = self.numberOfBroodsWithDrone(drone)
        broods = SortedSet()

        for i in range(nr_broods-1):
            brood = self.combineGenotypes(drone)
            broods.add(brood)

        return broods

    def combineGenotypes(self, drone):
        """
        Runs the genotypes combination algorithm for this queen and the drone.
        为蜂王和雄峰运行基因型组合算法
        :param drone:
        :return: A new solution (brood).
        """

        x = self.x if random.getrandbits(1) else drone.x
        y = self.y if random.getrandbits(1) else drone.y
        return Solution(x, y)

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

