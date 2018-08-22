# -*- coding: utf-8 -*-
import random

def shell_sort(list):
  """希尔排序"""
  n = len(list)
  gap = n // 2
  while gap >= 1:
    for i in range(gap, n):
      while ((i - gap) >= 0 and list[i] < list[i - gap]):
        list[i], list[i - gap] = list[i - gap], list[i]
        i -= gap
    gap //= 2


if __name__ == '__main__':
  list = [random.randrange(100) for i in range(20)]
  print("原列表为：" , list)
  shell_sort(list)
  print("新列表为：" , list)
