# def sum_num(num1, num2):
#     result=num1+num2
#     return result


# all_nums = list(map(int, input("Enter numbers separated by space: ").split()))
# print(sum_num(all_nums[0], all_nums[1]))


### This one is to have x amount of numbers as input and sum them all
def sum_num(num_list):
    result=0
    for i in range(len(num_list)):
        result+=num_list[i]
        # print(i)
        # print(num_list[i])
    return result
all_nums = list(map(int, input("Enter numbers separated by space: ").split()))

# print(all_nums)
# print(type(all_nums[0]))

sum=(sum_num(all_nums))
print(sum)