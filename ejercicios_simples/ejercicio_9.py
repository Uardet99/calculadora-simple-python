inversion = int(input("¿Que cantidad de dinero le gustaria invertir?"))
interes = int(input("¿Que interes anual le gustaria obtener?"))
anios = int(input("¿Durante cuantos años le gustaria mantener la inversion?"))

beneficioInteres = (inversion * (interes / 100)) + inversion

print("Capital obtenido de la inversion", (beneficioInteres * anios))

# https://aprendeconalf.es/docencia/python/ejercicios/tipos-datos/