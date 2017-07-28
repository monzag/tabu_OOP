from datetime import date
import view
import events


class Controller:

    def start(self):
        events.Event.read_data_from_file()
        while True:
            view.print_main_menu()
            choice = view.get_choice()
            if choice == '1':
                self.book_private_mentoring()
            elif choice == '2':
                self.book_checkpoint()
            elif choice == '3':
                self.print_all_events()
            elif choice == '4':
                self.cancel_event()
            elif choice == '5':
                self.rescheduling_event()
            else:
                self.say_goodbye()

            events.Event.save_data_to_file()

    def print_all_events(self):
        view.print_all_events(events.Event.get_events())

    def book_event(self):
        pass

    def book_checkpoint(self):
        date = view.get_event_date()
        date = self.__class__.convert_date(date)
        events.Checkpoint(date)

    def book_private_mentoring(self):
        date = view.get_event_date()
        date = self.__class__.convert_date(date)
        event = events.PrivateMentoring(date)

        mentor = view.choose_mentor()
        print('here', mentor)
        event.set_preffered_mentor(mentor)

        goal = view.get_goal()
        event.set_goal(goal)

    def cancel_event(self):
        # TODO : anti_idiot
        user_choice = self.choose_event()
        events_list = events.Event.get_events()
        if int(user_choice) in range(len(events_list)+1):
            del(events_list[int(user_choice) - 1])

    def rescheduling_event(self):
        # TODO : anti_idiot
        user_choice = self.choose_event()
        events_list = events.Event.get_events()
        event = events_list[int(user_choice) - 1]
        date = view.get_event_date()
        date = self.__class__.convert_date(date)
        event.upload_date(date)

    def choose_event(self):
        self.print_all_events()
        user_input = view.get_choice()
        return user_input

    def say_goodbye(self):
        view.print_goodbye()
        exit()

    @staticmethod
    def convert_date(date_str):
        date_list = date_str.split('-')
        return date(int(date_list[2]), int(date_list[1]), int(date_list[0]))
