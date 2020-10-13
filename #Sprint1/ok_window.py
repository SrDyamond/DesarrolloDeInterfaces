import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class OkWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="")
        label = Gtk.Label("Contraseña Correcta")
        label.set_padding(50,50)
        self.add(label)
