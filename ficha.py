from gettext import find


def ficha():
    """Ejercicio integrador. Lee nombre, email y 3 notas, y genera una ficha
    de alumno aplicando: strip, title, lower, upper, int, len, find, slicing,
    reverse, replace, count, in, f-strings, strings multilínea y operaciones matemáticas.
    """
    # Ejercicio integrador: Generador de Ficha de Alumno
    #
    # Leer mediante input:
    #   1. Nombre completo (puede tener espacios extra y mayúsculas mezcladas)
    #   2. Email (puede tener mayúsculas)
    #   3. Tres notas (como texto, hay que convertirlas)
    #
    # Generar una ficha que incluya:
    #   - Encabezado decorativo usando un string multilínea con "="
    #   - Nombre limpio: sin espacios extra y con formato título
    #   - Email en minúsculas
    #   - Cantidad de caracteres del nombre
    #   - Iniciales: usar find para encontrar el espacio e indexar las letras
    #   - Usuario: apellido.nombre en minúsculas
    #   - Verificar si el email contiene @ 
    #   - Extraer el dominio del email
    #   - Nombre con guion bajo en vez de espacio
    #   - Contar las 'a' en el nombre
    #   - Código secreto: nombre invertido en mayúsculas
    #   - Las 3 notas, su suma, promedio y promedio entero
    #   - Cierre decorativo usando repetición de string ("=" * 24)
    nombre_completo= input("Ingrese nombre: ")
    Email= input("ingrese email: ")
    nota1= input("Nota 1: ")
    nota2 = input("Nota 2: ")
    nota3 = input("Nota 3: ")
    print("""========================
    FICHA DEL ALUMNO
========================""")
    print(f"Nombre: {nombre_completo.strip().title()}")
    print(f"Email: {Email.lower()}")
    print(f"Caracteres en nombre: {len(nombre_completo.strip())}")
    print(f"Iniciales: {nombre_completo.title().strip()[0]}{nombre_completo.strip().title()[nombre_completo.title().strip().find(" ")+1]}")
    print(f"Usuario: {nombre_completo.lower().strip()[nombre_completo.strip().find(' '): ]}.{nombre_completo.lower().strip()[0:nombre_completo.strip().find(' ')+1]}")
    print(f"Email valido: {"@" in Email}")
    print(f"Dominio: {Email[(Email.find('@')):]}")
    print(f"Nombre para archivo: {nombre_completo.strip().title().replace(" ","_")}")
    print(f"Cantidad de a: {nombre_completo.lower().count("a")}")
    print(f"Código secreto: {nombre_completo.upper()[::-1]}")
    print(nota1)
    print(nota2)
    print(nota3)
    nota1= int(nota1)
    nota2= int(nota2)
    nota3= int(nota3)
    suma= nota1+nota2+nota3
    promedio= (nota1+nota2+nota3)/3
    promedio_entero= (nota1+nota2+nota3)//3
    print(suma)
    print(promedio)
    print(promedio_entero)
    print("="*24)