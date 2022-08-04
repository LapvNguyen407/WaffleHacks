import pygame
from datetime import datetime

class Jentry:
    #Variables
    date = 404
    today = 404
    mood = 404
    social = 404
    energy = 404
    freetime = 404
    exercise = 404
    diet = 404
    sleep = 404
    menstruation = False
    journal = 404
    

    #Constructor
    def __init__(self, date, mood, social, energy, freetime, exercise, diet, sleep, menstruation, journal):
        self.date = date
        self.today = datetime.now().strftime("%x") # --> MM/dd/yy
        self.mood = int(mood)
        self.social = int(social)
        self.energy = int(energy)
        self.freetime = int(freetime)
        self.exercise = int(exercise)
        self.diet = int(diet)
        self.sleep = int(sleep)
        self.menstruation = bool(menstruation == "True")
        self.journal = str(journal)

    def __str__(self):
        return str(self.date) + "|" + str(self.mood) + "|" + str(self.social) + "|" + str(self.energy) + "|" + str(self.freetime) + "|" + str(self.energy) + "|" + str(self.diet) + "|" + str(self.sleep) + "|" + str(self.menstruation) + "|" + str(self.journal)
    
    #Getters
    def get_date(self):
        return self.date

    def get_mood(self):
        return self.mood
        
    def get_social(self):
        return self.social

    def get_energy(self):
        return self.energy

    def get_freetime(self):
        return self.freetime

    def get_exercise(self):
        return self.exercise
    
    def get_diet(self):
        return self.diet

    def get_sleep(self):
        return self.sleep
    
    def get_menstruation(self):
        return self.menstruation

    def get_journal(self):
        return self.journal
    
    #Setters
    def set_value(self, value_to_set, new_value):
        if (value_to_set == "Date"):
            self.date = new_value
        elif (value_to_set == "Mood"):
            self.mood = int(new_value)
        elif (value_to_set == "Social"):
            self.social = int(new_value)
        elif (value_to_set == "Energy"):
            self.energy = int(new_value)
        elif (value_to_set == "Freetime"):
            self.freetime = int(new_value)
        elif (value_to_set == "Exercise"):
            self.exercise = int(new_value)
        elif (value_to_set == "Diet"):
            self.diet = int(new_value)
        elif (value_to_set == "Sleep"):
            self.sleep = int(new_value)
        elif (value_to_set == "Menstruation"):
            self.menstruation = new_value
        elif (value_to_set == "Journal"):
            self.journal = new_value

    #Methods
    def get_log(self):
        log = str(self.today) + "|" + str(self.mood) + "|" + str(self.social) + "|" + str(self.energy) + "|" + str(self.freetime) + "|" + str(self.energy) + "|" + str(self.diet) + "|" + str(self.sleep) + "|" + str(self.menstruation) + "|" + str(self.journal)
        return log

    def get_value(self, value_to_get):
        if (value_to_get == "Date"):
            return self.date
        elif (value_to_get == "Mood"):
            return self.mood
        elif (value_to_get == "Social"):
            return self.social
        elif (value_to_get == "Energy"):
            return self.energy
        elif (value_to_get == "Freetime"):
            return self.freetime
        elif (value_to_get == "Exercise"):
            return self.exercise
        elif (value_to_get == "Diet"):
            return self.diet
        elif (value_to_get == "Sleep"):
            return self.sleep
        elif (value_to_get == "Menstruation"):
            return self.menstruation
        elif (value_to_get == "Journal"):
            return self.journal

