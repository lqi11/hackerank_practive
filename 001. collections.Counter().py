import collections

number_of_shoes = int(input())
sizes_in_stock = collections.Counter(map(int,input().split()))

total_revenue = 0

for _ in range(int(input())):
    size, price = map(int, input().split())
    if sizes_in_stock[size]: # every time counter -=1, when size use out, it is 0
        total_revenue += price
        sizes_in_stock[size] -= 1

print(total_revenue)