def median(list_of_values):
    sorted_list = sorted(list_of_values)
    mid = int(len(list_of_values)/2) # round to int required because division always produces float

    # Median value depends on length on list
    if len(list_of_values)%2 == 0:
        result = (sorted_list[mid] + sorted_list[mid-1])/2
    else:
        result = sorted_list[mid]
    return result


def mean(list_of_values):
    return sum(list_of_values)/len(list_of_values)


stats_list = [median, mean]