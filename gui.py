from tkinter import*
from PIL import ImageTk, Image
import database

root=Tk()
root.config( bg="#CBA16F")
root.geometry("1000x600+300+50")
root.title("Registro de usuario")
root.resizable(False, False)

nombre = StringVar()
correo = StringVar()
clave = StringVar()


def insert_db():     
    nombre = entry_nombre.get()
    correo = entry_correo.get()
    clave = entry_clave.get()
    cliente_db = database.MyDatabase()
    cliente_db.insert_db(nombre, correo, clave)
    
    
def read_db():
    cliente_db = database.MyDatabase()
    cliente_db.read_db()
    fila = 0 
    for user in database.data:
        registro = user
        print('RESULTADO - FrontEnd: ' + str(fila) + " - " + str(registro))
        title1 = Label(frame_datos, 
              text=registro, 
              font=("Century Gothic", "15", "bold"),width=32,
              justify=LEFT, bg="#B77E55")
        title1.place(x=50, y=530)
        fila = fila + 1   

frame_datos= Frame(root, bg="#CBA16F", width="500", height="600")
frame_datos.place( x=0, y=0)

my_image = ImageTk.PhotoImage(Image.open("ganchos.jpeg"))
my_label = Label(image=my_image, bg="#CBA16F")
my_label.place(x=500,y=-400)

titulo=Label(frame_datos, text="¡Regístrate!",fg="black", font=("Verdana", 20), bg="#B77E55", width="29", height="1").place( x=3, y=20)

Label(frame_datos, text="Nombre:", font=("Century Gothic", 20), width=10, fg="white", bg="#CBA16F").place(x=30, y=90) 
entry_nombre=Entry(frame_datos, width=30, font=("Verdana", 15))
entry_nombre.place(x=53, y=130)

Label(frame_datos, text="Correo Electrónico:", font=("Century Gothic", 20), width=17, fg="white", bg="#CBA16F").place(x=38, y=185) 
entry_correo=Entry(frame_datos, width=30, font=("Verdana", 15))
entry_correo.place(x=53, y=225)

Label(frame_datos, text="Contraseña:", font=("Century Gothic", 20), width=10, fg="white", bg="#CBA16F").place(x=50, y=285) 
entry_clave=Entry(frame_datos, width=30, font=("Verdana", 15))
entry_clave.place(x=53, y=325)

boton_registrarse = Button(frame_datos, text="Registrarse",font=("Century Gothic", 11), bg="#B77E55", width=17, height=2, command=insert_db)
boton_registrarse.place(x=65, y=410)

boton_ver = Button(frame_datos, text="Ver Registro",font=("Century Gothic", 11), bg="#B77E55", width=17, height=2, command=read_db)
boton_ver.place(x=265, y=410)

root.mainloop()