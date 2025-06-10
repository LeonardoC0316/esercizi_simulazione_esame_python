class Movie:
    def __init__(self, movie_id:str, title:str,director:str):
        self.movie_id:str = movie_id
        self.title:str = title
        self.director:str = director
        self.is_rented:bool = False

    def rent(self) -> None:
        if self.is_rented is False:
            self.is_rented = True
        else:
            return f"Sorry the film '{self.title}'has beeen already rented"

    def return_movie(self) -> None:
        if self.is_rented is True:
            self.is_rented = False
        else:
            return "The film '{self.title}' has not been rented by this client."
    
class Customer:
    def __init__(self, customer_id:str,name:str,rented_movies:list[Movie]):
        self.customer_id = customer_id
        self.name = name
        self.rented_movies:list[Movie] = []

    def rent_movie(self,movie: Movie) -> None:
        """
        controlla se nella lista "rented_movie" è presente il titolo e se 
        non è presente lo aggiunge
        """
        if movie.is_rented:
            print("The film has already been rented")
            
        else:
            movie.rent()
            self.rented_movies.append(movie)
    
    def return_movie(self, movie: Movie):
        if movie in self.rented_movies:
            movie.return_movie()
            self.rented_movies.remove(movie)
        else:
            return f"The movie '{self.title}' has not been rented by this client"     

class VideoRentalStore:
    def __init__(self,customers:dict [str, Customer] = None, movies:dict[str, Movie]= None):
        self.movie:dict[str, Movie] = customers if customers is not None else {}
        self.customers:dict[str, Customer] = movies if movies is not None else {}
    

    def add_movie(self, movie_id: str, title: str, director: str):
        if movie_id not in self.movie:
            self.movie[movie_id]=Movie(movie_id,title,director)
        else:
            return f"The film with this id '{movie_id}' is not found"
        
    def register_customer(self, customer_id:str, name:str) -> None:
        if customer_id in self.customers:
            print("The client has already been registred")

        else:
            customer:Customer = Customer(customer_id, name)
            self.customers[customer_id] = customer

    def rent_movie(self, customer_id:str, movie_id:str) -> None:
        if customer_id not in self.customers or movie_id not in self.movies:
            print("Client or film not in the sistem!")

        else:
            movie:Movie = self.movie[movie_id]
            self.customer[customer_id].rent_movie(movie)

    def get_rented_movies(self, customer_id:str) -> list[Movie]:
        if customer_id not in self.customers:
            print("The client is not in the sistem")
            return []

        else:
            return self.customers[customer_id].rented_movies






        
               
    

