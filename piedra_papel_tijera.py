import random

Piedra = 'piedra'
Papel = 'papel'
Tijera = 'tijera'
Lagarto = 'lagarto'
opciones = [Piedra, Papel, Tijera, Lagarto]
GanaJugador = [[Papel, Piedra], [Tijera, Papel], [Piedra, Tijera], [Lagarto, Papel], [Piedra, Lagarto], [Tijera, Lagarto]]
GanaMaquina = [[Piedra, Papel], [Papel, Tijera], [Tijera, Piedra], [Papel, Lagarto], [Lagarto, Piedra], [Lagarto, Tijera]]

def GeneraResultadoOrdenador():
    """Genera un movimiento aleatorio de la maquina"""
    return random.choice(opciones)

def FuncionGanador(EleccionUsuario, EleccionOrdenador):
    """
    .. include:: ../README.md

    Determina el resultado del juego basado en las elecciones del usuario y la máquina.

        Args:
            EleccionUsuario (str): Elección del usuario.
            EleccionOrdenador (str): Elección de la máquina.

        Returns:
            int: 1 si el jugador gana, -1 si la máquina gana, 0 si hay empate.
        """
    if [EleccionUsuario, EleccionOrdenador] in GanaJugador:
        return 1
    elif [EleccionUsuario, EleccionOrdenador] in GanaMaquina:
        return -1
    return 0

print("JUEGO : Piedra, papel, tijera y lagarto")
NombreUsuario = input("Dame tu nombre: ")
Intentos = int(input("¿Cuántos intentos quieres?: "))
PuntosUsuarios = 0
PuntosMaquina = 0

for _ in range(Intentos):
    Jugar = input("¿Quieres jugar? (s/n): ")
    if 's' in Jugar.lower():
        EleccionOrdenador = GeneraResultadoOrdenador()
        print(f"Te quedan {Intentos - _} intentos")
        Movimiento = input("Selecciona un movimiento ('p' para piedra / 'a' para papel / 't' para tijeras / 'l' para lagarto / 'TERMINAR' para finalizar partida): ").lower()

        if Movimiento == 'terminar':
            print("Tienes miedo?")
            break
        elif Movimiento in ['p', 'a', 't', 'l']:
            if Movimiento == 'p':
                EleccionUsuario = Piedra
            elif Movimiento == 'a':
                EleccionUsuario = Papel
            elif Movimiento == 't':
                EleccionUsuario = Tijera
            else:
                EleccionUsuario = Lagarto

            print(f"Elección del usuario: {EleccionUsuario}")
            print(f"Elección del ordenador: {EleccionOrdenador}")

            resultado = FuncionGanador(EleccionUsuario, EleccionOrdenador)
            if resultado == 1:
                print("¡Gana el usuario", NombreUsuario, "!")
                PuntosUsuarios += 1
            elif resultado == -1:
                print("¡Gana el ordenador!")
                PuntosMaquina += 1
            else:
                print("¡Empate!")
        else:
            print("Entrada incorrecta. Vuelve a intentar.")
    elif 'n' in Jugar.lower():
        break
    else:
        print('Entrada incorrecta. Vuelve a intentar.')

    print()

print("Juego terminado!")
print(f"Puntos de {NombreUsuario}: {PuntosUsuarios}")
print(f"Puntos del ordenador: {PuntosMaquina}")

if PuntosUsuarios > PuntosMaquina:
    print(f"¡El ganador es {NombreUsuario}!")
elif PuntosUsuarios < PuntosMaquina:
    print("¡El ganador es el ordenador!")
else:
    print("¡Empate!")
