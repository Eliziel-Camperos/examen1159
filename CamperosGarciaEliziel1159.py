class Comics:
    def __init__(self):
        self.id1159 = ""  
        self.serie1159 = ""  
        self.genero1159 = ""  
        self.cven1159 = 0  
        self.autor1159 = ""  
        self.color1159 = ""  
        self.precio1159 = 0.0  


    def mostrar_datos1159(self):
        print(f"ID:              {self.id1159}")
        print(f"Serie:           {self.serie1159}")
        print(f"Género:          {self.genero1159}")
        print(f"Cómics Vendidos: {self.cven1159}")
        print(f"Autor:           {self.autor1159}")
        print(f"Color:           {self.color1159}")
        print(f"Precio:          {self.precio1159}")
    def ID1159(self, id_comic):
        self.id1159 = id_comic
    def Serie1159(self, serie):
        self.serie1159 = serie
    def lista_ID1159(self):
        return ["454", "742", "735", "777", "222", "9999", "043"]
    def lista_series1159(self):
        return ["Spiderman", "Iron Man", "X-Men", "Chaos + Order", "Jujutsu Kaizen", "One Piece", "Deadpool"]
    def lista_generos1159(self):
        return ["Acción, superheroes, Ciencia Ficción, Fantasía","Acción, superheroes, Ciencia Ficción, Fantasía, Drama","Acción, superheroes, Ciencia Ficción, Fantasía, Comedia, Drama""Acción, superheroes, Ciencia Ficción, Fantasía, Comedia, Drama, horror","Acción, superheroes, Ciencia Ficción, Fantasía, Comedia, Drama, aventura","Acción, Superhéroes, Ciencia ficción, Comedia"]
    def lista_cven1159(self):
        return [1000, 900, 800, 750, 650, 1200, 1100]
    def lista_autores1159(self):
        return ["Stan Lee, Steve Ditko", "Stan Lee, Jack Kirby, Larry Lieber, Don Heck", "Stan lee", "Elicrafting","GeGe Akutami", "Eiichiro Oda", "Rob Liefeld, Fabian Nicieza"]
    def lista_colores1159(self):
        return ["Color", "Color", "Color", "Color", "Blanco y negro", "Blanco y negro", "Color"]
    def lista_precios1159(self):
        return [4.99, 8.99, 36.99, 4.99, 7.99, 7.99, 10.99]
    

comic_obj = Comics()
comic_obj.ID1159("C001")
comic_obj.Serie1159("Spiderman")
comic_obj.genero1159 = "Acción"
comic_obj.cven1159 = 1000
comic_obj.autor1159 = "Stan Lee"
comic_obj.color1159 = "Color"
comic_obj.precio1159 = 10.99
comic_obj.mostrar_datos1159()


print("Lista de series:         ", comic_obj.lista_ID1159())
print("Lista de series:         ", comic_obj.lista_series1159())
print("Lista de géneros:        ", comic_obj.lista_generos1159())
print("Lista de cómics vendidos:", comic_obj.lista_cven1159())
print("Lista de autores:        ", comic_obj.lista_autores1159())
print("Lista de colores:        ", comic_obj.lista_colores1159())
print("Lista de precios:        ", comic_obj.lista_precios1159())
