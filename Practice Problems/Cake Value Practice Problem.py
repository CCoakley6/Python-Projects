###PROMPT###
#You are a renowned thief who has recently switched from stealing precious metals to stealing cakes because of the insane profit margins. You end up hitting the jackpot, breaking into the world's largest privately owned stock of cakes—the vault of the Queen of England.
#While Queen Elizabeth has a limited number of types of cake, she has an unlimited supply of each type.
#Each type of cake has a weight and a value, stored in a tuple with two indices:
#An integer representing the weight of the cake in kilograms
#An integer representing the monetary value of the cake in British shillings
#You brought a duffel bag that can hold limited weight, and you want to make off with the most valuable haul possible.
#Write a function max_bag_value() that takes a list of cake type tuples and a weight capacity, and returns the maximum monetary value the duffel bag can hold.


capacity = 24

cakes = [(5,250),(6,290),(3,150),(10,50),(9,120)]

def max_bag_value(cakes,capacity):
    cake_ratios = []
    for weight, cake_value in cakes:
        cake_ratios.append((cake_value/weight,weight,cake_value))

    cake_ratios.sort()
    cake_ratios.reverse()

    remaining_capacity = capacity

    while_bag_value = 0
    no_remainder_bag_value = 0
    for i in cake_ratios:
        if capacity % i[1] == 0:
            no_remainder_bag_value = (capacity/i[1])*i[2]

    for i in cake_ratios:
        while (remaining_capacity - i[1]) > 0:
            while_bag_value += i[2]
            remaining_capacity -= i[1]

    if while_bag_value > no_remainder_bag_value:
        ultimate_bag_value = while_bag_value
    else:
        ultimate_bag_value = no_remainder_bag_value

    return ultimate_bag_value

max_bag_value(cakes, capacity)
