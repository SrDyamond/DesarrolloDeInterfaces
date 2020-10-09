import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class PasswordOk(Gtk.Window):
    def __init__(self):
            Gtk.Window.__init__(self, title="Contraseña Correcta")

            vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
            self.add(vbox)

            self.entry = Gtk.Entry()
            self.entry.set_text("Contraseña correcta")
            self.entry.set_editable(False)
            vbox.pack_start(self.entry, True, True, 0)

window = PasswordOk()
window.show_all()

Gtk.main()
