import os
import datetime as dtime


class DirectoryManager:

    def __init__(self):
        self.str_ts = dtime.datetime.now().replace(microsecond=0).strftime("%Y%m%d_%H%M%S")
        self._DIR_TICKETS = '../data/tickets/'

        self.create_dirs()

    def create_dirs(self):
        dir_tickets = os.path.join(self._DIR_TICKETS, self.str_ts)
        if not os.path.exists(dir_tickets):
            os.makedirs(dir_tickets)

    def get_dir_tickets(self):
        return self._DIR_TICKETS
