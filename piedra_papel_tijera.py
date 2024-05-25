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
NombreUsuario = input("Dame tu nombre: ")
Intentos = int(input("¿Cuántos intentos quieres?: "))
PuntosUsuarios = 0
PuntosMaquina = 0

for _ in range(Intentos):
    Jugar = input("¿Quieres jugar? (s/n): ")
    if 's' in Jugar.lower():
        EleccionOrdenador = GeneraResultadoOrdenador()
        print(f"Te quedan {Intentos - _} intentos")
        Movimiento = input("Selecciona un movimiento ('p' para piedra / 'a' para papel / 't' para tijeras): ").lower()

        if Movimiento in ['p', 'a', 't']:
            if Movimiento == 'p':
                EleccionUsuario = Piedra
            elif Movimiento == 'a':
                EleccionUsuario = Papel
            elif Movimiento == 't':
                EleccionUsuario = Tijera

            print(f"Elección del ordenador: {EleccionOrdenador}")
            print(f"Elección del usuario: {EleccionUsuario}")

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
