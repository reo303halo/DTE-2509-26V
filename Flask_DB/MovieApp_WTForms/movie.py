# Usually in "models" folder

class Movie:
    def __init__(self, id, title, year, country, genre, age_rating, duration, price):
        self.id = id
        self.title = title
        self.year = year
        self.country = country
        self.genre = genre
        self.age_rating = age_rating
        self.duration = duration
        
        # Replace database entries with missing values with something useful for the user:
        if price == None:
            self.price = "Unavailable"
        else:
            self.price = price
        # Unavailable in plain English is more udnerstandable for most than "Null" or "None"