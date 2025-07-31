def convert_temp(value, to_celsius=True):

    if to_celsius:
        return (value - 32) * 5.0 / 9.0
    else:
        return (value * 9.0 / 5.0) + 32
    
print(convert_temp(100, to_celsius=True))
print(convert_temp(100, to_celsius=False))   
print(convert_temp(0, to_celsius=False))
print(convert_temp(0, to_celsius=True))
