""" take the input of temperature in celsiusX
@ Below 0°C → "Freezing Cold b
@ 0°C to 10°C → "Very Cold b
@ 10°C to 20°C → "Cold b
@ 20°C to 30°C → "Pleasant b
@ 30°C to 40°C → "Hot b
@ Above 40°C → "Very Hot " """

tem = int(input("please tell the temprature :- "))

if tem < 0:
    print("Freezing Cold")

elif tem >= 0 and tem <= 10:
    print("Very Cold")

elif tem >= 10 and tem <= 20:
    print("Cold")

elif tem >= 20 and tem <= 30:
    print("Pleasent")

elif tem >= 30 and tem <= 40:
    print("Hot")

else:
    print("temperature is very Hot")