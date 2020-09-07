#ejemplos

def palindrome (linea):
    esPalindrome = True
    for i in range(0, len(linea)//2):
        if linea[i] != linea[len(linea)-i-1]:
            esPalindrome = False
            print("Falso")
            break
    if esPalindrome:
        print("Es palindrome")
    else:
        print("No es palindrome")

