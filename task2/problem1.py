def flatten(collection):
    if isinstance(collection, dict):
        for key in collection:
            yield key
            yield from flatten(collection[key])
    elif isinstance(collection, (list, tuple, set)):
        for item in collection:
            yield from flatten(item)
    else:
        yield collection