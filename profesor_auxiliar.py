from profesor import Profesor
from alumno import Alumno

class ProfesorAuxiliar(Profesor, Alumno):

	def __init__(self, asignatura="", **kwargs):
		super().__init__(**kwargs)
		self.__asignatura = asignatura

	@property
	def asignatura(self):
		return self.__asignatura

	def __str__(self):
		return "{} Asignatura: {}".format(super().__str__(), self.__asignatura)

	def leer_datos(self):
		super().leer_datos()
		self.__asignatura = input("Introduce la asignatura: ")
	