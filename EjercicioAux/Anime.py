class Anime:
    def __init__(self, nombre: str, genero: str, nroEpisodios: int):
        self.nombre = nombre
        self.genero = genero
        self._nroEpisodios = nroEpisodios
        self._episodios = [] 

    def __str__(self):
        return f"Nombre: {self.nombre}, Género: {self.genero}, Total Episodios: {self._nroEpisodios}"

if __name__ == "__main__":
    mi_anime = Anime("Naruto", "Shonen", 220)
    print(mi_anime)
    mi_anime = Anime("Kimetsu no Yaiba", " cazador", 520)
    print(mi_anime)
