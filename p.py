estudiantes=[]
def registro_estudiante(n1,n2,n3,n4,rut,nombre):
    estudiante = {
        'rut':rut, 
        'nombre':nombre,
        'n1':n1,
        'n2': n2,
        'n3': n3,
        'n4': n4,
    }
    estudiantes.append(estudiante)
def verificar_rut(rut):
    rutp = rut.split('-')
    if len(rutp) !=2:
        return False
    numero, verificadorut = rutp
    if not numero.isdigit() or (not verificadorut.isdigit() and verificadorut.upper() != 'K'):
        return False
    return len(numero) >= 7 and len(numero) <= 8
def calcular_notafinal(n1,n2,n3,n4, examenfinal):
    nota_presc = (n1 * 0.3) + (n2 * 0.3) + (n3 * 0.3) + (n4 * 0.3)
    nota_final= (nota_presc * 0.6) + (examenfinal * 0.6)
    return nota_final
def menu():
    while True:
        print(""
                  Menu estudiantes 
                  1. registrar estudiante 
                  2. mostrar estudiantes
                  3. buscar estudiante por su rut 
                  4. salir
        "")
        opcion =input("selecciona una opcion del menu")
        if opcion == '1':
         registro_estudiante()
        elif opcion == '2':
         mostrar_estudiante()
        elif opcion == '3':
            rut = input("ingresa el rut del estudiante")
        elif opcion == '4':    
            print("cerraste el menu")
            break
        else: 
            print ("opcion invalida, intenta de nuevo")
def registro_estudiante():
 rut = input("ingresa el rut del estudiante sin puntos y con guion")
if not verificar_rut:
    print("rut invalido, ingresa rut sin puntos y con guion")
nombre = input("ingresa el nombre del estudiante")
try:
    n1 = float(input("ingresa tu primera nota"))
    n2 = float(input("ingresa tu segunda nota"))
    n3 = float(input("ingresa tu tercera nota"))
    n4= float(input("ingresa la cuarta nota"))
except ValueError:
    print("la nota ingresada no es valida, ingresa tus notas nuevamente")
    return

    

