import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from ventana_reservas import Reservas
from ventana_producto import Producto

builder = Gtk.Builder()
builder.add_from_file("catalogo.glade")

boton_reservas = builder.get_object("Boton_Reservas")
boton_reservas.connect("clicked", Reservas.mostrarReservas)

boton_1=builder.get_object("Boton1")
boton_1.connect("clicked",Producto.mostrarProducto)
boton_2=builder.get_object("Boton2")
boton_2.connect("clicked",Producto.mostrarProducto)
boton_3=builder.get_object("Boton3")
boton_3.connect("clicked",Producto.mostrarProducto)
boton_4=builder.get_object("Boton4")
boton_4.connect("clicked",Producto.mostrarProducto)
boton_5=builder.get_object("Boton5")
boton_5.connect("clicked",Producto.mostrarProducto)
boton_6=builder.get_object("Boton6")
boton_6.connect("clicked",Producto.mostrarProducto)
boton_7=builder.get_object("Boton7")
boton_7.connect("clicked",Producto.mostrarProducto)
boton_8=builder.get_object("Boton8")
boton_8.connect("clicked",Producto.mostrarProducto)
boton_9=builder.get_object("Boton9")
boton_9.connect("clicked",Producto.mostrarProducto)
boton_10=builder.get_object("Boton10")
boton_10.connect("clicked",Producto.mostrarProducto)

window = builder.get_object("window")
window.connect("destroy", Gtk.main_quit)
window.show_all()

Gtk.main()
