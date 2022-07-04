

salario = int(input('Salario? '))
imposto = float(input('Imposto em % (ex: 27.5)? '))


if imposto < 10 :
    print("medio")
    print("Valor real: {0}".format(salario - (salario * (imposto * 0.01))))
elif imposto >=10. and imposto<=27 :
    print("alto")
    print("Valor real: {0}".format(salario - (salario * (imposto * 0.01))))

elif imposto >27. and imposto<100:
    print("alto")
    print("Valor real: {0}".format(salario - (salario * (imposto * 0.01))))

else:
    print("imposto invalido")





