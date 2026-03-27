def rectangle():
    """Lee base y altura de un rectángulo, calcula e imprime
    el área y el perímetro.
    """
    base = int(input("Base: "))
    altura = int(input("Altura: "))
    area = base * altura
    perimetro = (base + altura)*2
    print(area)
    print(perimetro)