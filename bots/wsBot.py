import pyautogui, webbrowser
from time import sleep

#contactos
contactos = {
    "Aaron" : "+5214426694515",
    "Sergio" : "+524423762341",
    "Fatima" : "+5214421782735"  
}

print(contactos)

contactoDeseado = input("Escriba el nombre del contacto a desear: ").capitalize()


#texto
textoMensajes = input("Escribe el mensaje: ")
numeroMensajes = int(input("Cuantos mensajes quieres mandar?: "))

webbrowser.open("https://web.whatsapp.com/send?phone=" + contactos[contactoDeseado])
#browser
sleep(5)

#loop
for num in range(numeroMensajes):
    pyautogui.typewrite(textoMensajes)
    pyautogui.press("enter")
    


print("Fin de mensaje")
    