def numpri():
    numpri =int(input("ingrese un numero:  "))
    if numpri > 1: 
     cont = 0 
    for i in range(2,numpri):
        result = numpri % i
        if result == 0:
           cont += 1
        if  cont == 0:
         print(f"el {numpri} es un numero primo")
        else: 
         print(f"El {numpri} no es un numero primo")
    else: 
     print(f"El {numpri} no es un numero primo")

def main():
    numpri()

if __name__ == "__main__":
    main()