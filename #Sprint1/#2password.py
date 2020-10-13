import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from passwordOk import WindowOk
from passwordFail import WindowFail

class PasswordWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Pass")
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(box)

        label = Gtk.Label("Introduce tu contraseña")
        label.set_padding(50,50)
        box.pack_start(label, True, True, 0)

        self.entry = Gtk.Entry()
        box.pack_start(self.entry, True, True, 0)
        self.entry.set_visibility(False)

        button = Gtk.Button(label="Aceptar")
        button.connect("clicked", self.on_button_clicked)
        box.pack_start(button, True, True, 0)

    def on_button_clicked(self, widget):
        if self.entry.get_text() == "pass":
            window = WindowOk()
            window.show_all()
        else:
            window = WindowFail()
            window.show_all()

window = PasswordWindow()
window.connect("destroy", Gtk.main_quit)
window.show_all()

Gtk.main()
