#!/usr/data/bin/python3
import math

def main():
    number_of_ingredients = int(input())
    qty_of_each_ing_req = input().split()
    qty_of_each_ing_avl = input().split()

    max_num = None
    for x in range(0, number_of_ingredients):
        ing_req = int(qty_of_each_ing_req[x])
        ing_avl = int(qty_of_each_ing_avl[x])

        num = math.floor(ing_avl/ing_req)

        if max_num is None:
            max_num = num
        else:
            if num < max_num:
                max_num = num

    print(max_num)

main()

