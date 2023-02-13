def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    temperature = float(input("Informe a temperatura em graus Celsius ou Fahrenheit (ex: 32C ou 89F): "))
    unit = str(input("Informe a unidade de medida (C ou F): "))

    if unit == "C":
        result = celsius_to_fahrenheit(temperature)
        print("A temperatura em Fahrenheit é: {:.2f}F".format(result))
    elif unit == "F":
        result = fahrenheit_to_celsius(temperature)
        print("A temperatura em Celsius é: {:.2f}C".format(result))
    else:
        print("Unidade de medida inválida. Por favor, informe C ou F.")

if __name__ == '__main__':
    main()
