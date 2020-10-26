class Controlador:

	# Inicializador

	def __init__(self, label_resultado):
		self.operacion_pulsada = None
		self.primer_operando = None
		self.ha_pulsado_operacion_o_igual = False
		self.label_resultado = label_resultado
		self.label_resultado.set_text("")

	# Metodos que responden a las acciones del usuario

	# Botones numericos
	def ha_pulsado(self, widget,pulsado):
		posicion = pulsado
		print (posicion)
		self._limpiar_pantalla_si_es_necesario()
		texto_actual = self.label_resultado.get_text()
		self.label_resultado.set_text(texto_actual + str(posicion) )

	# Botones de coma decimal y borrado

	def ha_pulsado_punto(self, widget):
		if self._ha_introducido_punto() == False:
			# El usuario todavia no ha introducido una coma decimal
			texto_actual = self.label_resultado.get_text()
			self.label_resultado.set_text(texto_actual + ".")
		else:
			# Ya hay una coma decimal en pantalla.
			# No hacemos nada. No puede haber un número con 2 comas decimales
			pass

	def ha_pulsado_borrar(self, widget):
		self.operacion_pulsada = None
		self.primer_operando = None
		self.ha_pulsado_operacion_o_igual = False
		self.label_resultado.set_text("")

	# Botones de operacion

	def ha_pulsado_sumar(self, widget):
		self.ha_pulsado_operacion_o_igual = True
		self._operar_y_mostrar_resultado_si_es_necesario()
		self.primer_operando = float(self.label_resultado.get_text())
		self.operacion_pulsada = "+"

	def ha_pulsado_restar(self, widget):
		self.ha_pulsado_operacion_o_igual = True
		self._operar_y_mostrar_resultado_si_es_necesario()
		self.primer_operando = float(self.label_resultado.get_text())
		self.operacion_pulsada = "-"

	def ha_pulsado_multiplicar(self, widget):
		self.ha_pulsado_operacion_o_igual = True
		self._operar_y_mostrar_resultado_si_es_necesario()
		self.primer_operando = float(self.label_resultado.get_text())
		self.operacion_pulsada = "*"

	def ha_pulsado_dividir(self, widget):
		self.ha_pulsado_operacion_o_igual = True
		self._operar_y_mostrar_resultado_si_es_necesario()
		self.primer_operando = float(self.label_resultado.get_text())
		self.operacion_pulsada = "/"

	def ha_pulsado_igual(self, widget):
		self.ha_pulsado_operacion_o_igual = True
		self._operar_y_mostrar_resultado_si_es_necesario()
		self.primer_operando = None
		self.operacion_pulsada = None

	# Metodos de uso preferiblemente privado

	def _operar_y_mostrar_resultado_si_es_necesario(self):
		if self.primer_operando is not None:
			valor_actual = float(self.label_resultado.get_text())
			resultado = self._efectuar_operacion(self.primer_operando, valor_actual, self.operacion_pulsada)
			self.label_resultado.set_text(str(round(resultado, 5)))

	def _efectuar_operacion(self, op1, op2, operacion):
		assert op1 is not None, "Inconsistencia"
		assert op2 is not None, "Inconsistencia"
		if operacion == "+":
			return op1 + op2
		elif operacion == "-":
			return op1 - op2
		elif operacion == "*":
			return op1 * op2
		elif operacion == "/":
			return op1 / op2
		else:
			assert False, "Inconsistencia"

	def _ha_introducido_punto(self):
		try:
			posicion = self.label_resultado.get_text().index('.')
			print("Se introdujo una coma decimal, tecleada en la " + posicion + " pulsacion")
			return True
		except ValueError:
			return False

	def _limpiar_pantalla_si_es_necesario(self):
		if self.ha_pulsado_operacion_o_igual:
			self.ha_pulsado_operacion_o_igual = False
			self.label_resultado.set_text("")
