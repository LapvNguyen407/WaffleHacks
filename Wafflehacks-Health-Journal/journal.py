from file_reader import FileReader
from jentry import Jentry
from datetime import datetime, timedelta

class Journal:
    #Variables
    jentries = {}

    #Constructor
    def __init__(self, jentry_list):
        for current_jentry in jentry_list:
            date = current_jentry[0]
            mood = current_jentry[1]
            social = current_jentry[2]
            energy = current_jentry[3]
            freetime = current_jentry[4]
            exercise = current_jentry[5]
            diet = current_jentry[6]
            sleep = current_jentry[7]
            menstruation = current_jentry[8]
            journal = current_jentry[9]

            jentry = Jentry(date, mood, social, energy, freetime, exercise, diet, sleep, menstruation, journal)

            self.jentries.update({str(jentry.get_date()) : jentry})
    
    #Getters
    def get_is_menstruating(self):
        if (FileReader.track_menstruation):
            return True
        return False

    def get_jentries(self):
        return self.jentries

    def get_jentry(self,key):
        if key in self.jentries.keys():
            return self.jentries[key]
        else:
            return 0

    def has_jentry(self, key):
        if key in self.jentries.keys():
            return True
        else:
            return False
    
    #Setters
    
    #Methods
    def __generate_score(self, value_to_check):
        
        today = (datetime.today() - timedelta(days= 1)).strftime("%x")
        yesterday = (datetime.today() - timedelta(days= 2)).strftime("%x")
        two_day_ago = (datetime.today() - timedelta(days= 3)).strftime("%x")

        day_one_score = int(self.jentries[today].get_value(value_to_check))
        day_two_score = int(self.jentries[yesterday].get_value(value_to_check))
        day_three_score = int(self.jentries[two_day_ago].get_value(value_to_check))
        
        return (day_one_score, day_two_score, day_three_score)
        
    def is_downward_trend(self, value_to_check):
        day_one, day_two, day_three = self.__generate_score(value_to_check)
        if(day_three <=6):
            return (day_one < day_two and day_two < day_three)

    def check_low_score(self, value_to_check):
        day_one, day_two, day_three = self.__generate_score(value_to_check)

        if (value_to_check == "Mood"):
            return (day_two + day_one + day_three) <= 12
        else:
            return (day_two + day_one + day_three) <= 3

    def downward_spiral(self, value_to_check): #for the memems
        return self.is_downward_trend(value_to_check) and self.check_lowscore(value_to_check)

    def get_weekly_avg(self, value_to_check):
        weekly_sum = 0

        for i in range(7):
            current_day = (datetime.today() - timedelta(days=i)).strftime("%x") 
            weekly_sum += self.jentries[current_day].get_value(value_to_check)

        return weekly_sum/7
    
    def get_monthly_avg(self, value_to_check):
        monthly_sum = 0

        for i in range(30):
            current_day = datetime.now().strftime("%x") - timedelta(days=i)
            monthly_sum += self.jentries[current_day].get_value(value_to_check)

        return monthly_sum/30

    def get_sum(self, jentry):
        return jentry.get_social() + jentry.get_energy() + jentry.get_freetime() + jentry.get_exercise() + jentry.get_diet() + jentry.get_sleep()
    
    def add_to_jentries_map(self, jentry):
       self.jentries.update({jentry.get_date() : jentry})