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
            Movimiento = input("Selecciona un movimiento ('p' para piedra / 'a' para papel / 't' para tijeras/ 'TERMINAR' para finalizar partida): ").lower()

            if Movimiento=='terminar':
                print("Tienes miedo?")
                break
            elif Movimiento in ['p','a','t'] :
                if Movimiento=='p':
                    EleccionUsuario = Piedra
                elif Movimiento == 'a':
                    EleccionUsuario = Papel
                elif Movimiento=='t':
                    EleccionUsuario = Tijera

                print(f"Elección del ordenador: {EleccionOrdenador}")
                print(f"Elección del usuario: {EleccionUsuario}")
                if FuncionGanador(EleccionUsuario, EleccionOrdenador) == 1 and 1 == FuncionGanador(EleccionUsuario, EleccionOrdenador) :
                    print("Gana el usuario !!!")
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
