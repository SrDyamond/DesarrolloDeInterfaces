import gi
import threading
import time
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

def thread_function(numero, ventana):
	i = 0
	while ventana.ha_cerrado == False:
		time.sleep(1)
		ventana.label.set_text(str(i))
		i = i + 1

class Ventana(Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self, title="")
		self.ha_cerrado = False
		self.label = Gtk.Label(label="Comenzando...")
		self.add(self.label)
		self.label.set_margin_bottom(50)
		self.label.set_margin_top(50)
		self.label.set_margin_start(100)
		self.label.set_margin_end(100)
		x = threading.Thread(target=thread_function, args=(1,self))
		x.start()

	def cerrar(self, widget):
		self.ha_cerrado = True

###############################
#
# Punto de entrada del programa

ventana = Ventana()
ventana.connect("destroy", ventana.cerrar)
ventana.connect("destroy", Gtk.main_quit)
ventana.show_all()

Gtk.main()
