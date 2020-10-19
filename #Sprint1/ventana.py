import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from componente_adivinanza import ComponenteAdivinanza

class Ventana(Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self)
		box = Gtk.Box(orientation = Gtk.Orientation.VERTICAL)
		self.add(box)
		box.pack_start(ComponenteAdivinanza("Soy un mes de vacaciones, con nombre de emperador. A veces refresco el rostro, otras doy mucho calor.", "Agosto"), True, True, 0)
		box.pack_start(ComponenteAdivinanza("Si me nombras desaparezco, ¿quien soy?", "El silencio"), True, True, 0)
		box.pack_start(ComponenteAdivinanza("Desde el lunes hasta el viernes, soy la última en llegar, el sábado soy la primera y el domingo a descansar.", "La letra S"), True, True, 0)
		box.pack_start(ComponenteAdivinanza("Termino cabeza arriba, empiezo cabeza abajo, y tan solo preguntar es mi trabajo.", "El signo de interrogación"), True, True, 0)
