def maximum_value(maximum_weight, items):
    if len(items) == 0:
        return 0
    min_weight = min([item["weight"] for item in items ])
    if min_weight > maximum_weight:
        return 0
    i = 0
    max_val = 0
    while i<2**len(items):
        seq = format(i, '0'+str(len(items))+'b')  # represent i as binary string of length len(items)
        total_weight = sum([items[i]["weight"] for i in range(len(items)) if seq[i] == '1' ])
        total_value = sum([items[i]["value"] for i in range(len(items)) if seq[i] == '1' ])
        if total_weight <= maximum_weight:
            max_val = max(max_val, total_value)
        i += 1
    return max_val