import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from password_fail.py import PasswordFail
from password_ok.py import PasswordOk

class PasswordWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Contraseña")

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        self.entry = Gtk.Entry()
        self.entry.set_text("Introduzca su contraseña")
        vbox.pack_start(self.entry, True, True, 0)

        hbox = Gtk.Box(spacing=6)
        vbox.pack_start(hbox, True, True, 0)

        self.check_visible = Gtk.CheckButton(label="Visible")
        self.check_visible.connect("toggled", self.on_visible_toggled)
        self.check_visible.set_active(True)
        hbox.pack_start(self.check_visible, True, True, 0)


        button = Gtk.Button(label="Aceptar")
        button.connect("clicked", self.on_button_clicked)
        vbox.pack_start(button, True, True, 0)

    def on_visible_toggled(self, button):
        value = button.get_active()
        self.entry.set_visibility(value)

    def on_button_clicked(self, widget):
        if self.entry.get_text() == "pass":
            window = PasswordOk()
            window.show_all()
            Gtk.main()
        else:
            window = PasswordFail()
            window.show_all()

            Gtk.main()

window = PasswordWindow()
window.connect("destroy", Gtk.main_quit)
window.show_all()

Gtk.main()
