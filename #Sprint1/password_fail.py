import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class PasswordFail(Gtk.Window):
    def __init__(self):
            Gtk.Window.__init__(self, title="ERROR")

            vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
            self.add(vbox)

            self.entry = Gtk.Entry()
            self.entry.set_text("Fallo en la contraseña")
            self.entry.set_editable(False)
            vbox.pack_start(self.entry, True, True, 0)

window = PasswordFail()
window.show_all()

Gtk.main()
