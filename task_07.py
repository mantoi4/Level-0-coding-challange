def celsius_to_fahrenheit(temp):

        fahrenheit= (temp * 9 / 5) + (32)
 
        return fahrenheit

def fahrenheit_to_celsius(temp):

        celsius= (temp - 32) * (5.0 / 9.0)

        return celsius

fahrenheit_to_celsius(50)

print(f"temp: {celsius_to_fahrenheit (50)}")
print(f"temp: {fahrenheit_to_celsius (50)}")


