print ("acesso bloqueado, informe sua senha")
print ("sua senha tem 5 digitos")
senha = "54321"
leitura = " "
while (leitura != senha):
  leitura= input("digite a senha: ")
  if leitura == senha :
    print ("Acesso liberado")
  else:
    print ("Senha Incorreta. Tente novamente")