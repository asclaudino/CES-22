class Author:
    def __init__(self, name, surname, birth_date, death_date,publishes):
        self.name = name
        self.surname = surname
        self.birth_date = birth_date
        self.death_date = death_date
        self.publishes = publishes

    def __str__(self):
        return "Name: " + self.name + " \nSurname: " + self.surname + " \nBirth Date: " + self.birth_date + " \nDeath Date: " + self.death_date 
        
    
    def get_publishes(self):
        for publish in self.publishes:
            str(publish)