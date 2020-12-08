# Have the function QuestionsMarks(str) take the str string parameter, which will contain single digit numbers, letters,
# and question marks, and check if there are exactly 3 question marks between every pair of two numbers that add up to
# 10. If so, then your program should return the string true, otherwise it should return the string false.
# If there aren't any two numbers that add up to 10 in the string, then your program should return false as well.

def question_marks(string):
    # loop through all part of string and find the numbers
    index = []
    numbers = []
    for a in range(len(string)):
        # try to convert to number
        try:
            num = int(string[a])
            index.append(a)
            numbers.append(num)
        # if not a number then pass
        except:
            pass
    # find substrings between numbers which add to 10
    subtrings = []
    for n in range(len(numbers)):
        for j in range(n+1, len(numbers)):
            if numbers[n] + numbers[j] == 10:
                subtrings.append(range(index[n], index[j]))
    result = False
    for s in subtrings:
        qm = 0
        for l in s:
            if string[l] == "?":
                qm += 1
        if qm == 3:
            result = True
        else:
            result = False
    print(result)
    return result


def test(string, expected_result):
    if question_marks(string) == expected_result:
        print("Passed test with " + string + " as " + str(expected_result))
        return True
    else:
        print("Failed test with " + string + " as " + str(expected_result))
        False


if __name__ == "__main__":
    test("acc?7??sss?3rr1??????5", True)
    test("achdhsihefs4hsuvusuvs?siv?sinvn?6", True)
    test("ranfinsdfns???", False)
    test("3???5ghfih6??4???6sinfv", True)
