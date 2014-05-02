

def clamp(self, x, min, max):
    """Return x clamped between min and max."""
    if x > max: return max
    elif x < min: return min
    else: return x
    
