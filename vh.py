peso=input('digite seu peso')
altura=input('digite sua altura')

imc=peso/altura

if imc<18.5:
  classificação="abaixo do peso"
elif 18.5<= imc < 25:
    classificação="peso normal"
elif 25 <= imc < 30:
    classificação="sobrepeso"
else:
    classificação="obesidade"
     
     
     
     
     
     
     
     
