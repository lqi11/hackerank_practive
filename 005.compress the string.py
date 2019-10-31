
from itertools import groupby
# for x, c in groupby((input())):
#     print(list(c))
# ['1']
# ['2', '2', '2']
# ['3']
# ['3']
print(*[(len(list(c)), int(x)) for x, c in groupby((input()))])