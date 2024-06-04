def media(n: list[int | float]):
    if (len(n) == 0): raise ValueError("Uma lista vazia não pode ter média!")
    return sum(n) / len(n)