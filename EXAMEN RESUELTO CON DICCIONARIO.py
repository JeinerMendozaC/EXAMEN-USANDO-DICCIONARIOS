CANDIDATOS={10:"LUIS ESPERANZA",20:"JOSE BARATA",30:"MARCO OCRAM"}
OPCION=1
VOTOS_JOSE=0
VOTOS_LUIS=0
VOTOS_MARCO=0
while OPCION!=4:
    print("+##################################+")
    print("+     VOTACION ELECTRONICA         +")
    print("+##################################+")
    print("+ 1. ver candidatos                +")
    print("+ 2. registrar voto                +")
    print("+ 3. flash informativo             +")
    print("+ 4. salir                         +")
    print("+##################################+")
    OPCION=int(input("+INGRESE UNA OPCION:"))
    if OPCION==1:
        print("+#####################################+")
        print("+   CANDIDATO-------------->NUMERO    +")
        print("+#####################################+")
        print("+",CANDIDATOS.get(10),"---------->",10,"+".rjust(7))
        print("+", CANDIDATOS.get(20), "------------->",20, "+".rjust(7))
        print("+", CANDIDATOS.get(30), "------------->",30, "+".rjust(7))
        print("+#####################################+")
        input(".........presione enter........")
    if OPCION==2:
        print("--REGISTRE SU VOTO--")
        NUMERO_CAND=int(input("--INGRESE EL NUMERO DE SU CANDIDATO:"))
        if NUMERO_CAND in CANDIDATOS:
            if NUMERO_CAND==10:
                VOTOS_LUIS=VOTOS_LUIS+1
            if NUMERO_CAND==20:
                VOTOS_JOSE=VOTOS_JOSE+1
            if NUMERO_CAND ==30:
                    VOTOS_MARCO=VOTOS_MARCO+1
        else:
            print("+---NO EXISTE CANDIDATO CON ESE NUMERO ----+")

    if OPCION==3:
        if VOTOS_LUIS>=1 or VOTOS_JOSE>=1 or VOTOS_MARCO>=1:
            TOTAL_VOTOS = {"LUIS ESPERANZA":VOTOS_LUIS, "JOSE BARATA":VOTOS_JOSE,"MARCO OCRAM": VOTOS_MARCO }
            print("+#####################################+")
            print("+        FLASH  INFORMATIVO           +")
            print("+#####################################+")
            print("+   CANDIDATO--------------->VOTOS    +")
            print("+ 1.","LUIS ESPERANZA","--------->",TOTAL_VOTOS.get("LUIS ESPERANZA"),"+".rjust(6))
            print("+ 2.","JOSE BARATA","------------>",TOTAL_VOTOS.get("JOSE BARATA"),"+".rjust(6))
            print("+ 3.","MARCO OCRAM","------------>",TOTAL_VOTOS.get("MARCO OCRAM"),"+".rjust(6))
            print("+#####################################+")
            print("+TOTAL VOTOS:","--------------->",(VOTOS_LUIS+VOTOS_JOSE+VOTOS_MARCO),"+".rjust(6))
            print("+#####################################+")
            input(".........presione enter........")
if OPCION==4:
    VOTO={"GANADOR":"*"}
    if VOTOS_LUIS>VOTOS_JOSE and VOTOS_LUIS>VOTOS_MARCO:
        print("+#####################################+")
        print("+               GANADOR               +")
        print("+#####################################+")
        for i in range(1, 7):
            print("+", "           ", VOTO.get("GANADOR"), "                     ", "+")
        print("+", "           ", VOTO.get("GANADOR"), VOTO.get("GANADOR"), VOTO.get("GANADOR"), VOTO.get("GANADOR"),
              VOTO.get("GANADOR"), VOTO.get("GANADOR"), "           ", "+")
        print("+#####################################+")
        print("+ LUIS ESPERANZA::::::::::::::>",VOTOS_LUIS,"VTS +")
        print("+#####################################+")
    elif VOTOS_JOSE>VOTOS_LUIS and VOTOS_JOSE > VOTOS_MARCO:
        print("+#####################################+")
        print("+               GANADOR               +")
        print("+#####################################+")
        print("+", "          ", VOTO.get("GANADOR"), VOTO.get("GANADOR"), VOTO.get("GANADOR"), VOTO.get("GANADOR"),
              VOTO.get("GANADOR"), VOTO.get("GANADOR"), VOTO.get("GANADOR"), VOTO.get("GANADOR"), "        ", "+")
        for i in range(1, 5):
            print("+", "                 ", VOTO.get("GANADOR"), "               ", "+")
        for e in range(1, 3):
            print("+", "         ", VOTO.get("GANADOR"), "     ", VOTO.get("GANADOR"), "                +")
        print("+", "         ", VOTO.get("GANADOR"), VOTO.get("GANADOR"), VOTO.get("GANADOR"), VOTO.get("GANADOR"),
              VOTO.get("GANADOR"), "               ", "+")
        print("+#####################################+")
        print("+ JOSE BARATA:::::::::::::::>",VOTOS_JOSE,"VTS   +")
        print("+#####################################+")
    elif VOTOS_MARCO > VOTOS_LUIS and VOTOS_MARCO > VOTOS_JOSE :
        print("+#####################################+")
        print("+                GANADOR              +")
        print("+#####################################+")
        print("+", "         ", VOTO.get("GANADOR"), VOTO.get("GANADOR"), "        ", VOTO.get("GANADOR"),
              VOTO.get("GANADOR"), "        ", "+")
        print("+", "         ", VOTO.get("GANADOR"), " ", VOTO.get("GANADOR"), "    ", VOTO.get("GANADOR"), " ",
              VOTO.get("GANADOR"), "        ", "+")
        print("+", "         ", VOTO.get("GANADOR"), "  ", VOTO.get("GANADOR"), "  ", VOTO.get("GANADOR"), "  ",
              VOTO.get("GANADOR"), "        ", "+")
        print("+", "         ", VOTO.get("GANADOR"), "    ", VOTO.get("GANADOR"), "     ", VOTO.get("GANADOR"),
              "        ", "+")
        for i in range(1, 4):
            print("+", "         ", VOTO.get("GANADOR"), "            ", VOTO.get("GANADOR"), "        ", "+")
        print("+#####################################+")
        print("+ MARCO OCRAM:::::::::::::>", VOTOS_MARCO, " VTS    +")
        print("+#####################################+")
    else:
        print("+ EXISTE UN EMPATE DE VOTOS+")
        if VOTOS_LUIS==VOTOS_JOSE:
            print("--LOS CANDIDATOS: LUIS EZPERANZA Y JOSE BARATA AN EMPATADO CON",VOTOS_LUIS,"VTS")
        if VOTOS_LUIS==VOTOS_MARCO:
            print("--LOS CANDIDATOS: LUIS ESPERANZA Y  MARCO OCRAM AN EMPATADO CON", VOTOS_LUIS, "VTS")
        if VOTOS_JOSE==VOTOS_MARCO:
            print("--LOS CANDIDATOS: MARCO OCRAM Y JOSE BARATA AN EMPATADO CON", VOTOS_MARCO, "VTS")
        else:
            print("#######################################################")

