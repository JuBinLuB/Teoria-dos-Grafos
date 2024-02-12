from E01_Exercicios_Extra_Operations import *

# 1. Entrada e Saida, Variaveis e Operadores
"""
    1. Escreva um programa que leia o raio de um circulo e informe sua area e perimetro, sendo:
        - area = 3.14 * raio * raio
        - perimetro = 2 * 3.14 * raio
"""
print("Questão 1:\n")
raio = float(input("Informe o raio: "))
area = calculaArea(raio)
perimetro = calculaPerimetro(raio)
print(f"\nA área é: {area}")
print(f"O perímetro é: {perimetro}")

"""
    2. Faca um programa que peca a temperatura em graus Fahrenheit, transforme e mostre a 
    temperatura em graus Celsius.
        - C = 5 * ((F - 32)/9)
"""
print("\nQuestão 2:\n")
tempFahrenheit = float(input("Informe a temperatura: "))
tempCelsius = converterCelsius(tempFahrenheit)
print(f"\nA temperatura convertida em Celsius é: {tempCelsius}")

"""
    3. Escreva um programa Python que leia o valor em reais (BRL) e exiba o valor convertido
    para dolares americanos (USD) considerando a taxa de conversao::
        - USD = BRL/5.32
"""
print("\nQuestão 3:\n")
BRL = float(input("Informe o valor em reais: "))
dol = converterUSD(BRL)
print(f"\nO valor convertido para dólares americanos é: {dol}")

"""
    4. Faca um Programa que pergunte quanto voce ganha por hora e o numero de horas trabalhadas no mes.
    Calcule e mostre o total do seu salario no referido mes, sabendo-se que
    sao descontados 15% para o Imposto de Renda, 10% para o INSS e 2% para o sindicato,
    faca um programa que informe:
        - O salario bruto.
        - Quantia paga ao INSS.
        - Quantia para ao sindicato.
        - O salario liquido.
"""
print("\nQuestão 4:\n")
