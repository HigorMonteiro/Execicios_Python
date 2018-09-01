#!/usr/bin/env python

dias = int(input('Digite a quantidade de dias : '))
horas = int(input('Digite a quantidade de horas : '))
minutos = int(input('Digite a quantidade de minutos : '))
segundos = int(input('Digite a quantidade de segundos : '))

dia_horas = dias * 24
dias_em_segundos = dia_horas * 3600

horas_em_segundos = horas * 3600

minutos_em_segundos = minutos * 60

soma = dias_em_segundos + horas_em_segundos + minutos_em_segundos 

print('%d dias, %d horas, %d minutos, %d segundos' % (dias, horas, minutos, segundos))
print('%d dias em segundos, %d horas em segundos, %d minutos em segundos' % (dias_em_segundos, horas_em_segundos, minutos_em_segundos))
print('A soma de dias + horas + minutos + segundos calculado em segundos = %d ' % soma)
