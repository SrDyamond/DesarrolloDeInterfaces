import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from calculadora_controlador import Controlador

builder = Gtk.Builder()
builder.add_from_file("calculadora.glade")

label_resultado = builder.get_object("label_result")
controlador = Controlador(label_resultado)

boton0 = builder.get_object("button0")
boton0.connect("clicked", controlador.ha_pulsado,0)
boton1 = builder.get_object("button1")
boton1.connect("clicked", controlador.ha_pulsado,1)
boton2 = builder.get_object("button2")
boton2.connect("clicked", controlador.ha_pulsado,2)
boton3 = builder.get_object("button3")
boton3.connect("clicked", controlador.ha_pulsado,3)
boton4 = builder.get_object("button4")
boton4.connect("clicked", controlador.ha_pulsado,4)
boton5 = builder.get_object("button5")
boton5.connect("clicked", controlador.ha_pulsado,5)
boton6 = builder.get_object("button6")
boton6.connect("clicked", controlador.ha_pulsado,6)
boton7 = builder.get_object("button7")
boton7.connect("clicked", controlador.ha_pulsado,7)
boton8 = builder.get_object("button8")
boton8.connect("clicked", controlador.ha_pulsado,8)
boton9 = builder.get_object("button9")
boton9.connect("clicked", controlador.ha_pulsado,9)

boton_punto = builder.get_object("button_dot")
boton_punto.connect("clicked", controlador.ha_pulsado_punto)
boton_borrar = builder.get_object("buttonC")
boton_borrar.connect("clicked", controlador.ha_pulsado_borrar)

boton_dividir = builder.get_object("button_divide")
boton_dividir.connect("clicked", controlador.ha_pulsado_op,"/")
boton_multiplicar = builder.get_object("button_multiply")
boton_multiplicar.connect("clicked", controlador.ha_pulsado_op,"*")
boton_sumar = builder.get_object("button_plus")
boton_sumar.connect("clicked", controlador.ha_pulsado_op,"+")
boton_restar = builder.get_object("button_minus")
boton_restar.connect("clicked", controlador.ha_pulsado_op,"-")
boton_igual = builder.get_object("button_equals")
boton_igual.connect("clicked", controlador.ha_pulsado_op,"none")

window = builder.get_object("window")
window.connect("destroy", Gtk.main_quit)
window.show_all()

Gtk.main()
