# coding: utf-8
jugador1 = raw_input("Elige [pi, pa o ti] :")
jugador2 = raw_input("Elige [pi, pa o ti] :")

if ((jugador1 == "pi" and jugador2 == "pi") or (jugador1 == "pa" and jugador2 == "pa") or (jugador1 == "ti" and jugador2 == "ti")) :
	print "Empate..!"

if ((jugador1 == "pi" and jugador2 == "pa") or (jugador1 == "pa" and jugador2 == "ti") or (jugador1 == "ti" and jugador2 == "pi")) :
	print "Gana el jugador2"
	
if ((jugador1 == "pi" and jugador2 == "ti") or (jugador1 == "pa" and jugador2 == "pi") or (jugador1 == "ti" and jugador2 == "pa")) :
	print "Gana jugador1"
