from mycroft import MycroftSkill, intent_file_handler


class GoogleCalendarReader(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('reader.calendar.google.intent')
    def handle_reader_calendar_google(self, message):
        self.speak_dialog('reader.calendar.google')


def create_skill():
    return GoogleCalendarReader()
