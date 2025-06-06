class Movie:
    def __init__(self, movie_id:str, title:str,director:str,is_rented:bool = False):
        self.movie_id = movie_id
        self.title = title
        self.director = director
        self.is_rented = bool       

    def rent(self):
        if self.is_rented is False:
            self.is_rented = True
        else:
            return f"Sorry the film '{self.title}'has beeen already rented"

    def return_movie(self):
        if self.is_rented is True:
            self.is_rented = False
        else:
            return "The film '{self.title}' has not been rented by this client."
    
class Customer:
    def __init__(self, customer_id:str,name:str,rented_movies:list[Movie]):
        self.customer_id = customer_id
        self.name = name
        self.rented_movies = [Movie]

    def rent_movie(self,movie: Movie):
        """
        controlla se nella lista "rented_movie" è presente il titolo e se 
        non è presente lo aggiunge
        """
        if self.title not in self.rented_movies and self.is_rented is False:
            self.rented_movie.append(self.title)
            Movie.rent()
    
    def return_movie(self):
        if self.title in self.rented_movies:
            self.rented_movies.remove(self.title)
        else:
            return f"The movie '{self.title}' has not been rented by this client"     

class VideoRentalStore:
    def __init__(self):
        self.movie:dict[str, Movie] = {}
        self.customers:dict[str, Customer]  = {}
    

    def add_movie(self, movie_id: str, title: str, director: str):
        if movie_id not in self.movie:
            self.movie[movie_id]=Movie(movie_id,title,director)
        else:
            return f"The film with this id '{movie_id}' is not found"








        
               
    

