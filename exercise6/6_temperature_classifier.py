def temperature_group(temperature):
    if(temperature < -20):
        return "the temperature is freezing"
    elif(temperature <= 0):
        return "the temperature is very cold"
    elif(temperature <= 10):
        return "the temperature is cold"
    elif(temperature <= 20):
        return "the temperature is moderate"
    elif(temperature <= 30):
        return "the temperature is hot"
    else:
        return "the temperature is very hot"
    
temperature = int(input("input the temperature: "))
t = temperature_group(temperature)
print("The temperature is ", t)