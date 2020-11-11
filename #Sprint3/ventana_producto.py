import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

builder = Gtk.Builder()
builder.add_from_file("producto.glade")

class Producto(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="")

    def mostrarProducto(self):
        builder = Gtk.Builder()
        builder.add_from_file("producto.glade")

        window = builder.get_object("window")
        window.show_all()
