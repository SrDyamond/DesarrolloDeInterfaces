import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class PasswordWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Contraseña")

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        self.entry = Gtk.Entry()
        self.entry.set_text("Introduzca su contraseña")
        self.entry.set_visibility(False)
        vbox.pack_start(self.entry, True, True, 0)

        button = Gtk.Button(label="Aceptar")
        button.connect("clicked", self.on_button_clicked)
        vbox.pack_start(button, True, True, 0)

    def on_button_clicked(self, widget):
        if self.entry.get_text() == "pass":
            print("Correcta. Cerrando ventana...")
            Gtk.main_quit()
        else:
            window = Gtk.Window(title="Contraseña Incorrecta")
            window.show()
            window.connect("destroy", Gtk.main_quit)
            Gtk.main()

window = PasswordWindow()
window.connect("destroy", Gtk.main_quit)
window.show_all()

Gtk.main()
