# FORMULARIO DE REGISTRO
# ALMACENAMIENTO EN TXT SIN VALIDACION

from ast import IfExp
import tkinter as tk
# Definir funciones
def limpiar_campos():
    tbNombre.delete(0, tk.END)
    tbApellido.delete(0, tk.END)
    tbEdad.delete(0, tk.END)
    tbTelefono.delete(0, tk.END)
    tbEstatura.delete(0, tk.END)
    variable_genero.set(0)
   
def borrar():
    limpiar_campos()
    
def guardar_valores():
    #obteber valores desde los entrys
    nombres = tbNombre.get()
    apellidos = tbApellido.get()
    edad = tbEdad.get()
    estatura = tbEstatura()
    telefono = tbTelefono.get()
    #Obtener genero de los radiobutton
    genero = ""
    if variable_genero.get() == 1:
        genero = "Masculino"
    elif variable_genero.get()==2:
        genero = "Femenino"

    # Generar cadena de caracteres
    datos = "Nombres: " + nombres + "\n"+"Apellidos: " + apellidos + "\n" + "Edad: " + edad + "\n" +"Estatura: " + estatura + "\n"+ "Telefono: " + telefono + "\n" + "Genero: " + genero + "\n"
    

# Creacion de ventana
ventana = tk.Tk()
ventana.geometry("500x500")
ventana.title("Formulario de registro")
ventana.configure(bg = 'light blue') #bg= background
label_font = ('Verdana', 10, 'bold') #font = fuente
entry_font = ('Verdana', 11)
rb_font= ('Verdana', 9, 'bold')
btn_font = ('Verdana', 12, 'bold')


# Crear variable para radiobutton
variable_genero = tk.IntVar() #metodo para hacer el selected de c#

# Creacion de etiquetas y campos de entrada
lbNombre = tk.Label(ventana, text="Nombres: ", bg="light blue", font=label_font)
lbNombre.pack(pady=5)
tbNombre = tk.Entry(ventana, font= entry_font)
tbNombre.pack()


lbApellido = tk.Label(ventana, text="Apellidos: ", bg = "light blue", font=label_font)
lbApellido.pack(pady=5)
tbApellido = tk.Entry(ventana, font= entry_font)
tbApellido.pack()

lbEdad = tk.Label(ventana, text="Edad",bg="light blue", font= label_font)
lbEdad.pack(pady=5)
tbEdad = tk.Entry(ventana, font= entry_font)
tbEdad.pack()

lbTelefono = tk.Label(ventana, text="Telefono: ", bg="light blue", font = label_font)
lbTelefono.pack(pady=5)
tbTelefono = tk.Entry(ventana, font= entry_font)
tbTelefono.pack()

lbEstatura = tk.Label(ventana, text="Estatura: ", bg="light blue", font= label_font)
lbEstatura.pack(pady=5)
tbEstatura = tk.Entry(ventana, font= entry_font)
tbEstatura.pack()

lbGenero = tk.Label(ventana, text="Genero: ", bg="light blue", font= label_font)
lbGenero.pack(pady=5)
rbMasculino = tk.Radiobutton(ventana, text="Masculino", variable = variable_genero, value=1, bg="light blue", font = rb_font)
rbMasculino.pack()
rbFemenino = tk.Radiobutton(ventana, text="Femenino", variable = variable_genero, value =2, bg="light blue", font = rb_font)
rbFemenino.pack()

btnGuardar = tk.Button(ventana, text="Guardar",  bg = "light gray", font= btn_font)
btnGuardar.pack(pady=5)
btnBorrar = tk.Button(ventana, text="Borrar valores", command= borrar ,bg = "light gray", font= btn_font)
btnBorrar.pack(pady=5)





ventana.mainloop()

