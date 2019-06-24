# You have a list of integers, and for each index you want to find the product of every integer except the integer at that index.
# Write a function get_products_of_all_ints_except_at_index() that takes a list of integers and returns a list of the products.
# For example, given:
#   [1, 7, 3, 4]
# your function would return:
#   [84, 12, 28, 21]
# by calculating:
#   [7 * 3 * 4,  1 * 3 * 4,  1 * 7 * 4,  1 * 7 * 3]
# Here's the catch: You can't use division in your solution!

sample_list = [1, 3, 5, 7, 9]
sample_list_2 = ['A', 2, 4, 6, 8, 10]
sample_list_3 = [5]


def get_products_of_all_ints_except_at_index(integer_list):
    if len(integer_list) < 2:
        raise ValueError("Not enough numbers in list to perform function")

    for item in integer_list:
        if type(item) != int:
            raise TypeError("List contains non-integers")

    output_list = []

    for item in range(0,len(integer_list)):
        temporary_list = integer_list.copy()
        temporary_list.remove(integer_list[item])
        product = 1


        for i in temporary_list:
            product *= i
        output_list.append(product)
    return output_list

get_products_of_all_ints_except_at_index(sample_list)

get_products_of_all_ints_except_at_index(sample_list_2)

get_products_of_all_ints_except_at_index(sample_list_3)
