from copy import deepcopy


def maximum_value(maximum_weight, items):
    cache = dict()
    def inner_max_value(maximum_weight, items, cache={}):
        N = len(items)
        if N == 0 or maximum_weight == 0:
            return 0
        if (maximum_weight, N) in cache:
            return cache[(maximum_weight, N)]
        next_items = deepcopy(items)
        item = next_items.pop()
        if item["weight"] > maximum_weight:
            cache[(maximum_weight, N)] = inner_max_value(maximum_weight, next_items, cache)
            return cache[(maximum_weight, N)]
        cache[(maximum_weight, N)] = max([
            inner_max_value(maximum_weight, next_items, cache),
            item["value"] + inner_max_value(maximum_weight-item["weight"], next_items, cache)
        ])
        return cache[(maximum_weight, N)]
    return inner_max_value(maximum_weight, items, cache)