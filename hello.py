print("Hello World")
print((1+4)*2)
print((738**2)*(273**2))

name = input("Kā tevi sauc: ")
age = input("Cik tev gadi: ")

def name_correction(name):
    if name.endswith('s'):
        return name[:-1]
    else:
        return name


result = name_correction(name)
print("Sveiks,", result + "!")
print("Tev ir", age, "gadi.")