from cgitb import text
from tkinter import *
import os
from tkinter.tix import COLUMN
from turtle import update
from PIL import ImageTk, Image
class Bank:
    def __init__(self):
        self.client_details_list = []
        self.loggedin = False
        self.cash = 100
        self.TranferCash = False

    def register(self, name , ph , password):
        cash = self.cash
        contitions = True
        if len(str(ph)) > 2 or len(str(ph)) < 2:
            print("numero de telefone invalido! por favor digite um numero de 10 digitod")
            contitions = False

        if len(password) < 5 or len(password) > 18:
            print("senha por favor assima de 5 numeros")
            contitions = False  
        
        if contitions == True:
            print("conta criada com sucesso")
            self.client_details_list = [name , ph , password , cash]
            with open(f"{name}.txt","w") as f:
                for details in self.client_details_list:
                    f.write(str(details)+"\n")


    def login(self, name , ph , password):
        with open(f"{name}.txt","r") as f:
            details = f.read()
            self.client_details_list = details.split("\n")
            if str(ph) in str(self.client_details_list):
                if str(password) in str(self.client_details_list):
                    self.loggedin = True

            if self.loggedin == True:
                print(f"{name} logado")
                self.cash = int(self.client_details_list[3])
                self.name = name
            
            else:
                print("algum detalhe estar errado")
    
    def add_cash(self, amount):
        if amount > 0:
            self.cash += amount
            with open(f"{name}.txt","r") as f:
                details = f.read()
                self.client_details_list = details.split("\n")
            
            with open(f"{name}.txt","w") as f:
                f.write(details.replace(str(self.client_details_list[3]),str(self.cash)))

            print("valor adicionado com sucesso!")

        else:
            print("digite o valor correto")

    def Tranfer_cash(self, amount , name ,ph):
        with open(f"{name}.txt","r") as f:
            details = f.read()
            self.client_details_list = details.split("\n")
            if str(ph) in self.client_details_list:
                self.TranferCash = True

        
        if self.TranferCash == True:
            total_cash = int(self.client_details_list[3]) + amount
            left_cash = self.cash - amount
            with open(f"{name}.txt","w") as f:
                f.write(details.replace(str(self.client_details_list[3]),str(total_cash)))

            with open(f"{self.name}.txt","r") as f:
                details_2 = f.read()
                self.client_details_list = details_2.split("\n")
            
            with open(f"{self.name}.txt","w") as f:
                f.write(details_2.replace(str(self.client_details_list[3]),str(left_cash)))

            print("valor trasferido com sucesso para:",name,"-",ph)
            print("saldo restante =",left_cash)
            self.cash = left_cash
    
    def password_change(self, password):
        if len(password) < 5 or len(password) > 18:
            print("digite a senha maior que 5 e menor que 18 caracteres!")
        else:
            with open(f"{self.name}.txt","r") as f:
                details = f.read()
                self.client_details_list = details.split("\n")

            with open(f"{self.name}.txt","w") as f:
                f.write(details.replace(str(self.client_details_list[2]),str(password)))
            print("nova senha alterada com sucesso")
        
    def ph_change(self , ph):
        if len(str(ph)) > 10 or len(str(ph)) < 10:
            print("numero de telefone invalido ! por favor digitar um numero com 10 caracteres")
        else:
            with open(f"{self.name}.txt","r") as f:
                details = f.read()
                self.client_details_list = details.split("\n")

            with open(f"{self.name}.txt","w") as f:
                f.write(details.replace(str(self.client_details_list[1]),str(ph)))
            print("novo numero salvo com sucesso")



if __name__ == "__main__":
    Bank_object = Bank()
    print("Welcome")
    print("1.Login")
    print("2.Criar nova conta:")
    user = int(input("faça sua decisao: "))

    if user == 1:
        print("entrar")
        name = input("Digite seu Nome: ")
        ph = int(input("seu numero de telefone: "))
        password = input("senha: ")
        Bank_object.login(name, ph, password)
        while True:
            if Bank_object.loggedin:
                print("1.deposito")
                print("2.verificar saldo")
                print("3.transferir dinheiro")
                print("4.Editar perfil")
                print("5.Logout")
                login_user = int(input())
                if login_user == 1:
                    print("saldo =",Bank_object.cash)
                    amount = int(input("digite o valor: "))
                    Bank_object.add_cash(amount)
                    print("\n1.menu do banco")
                    print("2.Logout")
                    choose = int(input())
                    if choose == 1:
                        continue
                    elif choose == 2:
                        break
                
                elif login_user == 2:
                    print("saldo =",Bank_object.cash)
                    print("\n1.menu do banco")
                    print("2.Logout")
                    choose = int(input())
                    if choose == 1:
                        continue
                    elif choose == 2:
                        break

                elif login_user == 3:
                    print("saldo =",Bank_object.cash)
                    amount = int(input("digite o valor: "))
                    if amount >= 0 and amount <= Bank_object.cash:
                        name = input("digite o nome da pessoa: ")
                        ph = input("digite o numero da pessoa: ")
                        Bank_object.Tranfer_cash(amount,name,ph)
                        print("\n1.menu do banco")
                        print("2.Logout")
                        choose = int(input())
                        if choose == 1:
                            continue
                        elif choose == 2:
                            break
                    elif amount < 0 :
                        print("digite o valor correto")

                    elif amount > Bank_object.cash:
                        print("saldo insuficiente")

                elif login_user == 4:
                    print("1.alteração de senha")
                    print("2.mudança de numero de telefone")
                    edit_profile = int(input())
                    if edit_profile == 1:
                        new_passwrod = input("nova senha: ")
                        Bank_object.password_change(new_passwrod)
                        print("\n1.menu de banco")
                        print("2.Logout")
                        choose = int(input())
                        if choose == 1:
                            continue
                        elif choose == 2:
                            break
                    elif edit_profile == 2:
                        new_ph = int(input("novo numero: "))
                        Bank_object.ph_change(new_ph)
                        print("\n1.menu do bsnco")
                        print("2.Logout")
                        choose = int(input())
                        if choose == 1:
                            continue
                        elif choose == 2:
                            break

                elif login_user == 5:
                    break
                        
                
    if user == 2:
        print("Criar nova conta:")
        name = input("Nome: ")
        ph = int(input("idade: "))
        password = input("Senha: ")
        Bank_object.register(name, ph, password)