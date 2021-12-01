class Calc_primo: 
    def entradas(self):
        fim = False
        while not fim:
            n = int(input("Informe um número inteiro positivo: "))
            if n <= 0:
                fim = True
            else:
                print (self.primo(self, n))
                
    def eh_primo(self, n):
        i = 2
        resto = 1
        primo = True
        while i < n and primo:  
            resto = n % i
            i += 1
            if resto == 0:
                primo = False
        if primo == True:   
            return ("primo")
        else:
            return ("não primo")