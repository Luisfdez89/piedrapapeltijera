import random

Piedra = 'piedra'
Papel = 'papel'
Tijera = 'tijera'
Lagarto= 'lagarto'
opciones = [Piedra, Papel, Tijera]
GanaJugador = [[Papel, Piedra], [Tijera, Papel], [Piedra, Tijera], [Lagarto, Papel], [Piedra, Lagarto], [Tijera, Lagarto]]
GanaMaquina = [[Piedra, Papel], [Papel, Tijera], [Tijera, Piedra], [Papel, Lagarto], [Lagarto, Piedra], [Lagarto, Tijera]]

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
            Movimiento = input("Selecciona un movimiento ('p' para piedra / 'a' para papel / 't' para tijeras/ 'TERMINAR' para finalizar partida / 'l' para lagarto): ").lower()

            if Movimiento=='terminar':
                print("Tienes miedo?")
                break
            elif Movimiento in ['p','a','t','l'] :
                if Movimiento=='p':
                    EleccionUsuario = Piedra
                elif Movimiento == 'a':
                    EleccionUsuario = Papel
                elif Movimiento=='t':
                    EleccionUsuario = Tijera
                else:
                    EleccionUsuario=Lagarto

                print(f"Elección del ordenador: {EleccionOrdenador}")
                print(f"Elección del usuario: {EleccionUsuario}")

                resultado = FuncionGanador(EleccionUsuario, EleccionOrdenador)
                if resultado == 1:
                    print("Gana el usuario!!!")
                elif resultado == -1:
                    print("Gana el ordenador!!!")
                else:
                    print("Empate!!!")
                break
            else:
                print("Entrada incorrecta. Vuelve a intentar.")
    elif 'n' in Jugar.lower():
        break
    else:
        print('Entrada incorrecta. Vuelve a intentar.')
    print()
