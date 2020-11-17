import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from ventana_reservas import Reservas
from controlador_catalogo import CatalogoControlador

builder = Gtk.Builder()
builder.add_from_file("catalogo.glade")

controlador = CatalogoControlador(builder)

boton_reservas = builder.get_object("Boton_Reservas")
boton_reservas.connect("clicked", Reservas.mostrarReservas)



window = builder.get_object("window")
window.connect("destroy", Gtk.main_quit)
window.show_all()

Gtk.main()
