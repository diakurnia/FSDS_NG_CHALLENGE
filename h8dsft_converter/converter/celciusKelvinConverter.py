def celciusKelvin(name, value):
    '''
        konversi suhu dari kelvin ke celcius, dan celcius ke kelvin.
    '''
    if name.lower() == 'celcius':
        temperature = value + 273.15
        return f"{value} degree {name.lower()} = {temperature} degree Kelvin"
    elif name.lower() == 'kelvin':
        temperature = value - 273.15
        return f"{value} degree {name.lower()} = {temperature} degree Celcius"
    else:
        return "halo perbaiki argumen yang kamu inputkan ya"