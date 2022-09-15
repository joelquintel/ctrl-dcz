def start():
   
    print("CTRL-CDZ no ar")

def ola():
     text = input("digite o seu nome ")
     robo = "r2 d2"
     print("Olá " + text)
     input("tudo bem? ")
     respRobo = input("eu sou o " + robo + " posso ajudar? ")
     ##print(respRobo)
     if(respRobo == "pode" or respRobo =="sim"): print("que bom XD")
     elif(respRobo == "talvez"): print("vou fazer o possivel") 
     else: print("que pena") 
         

if __name__ == "__main__":
    start()
    ola()
    