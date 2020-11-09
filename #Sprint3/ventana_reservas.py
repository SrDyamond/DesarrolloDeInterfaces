import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

builder = Gtk.Builder()
builder.add_from_file("reservas.glade")

class Reservas(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="")
        window = builder.get_object("window")
        
