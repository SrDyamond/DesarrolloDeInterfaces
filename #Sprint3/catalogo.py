import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from ventana_reservas import Reservas
from producto import MyWindow

builder = Gtk.Builder()
builder.add_from_file("catalogo.glade")

boton_reservas = builder.get_object("Boton_Reservas")
boton_reservas.connect("clicked", Reservas.mostrarReservas)

#boton_1=builder.get_object("Boton1")
#boton_1.connect("clicked",MyWindow.ventana)

window = builder.get_object("window")
window.connect("destroy", Gtk.main_quit)
window.show_all()

Gtk.main()
