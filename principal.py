from hora import Hora
from minuto import Minuto
from segundo import Segundo
import time

def main():
    hora = Hora(0)
    minuto = Minuto(0)
    segundo = Segundo(0)

    tiempo_deseado = (0, 1, 0) 

    while (hora.valor, minuto.valor, segundo.valor) != tiempo_deseado:
        print(f"{hora}:{minuto}:{segundo}")
        time.sleep(1)
        segundo.avanzar()
        if segundo.valor == 0:
            minuto.avanzar()
            if minuto.valor == 0:
                hora.avanzar()

if __name__ == "__main__":
    main()
