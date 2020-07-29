from usuario import Usuario

class Profesor(Usuario):

	def __init__(self, departamento="", **kwargs):
		super().__init__(**kwargs)
		self.__departamento = departamento

	@property
	def departamento(self):
		return self.__departamento

	def __str__ (self):
		return "{} Departamento: {}".format(super().__str__(), self.__departamento)
	
	def leer_datos(self):
		super().leer_datos()
		self.__departamento = input("Introduce el departamento: ")
