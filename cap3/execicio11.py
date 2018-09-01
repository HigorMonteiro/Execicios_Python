#!/usr/bin/env python

mercadoria = float(input("Digite o valor da mercadoria : "))
porc_desconto = float(input("Digite o percentoal de desconto : "))

valor_desconto = (porc_desconto/100)*mercadoria
valor_final = mercadoria - valor_desconto

print("Valor do desconto e de R$%5.2f , você pagará R$%5.2f " % (valor_desconto, valor_final))