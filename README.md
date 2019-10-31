# hackerank_practive
#20191030
nestedList 
1. sorted(set(_[1]) for _in classList) use second item in classList to set and sort
2. name, *line = input().split() *line means line is list
3. print(d) (d is deque) print result is deque(['1', '2']), *d result (1,2)
5. every time counter -=1, when size use out, it is 0
6. namedtuple: {:.2f} format, namedtuple('Student', input()) Point = namedtuple('Point','x,y')
>>> pt1 = Point(1,2)
the first line, input the name of list, the name of list can be a string. 
#20191031
8. OrderedCounter can be used directed by : 
class OrderedCounter(Counter, OrderedDict):
    pass
9. OrderedCounter(inside can use sorted()).most_common function
10. set, can use > to compare, all() all true or not
11. usage of set's symmetric_difference, union, difference
12.usage of discard of set: won't throw an error if the item to be removed doesn't exist
13. usage of set difference_update, symmetric_difference_update
14. this one more like a math problem
15. usage of itertools, permutation, product
16. difference between combination_with_replacment and combination. combination(string, number of combination)
16+1, itertool, groupby, for c,x in groupby(): c is # ['1'] # ['2', '2', '2'] # ['3'] # ['3']
18. .*\+ .*+, "+" itself means one or more letter continuing. if we want use "+", it need "\+"
