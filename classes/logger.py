import config as cfg

import uuid


class Logger:
    def __init__(self, hms):
        """
        ------------------------------------------------------------------------------------------
        Creating a log file. Entering the first entry

        type(hms) >> tuple | len(hms) >> 3 | type(hws[::]) >> str()
        ------------------------------------------------------------------------------------------
        """

        logname = f"logs/{uuid.uuid4().hex}.txt"
        message = f"{':'.join(hms)}\t-\t{cfg.events['Launch']}"

        with open(logname, mode="w", encoding="utf-8") as log_file:
            log_file.write(message)
        self.logname = logname
    
    def add_message(self, hms, event):
        """
        ------------------------------------------------------------------------------------------
        Entering the giving message

        type(hms) >> tuple | len(hms) >> 3 | type(hws[::]) >> str()
        type(event) >> str
        ------------------------------------------------------------------------------------------
        """

        if event in cfg.events:
            message = f"\n{':'.join(hms)}\t-\t{cfg.events[event]}"
        else:
            message = f"\n{':'.join(hms)}\t-\t{event}"

        with open(self.logname, mode="a", encoding="utf-8") as log_file:
            log_file.write(message)