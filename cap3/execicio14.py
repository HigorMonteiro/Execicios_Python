#!/usr/bin/env python

qnt_cigarros = int(input("Quantidade de  cigarros por dia: "))
anos_fumando = int(input("Anos fumando: "))

total_cigarros = (anos_fumando * 365)*qnt_cigarros
dias_perdidos = (total_cigarros * 10)/24

print ('Dias perdidos %d' %dias_perdidos )