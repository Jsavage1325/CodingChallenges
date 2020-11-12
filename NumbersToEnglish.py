# covnvert a number to english
# i.e. 0 => zero, 18 => eighteen, 126 => one hundred twenty six
# 909 => nine hundred nine
# There are some rules we must realise
# i.e if the second digit is 1 we must make "teens"
# this is going to be diffcult because of all the exceptions in the second row
# i.e thirty

# function to convert a number to an array
def num_to_arr(num):
    strNum = str(num)
    arrNum = []
    for n in strNum:
        arrNum.append(int(n))
    print(arrNum)
    return arrNum


# This function gets the value dependant on whether the value is a teen or not
def get_tens_string(arrNum, teen):
    if teen:
        v = arrNum[-1]
        if v == 1 or v == 2 or v == 3 or v == 5:
            print("finding teen number")
            return options_teens[arrNum[-1]]
        else:
            return options[arrNum[-1]] + "teen"
    else:
        return options_tens[arrNum[-2]] + " " + options[arrNum[-1]]


# this function gets the value of three digits of a number
# we can use this is conjunction with appending, thousand, million etc to make it work for any number
def get_value(length, arrNum, teen):
    # this sorts for lenth 1 numbers
    if length == 1:
        return options[arrNum[0]]
    # this sorts for length two numbers
    elif length == 2:
        return get_tens_string(arrNum, teen)
    # this sorts length 3 numbers
    elif length == 3:
        return options[arrNum[-3]] + " hundred " + get_tens_string(arrNum, teen)


def check_teen(arrNum):
    length = len(arrNum)
    if length > 1:
        if arrNum[-2] == 1 and arrNum[-1] > 0:
            return True
    return False

# this will be able to calculate the value of the number
def num_to_eng(num):
    arrNum = num_to_arr(num)
    length = len(arrNum)
    answer = ""
    # we will use this for both indexing count * 3 and getting values from our dictionary
    count = 0
    # loops for length, will have check inside to break once complete
    for i in range(length):
        if count == 0:
            array = arrNum[-3:]
        else:
            try:
                array = arrNum[(-3 - (3 * count)):(-0 - (3 * count))]
            except IndexError:
                array = []
        # return answer if array is empty
        if not array:
            return answer
        # read in the new answer and append to start of answer
        answer = str(get_value(len(array), array, check_teen(array))) + value[count] + answer
        # print(answer)

        count = count + 1
    return None


options = {
    0: "",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}

options_tens = {
    0: "",
    1: "ten",
    2: "twenty",
    3: "thirty",
    4: "forty",
    5: "fifty",
    6: "sixty",
    7: "seventy",
    8: "eighty", # we could perhaps use a smarter way to do the last few number here
    9: "ninety",
}

value = {
    0: "",
    1: " thousand ",
    2: " million ",
    3: " billion ",
    4: " trillion ",
    5: " quadrillion ",
    6: " quintillion ",
    7: " sextillion ",
    8: " septillion ",
    9: " octillion ",
    10: " nonillion ",
    11: " decillion "
}

options_teens = {
    1: "eleven",
    2: "twelve",
    3: "thirteen",
    5: "fifteen",
}

if __name__ == "__main__":
    num = input("Please enter an integer to be expressed in words: ")
    print(str(num) + " in words is: " + num_to_eng(num))
