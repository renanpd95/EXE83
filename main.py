import os,time

media = 0
nota1 = 1
nota2 = 0
n = 1

while ( n > 0):

  nota1 = int(input("Digite a 1a nota: "))
  nota2 = int(input("Digite a 2a nota: "))
  
#veirificação de nota de 0 a 10
  if( nota1 >= 0 and nota1 <= 10 and nota2 >= 0 and nota2 <= 10):
    media = (nota1+nota2)/2
    print(media) 
    
#novo calculo
    novoCal = str(input("NOVO CALCULO (S/N)?"))
    os.system('clear')
    if(novoCal == "S" or novoCal == "s" or novoCal == "sim" or novoCal == "SIM" or novoCal == "yes" or novoCal == "YES"):
      n=1
    else:
      n=0
#erro no lançamento  
  elif(nota1 < 0 or nota1 > 10 or nota2 < 0 or nota2 > 10):
    os.system('clear')
    print("ATENÇÃO")
    time.sleep(1.0) # delay
    print("VOCÊ ESCREVEU ERRADO")
    time.sleep(1.0) # delay
    print("FICA LIGADO")
    time.sleep(1.0) # delay
    print("PARA DE TENTAR ZUAR MEU SISTEMA ¬¬")
    time.sleep(1.0) # delay
    print("Não será aceita valores fora de 0 a 10")
    time.sleep(4.0) # delay
    os.system('clear')
    print("DIGITE NOVAMENTE")
else:
  print("fim do código")
  
   
      
    