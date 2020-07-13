x0 = 8370
digitos = 4
ui = 0
print("iteracion", "xn", "cuadrado", "Longuitud", "UI", "Random")
for i in range(1, 10):
    if (ui > 0):
        xn = ui
    else:
        xn = x0
    cuadrado = str(xn**2)
    lon = len(cuadrado)
    tem = ""
    for x in range(int(lon/2)-2, int(lon/2)):
        tem += cuadrado[x]
    for x in range(int(lon/2), int(lon/2)+2):
        tem += cuadrado[x]
    ui = int(tem)
    print(i, xn, cuadrado, lon, tem, (ui/10000))