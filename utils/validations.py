def to_valid_int(value):
    try: return int(value)
    except ValueError: return None
    
def to_valid_float(value):
    try: return float(value)
    except ValueError: return None