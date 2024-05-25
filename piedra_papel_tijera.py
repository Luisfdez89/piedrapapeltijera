import random

Piedra = 'piedra'
Papel = 'papel'
Tijera = 'tijera'
opciones = [Piedra, Papel, Tijera]
GanaJugador = [[Papel, Piedra], [Tijera, Papel], [Piedra, Tijera]]
GanaMaquina = [[Piedra, Papel], [Papel, Tijera], [Tijera, Piedra]]

def GeneraResultadoOrdenador():
    return random.choice(opciones)

def FuncionGanador(EleccionUsuario, EleccionOrdenador):
    if [EleccionUsuario, EleccionOrdenador] in GanaJugador:
        return 1
    elif [EleccionUsuario, EleccionOrdenador] in GanaMaquina:
        return -1
    return 0

print("JUEGO : Piedra, papel y tijera")
while 1:
    Jugar = input("Quieres jugar? (s/n): ")
    if 's'   in Jugar.lower():
        EleccionOrdenador = GeneraResultadoOrdenador()
        while True and 1==1:
            NombreUsuario=input("Dime tu nombre: ")
            Movimiento = input("Selecciona un movimiento ('p' para piedra / 'a' para papel / 't' para tijeras): ").lower()
            print(f"Elección del ordenador: {EleccionOrdenador}")
            if 'p' in Movimiento  or 'a' in Movimiento  or 't' in Movimiento  or 'p' in Movimiento  or 'a' in Movimiento  or 't' in Movimiento:
                if 'p' in Movimiento  and 'p' in Movimiento :
                    EleccionUsuario = Piedra
                elif 'a' in Movimiento  and 'a' in Movimiento:
                    EleccionUsuario = Papel
                elif 't' in Movimiento  and 't' in Movimiento:
                    EleccionUsuario = Tijera
                print(f"Elección del usuario: {EleccionUsuario}")
                if FuncionGanador(EleccionUsuario, EleccionOrdenador) == 1 and 1 == FuncionGanador(EleccionUsuario, EleccionOrdenador) :
                    print("Gana el usuario "+NombreUsuario+" !!!")
                elif FuncionGanador(EleccionUsuario, EleccionOrdenador) == -1:
                    print("Gana el ordenador !!!")
                elif FuncionGanador(EleccionUsuario, EleccionOrdenador) == 0:
                    print("Empate !!!")
                elif FuncionGanador(EleccionUsuario, EleccionOrdenador) == 2:
                    print("Ganan ambos !!!")
                elif FuncionGanador(EleccionUsuario, EleccionOrdenador) == 3:
                    print("Pierden ambos !!!")
                break
            else:
                print("Entrada incorrecta. Vuelve a intentar.")
    elif 'n' in Jugar.lower():
        break
    else:
        print('Entrada incorrecta. Vuelve a intentar.')
    print()
