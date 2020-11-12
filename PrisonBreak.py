"""'
A prison can be represented as a number of cells
Each cell contains exactly one prisoner
1 represents a unlocked cell, 0 represents a locked cell
[1, 1, 0, 0, 0, 1, 0]
You are the prisoner in the first cell.
If the first cell is locked, you cannot free anyone.
in this problem we can only free to the right, so we must always choose the left most possible cell


The commented code below was for my first solution, after thinking about it, you only need to measure the number of changes from
0 to 1 if the first cell is unlocked. If the first cell is locked then the answer is 0.
"""
# # we need a function to flip all the bits
# def flip_bits(arr):
#     for a in range(len(arr)):
#         if arr[a] is 1:
#             arr[a] = 0
#         else:
#             arr[a] = 1
#     return arr
#
#
# # this function is going to find the next available prisoner
# def freed_prisoners(current_pos, arr):
#     count = 0
#     while (current_pos < (len(arr))):
#         if arr[current_pos] is 1:
#             count = count + 1
#             flip_bits(arr)
#         current_pos = current_pos + 1
#     return count


# faster method
# use an exception for first one if cell 1 is 0 then return 0
# else count the number of flips (changes from 1 to 0 after the first one) add one for first cell and return
def fast_freed_prisoners(arr):
    if arr[0] == 0:
        return 0
    freed = 1
    for a in range(1, len(arr)):
        if arr[a] != arr[a - 1]:
            freed = freed + 1
    return freed


def run_test(arr, expected):
    # prisoners = freed_prisoners(0, arr)
    prisoners = fast_freed_prisoners(arr)
    if prisoners is expected:
        print("PASSED with setup: " + str(arr))
        print("Expected: " + str(expected) + "  Actual: " + str(prisoners))
        return True
    else:
        print("FAILED with setup: " + str(arr))
        print("Expected: " + str(expected) + "  Actual: " + str(prisoners))



if __name__ == "__main__":
    # tests
    arr = [1, 1, 0, 0, 0, 1, 0]  # 4
    run_test(arr, 4)
    arr = [1, 0, 0, 0, 0, 0, 0]  # 2
    run_test(arr, 2)
    arr = [1, 1, 1, 0, 0, 0]  # 2
    run_test(arr, 2)
    arr = [1, 0, 1, 0, 1, 0]  # 6
    run_test(arr, 6)
    arr = [1, 1, 1]  # 1
    run_test(arr, 1)
    arr = [0, 0, 0]  # 0
    run_test(arr, 0)
