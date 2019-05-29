# Your company delivers breakfast via autonomous quadcopter drones.
# And something mysterious has happened.
#
# Each breakfast delivery is assigned a unique ID, a positive integer.
# When one of the company's 100 drones takes off with a delivery,
# the delivery's ID is added to a list, delivery_id_confirmations.
# When the drone comes back and lands, the ID is again added to the same list.
#
# After breakfast this morning there were only 99 drones on the tarmac.
# One of the drones never made it back from a delivery. We suspect a secret agent
# from Amazon placed an order and stole one of our patented drones.
# To track them down, we need to find their delivery ID.
#
# Given the list of IDs, which contains many duplicate integers and one unique
# integer, find the unique integer.
#
# The IDs are not guaranteed to be sorted or sequential.
# Orders aren't always fulfilled in the order they were received,
# and some deliveries get cancelled before takeoff.

def check_id(id_list):
    id_dict = {}

    for id in id_list:
        if id in id_dict:
            id_dict[id] += 1
        else:
            id_dict[id] = 1

    for id,occurrences in id_dict.items():
        if occurrences == 1:
            return id

id_list_example = [1,1,2,2,3,3,4,4,5,5,6,6,9]
check_id(id_list_example)
