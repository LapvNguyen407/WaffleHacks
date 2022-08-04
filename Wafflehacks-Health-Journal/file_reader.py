from genericpath import exists
from pathlib import Path

class FileReader:

    def __init__(self):
        pass

    __track_menstruation = False

    def read_log(self):
        __p = Path(__file__)
        __filepath = str(__p.parent.absolute()) + "\jentry_log.txt"
        if not exists(__filepath):
            return "EMPTY"
        file = open(__filepath, "r")
        menstruation_line = file.readline()
        if not menstruation_line:
            return "EMPTY"
        self.__track_menstruation = menstruation_line.split("|")[0] == 'True'
        # file.readline()
        jentries = []
        log_entry = file.readline()
        while log_entry:
            jentries.append(log_entry.split("|"))
            log_entry = file.readline()
        file.close()
        return jentries

    def track_menstruation(self):
        return self.track_menstruation


    def read_quotes(self):
        __p = Path(__file__)
        __filepath = str(__p.parent.absolute()) + "\Daily_Quotes.txt"
        if not exists(__filepath):
            return ['“It is only when we take chances, when our lives improve. The initial and the most difficult risk that we need to take is to become honest. —Walter Anderson','“Develop success from failures. Discouragement and failure are two of the surest stepping stones to success.” —Dale Carnegie']
        file = open(__filepath, "r", encoding="utf8")
        quotes = []
        quote_line = file.readline()
        while quote_line:
            quotes.append(quote_line)
            file.readline()
            quote_line = file.readline()
        file.close()
        return quotes

# f = FileReader()
# f.read_log()