import time


def mimir(energy):
    while energy < 100:
        print(
            f"jorgito necesita dormir, ahora solo tiene {energy}% de energia")
        time.sleep(0.1)
        energy += 1
    print(f"jorgito recargado. {energy}% de energia")


input = int(input("cuanto porcentaje de energia le queda a jorgito? "))
if input <= 10:
    mimir(input)
else:
    print(f"a jorgito le queda {input} de energia, vuelva mas tarde")
