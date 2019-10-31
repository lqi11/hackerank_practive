
def secondLowestGrade(classList):
    secondLowestScore = sorted(set(_[1] for _ in classList))[1] #sort by [1]
    # print(secondLowestScore)
    result = sorted([_[0] for _ in classList if _[1] == secondLowestScore])
    return result

if __name__ == '__main__':
    numberOfStudents = int(input())
    classList = []
    for i in range(numberOfStudents):
       classList.append([str(input()), float(input())])
    print("\n".join(secondLowestGrade(classList)))
