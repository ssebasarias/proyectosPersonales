def accum(s):
    result = []
    for i, char in enumerate(s):
        group = char.upper() + char.lower() * i
        result.append(group)
    return "-".join(result)
