from mycroft import MycroftSkill, intent_file_handler


class GoogleCalenderReader(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('reader.calender.google.intent')
    def handle_reader_calender_google(self, message):
        self.speak_dialog('reader.calender.google')


def create_skill():
    return GoogleCalenderReader()

