"""Самая быстрая из известных мне сортировок это быстрая сортировка,
	быстрее сортировки пузырьком, слиянием, вставками и выбором
	из за того что делит массив пополам и сортирует его относительно
	границы одной из цифр на каждой итерации, """

import random
def sortQ(nums):
	if len(nums) <= 1:
		return nums
	else:
		rip = random.choice(nums)
		Up_nums = []
		Dow_nums = []
		Equ_nums = []
		for nn in nums:
			if nn < rip:
				Up_nums.append(nn)
			elif nn > rip:
				Dow_nums.append(nn)
			else:
				Equ_nums.append(nn)
		return sortQ(Up_nums) + Equ_nums + sortQ(Dow_nums)

def main(x):
	l = sortQ(x)
	print(l[0:10])

if __name__ == '__main__':
	x = [random.randint(1, 10000000000000000) for i in range(1000000)]
	main(x)
