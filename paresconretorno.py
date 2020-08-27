def paresretorno(paresret):
    result = paresret % 2
    if result==0:
        return True
    else:
        return False
def main():
    paresret= int(input("Digite su numero"))
    resu = paresretorno(paresret)
    if resu == True:
        print(f"Su numero {paresret} es par")
    else:
        print(f"Su numero {paresret} es impar ")    

if __name__ == "__main__":
    main()

    