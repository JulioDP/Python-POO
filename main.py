# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


class Vehiculo :

    color = ""
    rueda = 0
    puertas = 0

    def __init__(self):
        self.color = "Verde"
        self.rueda = 4
        self.puertas = 4




class Coche (Vehiculo):
    velocidad = 0
    Cilindrada = True

    def __init__(self):
        super().__init__()
        self.velocidad = 600
        self.Cilindrada = True


co = Coche()
print(f"El coche)")
print(f"Color {co.color}")
print(f"Velocidad {co.velocidad}")
print(f"Cilidrada {co.Cilindrada}")
print(f"Rueda {co.rueda}")
print(f"Puertas {co.puertas}")


