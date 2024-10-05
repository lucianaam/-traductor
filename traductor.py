traductor = {
            "JUICIOSO": "Es una persona responsable",
            "AGUACATE": "es una fruta que en algunos paises se le conoce como palta",
            "ESFERO": "Tambien conocido como boligrafo"
            "EH AVE MARIA": "se utiliza para expresar sorpresa"
            }
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
           
if word in traductor.keys():
    print ("el significado de la palabra ingresada es:", traduccion[word] )
    # ¿Qué debemos hacer si se encuentra la palabra?
else:
    print ("esa palabra no se encuentra en el diccionario")
