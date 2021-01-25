from mycroft import MycroftSkill, intent_handler
from google_calendar import getEventData
from OpenWeather_api_client import weatherClient


class GoogleCalendarReaderSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_handler('reader.calendar.google.intent')
    def handle_reader_calendar_google(self, message):

        self.speak_dialog('meeting', data=self.getEventData())

    def stop(self):
        pass


def create_skill():
    return GoogleCalendarReaderSkill()


if __name__ == '__main__':
    create_skill()
