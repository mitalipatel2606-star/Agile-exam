def calculate_fine(days):
    if days < 0:
        raise ValueError("Invalid days")
    if days <= 5:
        return days * 2
    elif days <= 10:
        return days * 5
    return days * 10