import random
from typing import List, Optional, Union

# ========== KLASY ==========
class Media:
    def __init__(self, title: str, year: int, genre: str):
        self.title = title
        self.year = year
        self.genre = genre
        self._views = 0
    
    def play(self) -> None:
        self._views += 1
    
    @property
    def views(self) -> int:
        return self._views
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.title}', {self.year})"


class Movie(Media):
    def __init__(self, title: str, year: int, genre: str):
        super().__init__(title, year, genre)
    
    def __str__(self) -> str:
        return f"{self.title} ({self.year})"
    
    def info(self) -> str:
        return f"🎬 Film: {self.title} ({self.year}), Gatunek: {self.genre}, Odtworzenia: {self.views}"


class Series(Media):
    def __init__(self, title: str, year: int, genre: str, episode: int, season: int):
        super().__init__(title, year, genre)
        self.episode = episode
        self.season = season
    
    def __str__(self) -> str:
        return f"{self.title} S{self.season:02d}E{self.episode:02d}"
    
    def info(self) -> str:
        return f"📺 Serial: {self.title} (S{self.season:02d}E{self.episode:02d}), Gatunek: {self.genre}, Odtworzenia: {self.views}"


# ========== BIBLIOTEKA ==========
class MediaLibrary:
    def __init__(self):
        self._library: List[Union[Movie, Series]] = []
    
    def add_movie(self, title: str, year: int, genre: str) -> Movie:
        movie = Movie(title, year, genre)
        self._library.append(movie)
        return movie
    
    def add_series(self, title: str, year: int, genre: str, episode: int, season: int) -> Series:
        series = Series(title, year, genre, episode, season)
        self._library.append(series)
        return series
    
    def get_movies(self) -> List[Movie]:
        movies = [item for item in self._library if isinstance(item, Movie)]
        return sorted(movies, key=lambda x: x.title)
    
    def get_series(self) -> List[Series]:
        series = [item for item in self._library if isinstance(item, Series)]
        return sorted(series, key=lambda x: x.title)
    
    def search(self, title: str) -> List[Union[Movie, Series]]:
        return [item for item in self._library if title.lower() in item.title.lower()]
    
    def generate_views(self) -> None:
        if not self._library:
            print("Biblioteka jest pusta!")
            return
        
        random_item = random.choice(self._library)
        random_views = random.randint(1, 100)
        
        for _ in range(random_views):
            random_item.play()
        
        print(f"📈 Dodano {random_views} odtworzeń dla: {random_item}")
    
    def run_generate_views(self, times: int = 10) -> None:
        print(f"🔁 Uruchamiam symulację {times} razy...")
        for i in range(times):
            print(f"  [{i+1}/{times}]", end=" ")
            self.generate_views()
    
    def top_titles(self, n: int = 3, content_type: Optional[str] = None) -> List[Union[Movie, Series]]:
        if content_type == 'movie':
            items = self.get_movies()
        elif content_type == 'series':
            items = self.get_series()
        else:
            items = self._library
        
        sorted_items = sorted(items, key=lambda x: x.views, reverse=True)
        return sorted_items[:n]
    
    def display_library(self) -> None:
        print("\n" + "="*60)
        print("📚 BIBLIOTEKA FILMÓW I SERIALI")
        print("="*60)
        
        if not self._library:
            print("Biblioteka jest pusta!")
            return
        
        movies = self.get_movies()
        series = self.get_series()
        
        print(f"\n🎬 FILMY ({len(movies)}):")
        print("-"*40)
        for movie in movies:
            print(f"  {movie.info()}")
        
        print(f"\n📺 SERIALE ({len(series)}):")
        print("-"*40)
        for series_item in series:
            print(f"  {series_item.info()}")
    
    def display_top_titles(self, n: int = 5) -> None:
        print(f"\n🏆 TOP {n} NAJPOPULARNIEJSZYCH TYTUŁÓW:")
        print("-"*40)
        
        print("\n🔥 Wszystkie tytuły:")
        top_all = self.top_titles(n)
        for i, item in enumerate(top_all, 1):
            print(f"  {i}. {item} - {item.views} odtworzeń")
        
        print(f"\n🎬 Top {n} filmów:")
        top_movies = self.top_titles(n, content_type='movie')
        for i, movie in enumerate(top_movies, 1):
            print(f"  {i}. {movie} - {movie.views} odtworzeń")
        
        print(f"\n📺 Top {n} seriali:")
        top_series = self.top_titles(n, content_type='series')
        for i, series_item in enumerate(top_series, 1):
            print(f"  {i}. {series_item} - {series_item.views} odtworzeń")


# ========== PRZYKŁADOWE DANE ==========
def create_sample_library() -> MediaLibrary:
    """Tworzy przykładową bibliotekę z danymi testowymi"""
    library = MediaLibrary()
    
    # Filmy
    library.add_movie("Pulp Fiction", 1994, "Kryminał")
    library.add_movie("Incepcja", 2010, "Sci-Fi")
    library.add_movie("Forrest Gump", 1994, "Dramat")
    library.add_movie("Matrix", 1999, "Sci-Fi")
    library.add_movie("Skazani na Shawshank", 1994, "Dramat")
    library.add_movie("Gladiator", 2000, "Historyczny")
    library.add_movie("Mroczny Rycerz", 2008, "Akcja")
    
    # Seriale (dodajemy po kilka odcinków)
    # The Simpsons
    library.add_series("The Simpsons", 1989, "Komedia", 1, 1)
    library.add_series("The Simpsons", 1989, "Komedia", 2, 1)
    library.add_series("The Simpsons", 1989, "Komedia", 3, 1)
    library.add_series("The Simpsons", 1989, "Komedia", 1, 2)
    
    # Breaking Bad
    library.add_series("Breaking Bad", 2008, "Dramat", 1, 1)
    library.add_series("Breaking Bad", 2008, "Dramat", 2, 1)
    library.add_series("Breaking Bad", 2008, "Dramat", 1, 2)
    
    # Gra o Tron
    library.add_series("Gra o Tron", 2011, "Fantasy", 1, 1)
    library.add_series("Gra o Tron", 2011, "Fantasy", 2, 1)
    library.add_series("Gra o Tron", 2011, "Fantasy", 1, 2)
    
    return library


# ========== GŁÓWNY PROGRAM ==========
def main():
    print("="*60)
    print("🎬 SYSTEM BIBLIOTEKI FILMÓW I SERIALI")
    print("="*60)
    
    # 1. Tworzymy przykładową bibliotekę
    library = create_sample_library()
    
    # 2. Wyświetlamy początkowy stan
    library.display_library()
    
    # 3. Demonstrujemy wyszukiwanie
    print("\n🔍 WYSZUKIWANIE:")
    print("-"*40)
    
    search_results = library.search("matrix")
    print("Wyniki wyszukiwania dla 'matrix':")
    for item in search_results:
        print(f"  - {item}")
    
    # 4. Uruchamiamy symulację odtwarzania
    print("\n" + "="*60)
    print("🎯 SYMULACJA ODTWARZANIA")
    print("="*60)
    
    library.run_generate_views(5)  # Mniej razy dla szybszego testu
    
    # 5. Wyświetlamy rankingi
    library.display_top_titles(3)
    
    # 6. Pokazujemy tylko filmy i tylko seriale
    print("\n" + "="*60)
    print("📋 PODZIAŁ NA FILMY I SERIALE")
    print("="*60)
    
    print("\n🎬 Wszystkie filmy (alfabetycznie):")
    for movie in library.get_movies():
        print(f"  • {movie}")
    
    print("\n📺 Wszystkie seriale (alfabetycznie):")
    for series_item in library.get_series():
        print(f"  • {series_item}")


# ========== URUCHOMIENIE ==========
if __name__ == "__main__":
    main()
    