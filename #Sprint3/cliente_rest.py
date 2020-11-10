import requests

class ClienteRest:
	def solicitar_lista_productos(self):
		response = requests.get('http://localhost:8080/product')
		return response.json()

    def solicitar_producto(self, referencia):
    	response = requests.get('http://localhost:8080/product/' + referencia)
    	return response.json()

    
