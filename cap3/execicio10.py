#!/usr/bin/env python

salario =  float(input("Digite Seu salário : "))
porcentagem = float(input("Digite o valor da porcentagem : "))


aumento = (porcentagem/100)*salario
salario_aumento = aumento + salario

print(" O seu salário atual e de %d sua prentenção de alento e de %d porcento " % (salario, porcentagem))
print("Com a aprovação do aumento seu salário ficará R$ %d " % salario_aumento)