import os

matriz=[
    ["Homero Simpson", "CEO", 1000000, 70000, 120000, 810000]
]

menu=("""
1. Registrar trabajador
2. Listar los todos los trabajadores
3. Imprimir planilla de sueldos
4. Salir del Programa
      """)
menu2=(''' PLANTILLA DE SUELDOS
       1.imprimir todos
       2.imprimir por cargo
       ''')

def buscarCargo(cargo):
    try: 
        for row in range(len(matriz)):
            if cargo == matriz[row][1]:
                return row 
        return -1 
    except:
        input("excepcion al buscar por cargo")


def registrar_trabajador():
        try:
            os.system("cls")
            nom = input("nombre: ")
            cargo =(input("cargo: "))
            sueldoB =int(input("sueldo: "))
            descSalud=sueldoB*0.07
            descAFP=sueldoB*0.12
            liquidoPagar=sueldoB-(descSalud+descAFP)
            matriz.append([nom,cargo,sueldoB,descSalud,descAFP,liquidoPagar])                 
            input("REGISTRO AGREGADO CON EXITO!")
        except:
            input("excepcion al ingresar")

def listado_Trabajadores():
    texto = '''                   LISTADO DE TRABAJADORES
------------------------------------------------------------------------------------------
Trabajador      | Cargo           | Sueldo Bruto | Desc.Salud | Desc.AFP | Líquido a pagar
------------------------------------------------------------------------------------------
'''
    for row in range(len(matriz)):
        texto += f"{matriz[row][0]:17s}" 
        texto += f"{matriz[row][1]:18s}"   
        texto += f"{matriz[row][2]:9d}"    
        texto += f"{matriz[row][3]:12d}"    
        texto += f"{matriz[row][4]:13d}"   
        texto += f"{matriz[row][5]:13d}"   
        texto += '\n' 

    input(texto)


def plantillaSueldos():
    try:
        os.system("cls")
        print("BÚSQUEDA AVANZADA POR CARGO")
        row = buscarCargo(input("cargo a buscar: "))
        texto = '''                   LISTADO DE TRABAJADORES
------------------------------------------------------------------------------------------
Trabajador      | Cargo           | Sueldo Bruto | Desc.Salud | Desc.AFP | Líquido a pagar
------------------------------------------------------------------------------------------
'''
        if row > -1:
            for row in range(len(matriz)):
                texto += f"{matriz[row][0]:17s}" 
                texto += f"{matriz[row][1]:18s}"   
                texto += f"{matriz[row][2]:9d}"    
                texto += f"{matriz[row][3]:12d}"    
                texto += f"{matriz[row][4]:13d}"   
                texto += f"{matriz[row][5]:13d}"   
                texto += '\n' 
                return texto
        else:
            input("no ha sido encontrado...")
    except:
        input("Excepcion al buscar")



def crearArchivo(): 
    with open('personas.txt','w', encoding='utf-8') as documento:
        documento.write(plantillaSueldos())


while True:
    os.system("cls")
    try:
        opc=int(input(menu))
        if opc ==1:
            registrar_trabajador()
        elif opc ==2:
            listado_Trabajadores()
        elif opc ==3:
            try:
                opc2=int(input(menu2))
                if opc2==1:
                    listado_Trabajadores()
                elif opc2==2:
                    plantillaSueldos()  
                    crearArchivo()
            except:
                input("Excepcion de opcion")
        elif opc==4:
            break
        else:
            input("opcion no valida")

    except:
        input("excepcion en menu")

