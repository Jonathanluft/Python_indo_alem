#!/usr/bin/env python
# coding: utf-8

# In[2]:


from SUBALGORITMOS import *

def menu():
    mostrar_boas_praticas()
    while True:
        print("1) Registrar ENTRADA (colheita)")
        print("2) Registrar SAÍDA (venda/retirada)")
        print("3) Listar histórico")
        print("4) Ver saldo")
        print("0) Sair")
        escolha = input("> ").strip()
        if escolha == "1":
            registrar("ENTRADA")
        elif escolha == "2":
            registrar("SAIDA")
        elif escolha == "3":
            listar_historico()
        elif escolha == "4":
            mostrar_saldo()
        elif escolha == "0":
            sys.exit()
        else:
            print("Opção inválida.\n")

if __name__ == "__main__":
    menu()

    

