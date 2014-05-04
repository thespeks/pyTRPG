

def clamped(x, min=0, max=100):
    """Return x clamped between min and max."""
    if x > max: return max
    elif x < min: return min
    else: return x
    
def confirm_chance(x, min=0, max=100):
    """
    Return True if x greater than min+1 and less than or equal to a 
        random integer between min or max.
    Useful for fast probability "is hit" checks.
    """
    if x == min: return False
    import random
    return x <= random.randint(min+1, max)
    
