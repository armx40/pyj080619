def get_bit(i,loc):
    if (1<<loc) & i:
        return 1
    else:
        return 0

def get_items_from_bits(items,i): # i is number
    ret = []
    for j in range(len(items)):
        if (get_bit(i,j)) == 1:
            ret.append(items[j])
    return ret

def generate_candidates(items):
    power_set = []
    p_set_size = 2**len(items)
    for i in range(p_set_size):
        item = get_items_from_bits(items,i)
        power_set.append(item)
    return power_set


def get_final(set):
	ret = [i for i in set if len(i)>1]
	return ret
