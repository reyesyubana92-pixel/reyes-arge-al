matriculados = {"Ana", "Hugo", "Lucas", "Sara"}
asistentes = {"Ana", "Lucas"}

ausentes = matriculados.difference(asistentes)
print(f"Estudiantes ausentes en la sesión: {ausentes}")