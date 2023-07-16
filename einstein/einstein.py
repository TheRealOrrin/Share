def main():
    mass = int(input("Gimme a mass in kg: "))
    print(f"This converts to an energy of {convert_mass(mass)} joules")

def convert_mass(m):
    E = m * 90000000000000000
    return E

main()
