import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from ventana_reservas import Reservas

builder = Gtk.Builder()
builder.add_from_file("catalogo.glade")


class Catalogo (Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Catalogo")

        boton_reservas = builder.get_object("Boton_Reservas")
        boton_reservas.connect("clicked", self.on_button1_clicked)

        boton_pagar = builder.get_object("Boton_Pagar")
        boton_pagar.connect("clicked", self.on_button2_clicked)

    def on_button1_clicked(self, widget):
        print("hola")

    def on_button2_clicked(self, widget):
        print("clic")

        # window = Reservas()
        # window.show_all()


window = builder.get_object("window")
window.connect("destroy", Gtk.main_quit)
window.show_all()

Gtk.main()
