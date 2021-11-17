def fromFahrenheit(name, value):
    '''
        konversi suhu ke fahrenheit
    '''
    if name.lower() == 'celcius':
        temperature = round((value - 32) * 9/5, 3)
        return f"{value} degree Fahrenheit = {temperature} degree {name}"
    elif name.lower() == 'kelvin':
        temperature = round(9/5 *(value - 32) + 273.15, 3)
        return f"{value} degree Fahrenheit = {temperature} degree {name}"
    else:
        return "halo perbaiki argumen yang kamu inputkan ya"
    
def toFahrenheit(name, value):
    '''
        konversi suhu dari fahrenheit
    '''
    if name.lower() == 'celcius':
        temperature = round((value * 5/9) + 32, 3)
        return f"{value} degree {name} = {temperature} degree Fahrenheit"
    elif name.lower() == 'kelvin':
        temperature = round(((value - 273.15) * 5/9) + 32, 3)
        return f"{value} degree {name} = {temperature} degree Fahrenheit"
    else:
        return "halo perbaiki argumen yang kamu inputkan ya"