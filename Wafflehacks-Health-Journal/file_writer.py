from genericpath import exists
from pathlib import Path


class FileWriter:

    track_menstruation = False

    def __init__(self, track_menstruation):
        self.track_menstruation = track_menstruation

    def write_to_log(self,log_entry):
        p = Path(__file__)
        filepath = str(p.parent.absolute()) + "\jentry_log.txt"
        if not exists(filepath):
            file = open(filepath, "x")
            file.close()
            file = open(filepath, "a")
            file.write(str(self.track_menstruation) + "|Tracking Menstruation\n")
            file.close()
        file = open(filepath, "a")
        file.write("\n" + log_entry)
        file.close()
