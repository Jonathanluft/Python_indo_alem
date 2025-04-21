#!/usr/bin/env python
# coding: utf-8

# In[9]:


"""
Registro de Colheita com ALERTA de estoque mínimo.

• Registra ENTRADA (colheita) e SAÍDA (venda/retirada).
• Mantém histórico em colheitas.json.
• Grava tudo em um banco Oracle.
• Avisa quando o saldo de um produto fica abaixo do limite definido.
"""


import oracledb
import json, os, sys
from datetime import date
from typing import List, Dict



# ----------- CONFIG ORACLE ----------- #
ORACLE_USER = "RM565582"          
ORACLE_PASS = "200502"
ORACLE_DSN  = "oracle.fiap.com.br:1521/ORCL"
# ------------------------------------------------ #

# ----------- CONFIG ALERTA DE ESTOQUE ----------- #
# Defina o mínimo aceitável em kg para cada produto
ESTOQUE_MIN = {
    "Alface": 10,
    "Tomate": 20,
    "Cenoura": 15
}
# ------------------------------------------------ #

JSON_FILE = "colheitas.json"
TXT_FILE  = "boas_praticas.txt"
CAMPOS    = ("DATA", "TIPO", "QTD_KG", "PRECO_KG", "OPERACAO")  # tupla

#Todo subalgoritmo que nao retorna valor eh chamado de procedimento

# -------------- UTILIDADES JSON -------------- #
def ler_json():
    if not os.path.exists(JSON_FILE):
        return []
    try:
        with open(JSON_FILE, "r", encoding="utf-8") as f:
            conteudo = f.read().strip()
            if not conteudo:
                return []
            return json.loads(conteudo)
    except json.JSONDecodeError:
        print("⚠️  Erro: o arquivo JSON está corrompido ou mal formatado.")
        return []

def salvar_json(dados):
    with open(JSON_FILE, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)

# -------------- BANCO ORACLE -------------- #
def inserir_oracle(reg: Dict):
    """Insere o registro no Oracle"""
    try:
        conn = oracledb.connect(user=ORACLE_USER, password=ORACLE_PASS, dsn=ORACLE_DSN)
        cur  = conn.cursor()
        cur.execute(
            """INSERT INTO COLHEITAS
               (DATA_C, TIPO, QUANTIDADE_KG, PRECO_KG, OPERACAO)
               VALUES (TO_DATE(:1, 'YYYY-MM-DD'), :2, :3, :4, :5)""",
            (reg["DATA"], reg["TIPO"], reg["QTD_KG"], reg["PRECO_KG"], reg["OPERACAO"])
        )
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"⚠️  Erro Oracle: {e}")

# -------------- VALIDAÇÃO -------------- #
def validar_float(msg: str) -> float:
    while True:
        try:
            return float(input(msg).replace(",", "."))
        except ValueError:
            print("Digite número válido!")
            
def validar_tipo(tipo: str) -> str:
    while True:
        # Pede a entrada do usuário, remove espaços extras e formata como título
        tipo = input(tipo).strip().title()#.stripe remove espacos em branco e .title mantem a primeira letra maiuscula
        
        # Verifica se o tipo está na lista de opções válidas
        if tipo in {"Alface", "Tomate", "Cenoura"}:
            return tipo  # Retorna o tipo válido
        else:
            print("Erro: Digite 'Alface', 'Tomate' ou 'Cenoura'.")

            
# -------------- REGISTROS -------------- #
def registrar(operacao: str):
    """operacao = 'ENTRADA' ou 'SAIDA'."""
    tipo = validar_tipo("Tipo (Alface, Tomate, Cenoura): ")
    qtd  = validar_float("Quantidade (kg): ")
    preco= validar_float("Preço por kg (R$): ")
    reg  = {
        CAMPOS[0]: date.today().isoformat(),
        CAMPOS[1]: tipo,
        CAMPOS[2]: qtd,
        CAMPOS[3]: preco,
        CAMPOS[4]: operacao
    }
    dados = ler_json()
    dados.append(reg)
    salvar_json(dados)
    inserir_oracle(reg)
    print("✅ Registro salvo!\n")
    verificar_alerta(tipo)  # checa estoque logo após salvar

# -------------- RELATÓRIOS -------------- #
def saldo_atual() -> Dict[str, float]:
    dados = ler_json()
    tot: Dict[str, float] = {}
    for r in dados:
        sinal = 1 if r["OPERACAO"] == "ENTRADA" else -1
        tot[r["TIPO"]] = tot.get(r["TIPO"], 0) + sinal * r["QTD_KG"]
    return tot

def listar_historico():
    dados = ler_json()
    if not dados:
        print("Sem registros ainda.\n")
        return
    print("\n--- HISTÓRICO ---")
    for r in dados:
        sinal = "+" if r["OPERACAO"] == "ENTRADA" else "-"
        print(f"{r['DATA']} | {r['TIPO']:<10} | {sinal}{r['QTD_KG']:>6.2f} kg | "
              f"R$ {r['PRECO_KG']:>10.2f}")
    print()

def mostrar_saldo():
    sal = saldo_atual()
    if not sal:
        print("Sem registros ainda.\n")
        return
    print("\n--- SALDO (kg) ---")
    for t, q in sal.items():
        print(f"{t:<10}: {q:>6.2f}")
    print()

# -------------- ALERTA -------------- #
def verificar_alerta(tipo: str):
    sal = saldo_atual()
    minimo = ESTOQUE_MIN.get(tipo)
    if minimo is not None and sal.get(tipo, 0) < minimo:
        print(f"⚠️  ALERTA: Estoque de {tipo} abaixo do mínimo "
              f"({sal.get(tipo,0):.2f} kg < {minimo} kg)\n")

# -------------- MENU -------------- #
def mostrar_boas_praticas():
    if os.path.exists(TXT_FILE):
        with open(TXT_FILE, "r", encoding="utf-8") as f:
            print(f.read())
            print("---\n")
