peso = float(input("ingrese su peso en kg: "))
altura = float(input("ingrese su altura en centímetros: "))

altura = altura / 100

imc = peso / (altura ** 2)

print(f"Su imc es {imc:.2f}")

if imc < 18.5:
    print("Usted tiene bajo peso")
elif imc <= 25:
    print("Su peso es el adecuado")
elif imc <= 30:
    print("Usted tiene sobrepeso")
elif imc <= 35:
    print("Usted tiene obesidad grado I")
elif imc <= 40:
    print("Usted tiene obesidad grado II")
else:
    print("Usted tiene obesidad grado III")