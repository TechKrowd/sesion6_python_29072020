from usuario import Usuario

class Alumno(Usuario):

	def __init__(self, nota=0, **kwargs):
		super().__init__(**kwargs)
		self.__nota = nota

	@property
	def nota(self):
		return self.__nota

	def __str__(self):
		return "{} Nota: {}".format(super().__str__(), self.__nota)
	
	def leer_datos(self):
		super().leer_datos()
		nota = input("Introduce la nota: ")
		if nota.isdigit():
			self.__nota = int(nota) if int(nota)>=0 and int(nota)<=10 else 0
		else:
			self.__nota = 0