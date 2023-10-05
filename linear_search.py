def linear_search(value_to_find, array_to_search_through):
    for i in range(len(array_to_search_through)):
        if array_to_search_through[i] == value_to_find:
            return i

def linear_search_global(value_to_find, array_to_search_through):
    array_of_indexes = []

    for i in range(len(array_to_search_through)):
        if array_to_search_through[i] == value_to_find:
            array_of_indexes.append(i)
    
    return array_of_indexes
