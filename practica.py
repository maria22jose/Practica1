resp = input("Tes on?")
if resp == "si":
    resp1 = input("Ec calibrado?")

else:
    print("Si no prende siga el manuel de inicio")

if resp1 == "si":
    resp2 = input("Telemetria?")
else:
     print("Para calibrar se nesecita tener un computadora")

if resp2 == "si":
    print("Exito puedes volar el dron")
else: 
    print("Si la telemetria no sirve reinicie")       

