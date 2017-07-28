import os
from datetime import date


class Event:

    events = []

    def __init__(self, date):
        '''
        Date object
        '''
        self.date = date

    def get_date(self):
        return self.date
    
    def upload_date(self, date):
        self.date = date

    @classmethod
    def sort_events(cls):
        is_sorted = False
        while not is_sorted and len(cls.events) > 1:
            is_sorted = True
            for item in range(len(cls.events) - 1):
                if cls.events[item].date > cls.events[item + 1].date:
                    temp = cls.events[item]
                    cls.events[item] = cls.events[item + 1]
                    cls.events[item + 1] = temp
                    is_sorted = False

    @classmethod
    def add_event(cls, event):
        cls.events.append(event)
        cls.sort_events()

    @classmethod
    def get_events(cls):
        return cls.events

    @classmethod
    def read_data_from_file(cls):
        file_path = os.getcwd() + '/events.csv'
        if os.path.exists(file_path):
            with open(file_path, 'r') as csvfile:

                splitted_rows = [line.replace('\n', '').strip().split(',') for line in csvfile]

                for item_list in splitted_rows:
                    date_list = item_list[0].split('-')
                    dates = date(int(date_list[0]), int(date_list[1]), int(date_list[2]))
                    if 'PrivateMentoring' in item_list:
                        event = PrivateMentoring(dates)
                    else:
                        event = Checkpoint(dates)

        return cls.events

    @classmethod
    def save_data_to_file(cls):
        file_path = os.getcwd() + '/events.csv'
        with open(file_path, 'w') as csvfile:
            string_to_save = cls.data_to_save()
            csvfile.write(string_to_save)

    @classmethod
    def data_to_save(cls):
        list_to_save = []
        for event in cls.events:
            row = [str(event.date), event.__class__.__name__]
            list_to_save.append(row)

        string_save = '\n'.join(','.join(row) for row in list_to_save)

        return string_save


class Checkpoint(Event):

    events = []

    def __init__(self, date):
        super().__init__(date)
        Event.add_event(self)
        Checkpoint.add_event(self)

    def __str__(self):
        return '{} Checkpoint'.format(self.date)


class PrivateMentoring(Event):

    events = []

    def __init__(self, date):
        super().__init__(date)
        self.preffered_mentor = None
        self.goal = None
        Event.add_event(self)
        self.__class__.add_event(self)

    def set_goal(self, goal):
        self.goal = goal

    def set_preffered_mentor(self, preffered_mentor):
        self.preffered_mentor = preffered_mentor

    def __str__(self):
        return '{} private mentoring with {} about {}'.format(self.date, self.preffered_mentor, self.goal)


    
