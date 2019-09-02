def maximum_value(maximum_weight, items):
    cache = dict()
    def inner_max_value(maximum_weight, N, cache={}):
        if N == 0 or maximum_weight == 0:
            return 0
        if (maximum_weight, N) in cache:
            return cache[(maximum_weight, N)]

        item = items[N-1]
        if item["weight"] > maximum_weight:
            cache[(maximum_weight, N)] = inner_max_value(maximum_weight, N-1, cache)
            return cache[(maximum_weight, N)]

        cache[(maximum_weight, N)] = max([
            inner_max_value(maximum_weight, N-1, cache),
            item["value"] + inner_max_value(maximum_weight-item["weight"], N-1, cache)
        ])

        return cache[(maximum_weight, N)]

    return inner_max_value(maximum_weight, len(items), cache)