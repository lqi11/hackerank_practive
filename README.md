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
