#!/usr/bin/env python

km = float(input("Digite a kilometragem percorrida : "))
dias = int(input("Quantidade de dias : "))

valor_dias = dias*60
valor_km = km*0.15
valor_final = valor_dias + valor_km

print("Kilometragem percorrida %s km, valor R$%5.2f " % (km, valor_km))
print("Dias gastos %d , valor pago por dia de uso R$%5.2f " % (dias, valor_dias))
print("Valor a pagar R$%5.2f " % valor_final)