from file_reader import FileReader
from file_writer import FileWriter
from journal import *
import random
from Main_Menu_Screen import display_main_menu_screen
import mood_screen
from Analyze_Screen import display_analyze_screen
from Mental_Health_Screen import display_mental_screen
from Quit_Screen import display_quit_screen
from Body_Health_Screen import display_body_screen
from Journal_Screen import display_journal_screen

file_reader = FileReader()
file_writer = FileWriter(False)
log_entries = file_reader.read_log()
journal = Journal(log_entries)
if datetime.today().strftime("%x") in journal.get_jentries():
    today_jentry = journal.get_jentry(datetime.today().strftime("%x"))
else:
    today_jentry = Jentry(datetime.now().strftime("%x"),404,404,404,404,404,404,404,404,"")
    journal.add_to_jentries_map(today_jentry)
#track_menstruation = True
trends = []
main_menu_loop = True



def run():
    jentry_done = False
    # if log_entries == "EMPTY":
    #     track_menstruation = welcome_screen()
    while main_menu_loop:
        main_menu_selection = zero_main_menu()
        if main_menu_selection == "analyze":
            analysis_page_selection = five_analysis_screen()
            if analysis_page_selection == "back":
                continue
        elif main_menu_selection == "journal":
            if not jentry_done:
                entry_page_selection = "mind"
                one_mood_screen()
            while not jentry_done:   
                if entry_page_selection == "mind":
                    entry_page_selection = two_social_energy_freetime_screen()
                if entry_page_selection == "body":
                    entry_page_selection = three_exercise_diet_sleep_screen()
                if entry_page_selection == "journal":
                    entry_page_selection = four_journal_screen()
                    if entry_page_selection == "submit":
                        if today_jentry.get_social() + today_jentry.get_energy() + today_jentry.get_freetime() + today_jentry.get_exercise() + today_jentry.get_diet() + today_jentry.get_sleep() < 100:
                            jentry_done = True
                            file_writer.write_to_log(today_jentry.get_log())
                            break 
                if entry_page_selection == "back":
                    break
        elif main_menu_selection == "quit":
            quit_screen_selection = ""
            while quit_screen_selection != "back":
                quit_screen_selection = six_quit_screen()
            


    

# def welcome_screen():
#     #display welcome
#     #ask about menstruation
#     return #true or false

def zero_main_menu():
    quote = random.choice(file_reader.read_quotes())
    show_journal_button = False
    if not today_jentry.get_social() + today_jentry.get_energy() + today_jentry.get_freetime() + today_jentry.get_exercise() + today_jentry.get_diet() + today_jentry.get_sleep() < 100:
        show_journal_button = True
    return display_main_menu_screen(quote, show_journal_button)

def one_mood_screen():
    today_jentry.set_value("Mood", mood_screen.main())    

def two_social_energy_freetime_screen():
    return display_mental_screen(today_jentry)

def three_exercise_diet_sleep_screen():
    return display_body_screen(today_jentry)

def four_journal_screen():
    return display_journal_screen(today_jentry)
    

def five_analysis_screen():
    display_analyze_screen(journal)    

def six_quit_screen():
    trend_message = "You're doing well! Keep up the good work!"
    reminder_or_quote = ""
    if journal.check_low_score("Mood"):
        trends.append("Looks like your mood has been low recently :\(")
        get_downward_trend_message("Social")
        get_downward_trend_message("Energy")
        get_downward_trend_message("Freetime")
        get_downward_trend_message("Exercise")
        get_downward_trend_message("Diet")
        get_downward_trend_message("Sleep")
    if len(trends) > 0:
        trend_message = random.choice(trends)
    if not today_jentry.get_social() + today_jentry.get_energy() + today_jentry.get_freetime() + today_jentry.get_exercise() + today_jentry.get_diet() + today_jentry.get_sleep() < 100:
        reminder_or_quote = "Don't forget to log your journal entry for today!"
    else:
        reminder_or_quote = random.choice(file_reader.read_quotes())
    return display_quit_screen(trend_message, reminder_or_quote)
    

def get_downward_trend_message(value):
    if journal.is_downward_trend(value):
        trends.append("There's been a downward trend in your " + value + " recently.")

run()