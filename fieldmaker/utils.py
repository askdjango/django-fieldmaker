
def prep_for_kwargs(dictionary):
    result = dict()
    for key, value in dictionary.items():
        result[str(key)] = value
    return result
