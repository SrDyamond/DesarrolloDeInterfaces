import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from cliente_rest import ClienteRest
import threading
import shutil
import requests

def descargar_imagen(url_imagen):
	# Descargo la imagen
	r = requests.get(url_imagen, stream = True)
	with open("temp.png", 'wb') as f:
		shutil.copyfileobj(r.raw, f)
	imagen = Gtk.Image()
	imagen.set_from_file("temp.png")
	return imagen


class Producto(Gtk.Window):
	def __init__(self,referencia,imagenproducto,nombre):
		Gtk.Window.__init__(self, title="Producto")
		self.set_default_size(1366 , 768 )

		scrolled = Gtk.ScrolledWindow()
		scrolled.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
		self.add(scrolled)

		contenedor = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
		scrolled.add(contenedor)
		self.add(contenedor)

		caja1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
		contenedor.pack_start(caja1,True,True,0)

		caja2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
		contenedor.pack_start(caja2,True,True,0)

		caja3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
		caja2.pack_start(caja3,True,True,0)

		imagen=descargar_imagen(imagenproducto)
		caja1.pack_start(imagen,True,True,0)

		nom = Gtk.Label()
		nom.set_line_wrap(True)
		nom.set_markup("<b>"+nombre+"</b>")
		caja1.pack_start(nom,True,True,0)

		ref = Gtk.Label(label=referencia)
		caja1.pack_start(ref,True,True,0)

		precio = Gtk.Label(label="Precio:13000")
		precio.set_line_wrap(True)
		precio.set_max_width_chars(50)
		caja3.pack_start(precio,True,True,0)


		reservar = Gtk.Image()
		reservar.set_from_file("boton-reservar.png")
		button = Gtk.Button()
	#	button.connect("clicked", self.on_button_clicked)
		button.add(reservar)
		button.set_size_request(50,50)
		caja3.pack_start(button, True, True, 0)

	#	def on_button_clicked(self,widget):
	#		print("Reservado")
