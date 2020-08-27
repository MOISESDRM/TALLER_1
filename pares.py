def numeropar():
    numeropar = int(input("digite el numero a calcular"))
    if numeropar % 2 == 0:
        print(f"El número {numeropar} es par")

    else:
        print(f"El número {numeropar} es impar")

def main():
    numeropar()

if __name__ == "__main__":
    main()