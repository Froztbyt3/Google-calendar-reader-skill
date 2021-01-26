from mycroft import MycroftSkill, intent_handler
from mycroft_bus_client import MessageBusClient, Message
from adapt.intent import IntentBuilder
from google_calendar import getEventData
from OpenWeather_api_client import weatherClient

client = MessageBusClient()
client.run_in_thread()


class GoogleCalendarReaderSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_handler(IntentBuilder('reader.calendar.google.intent')
                    .require('Calendar')
                    .require('What')
                    .require('My')
                    .require('Is'))
    def handle_reader_calendar_google(self, message):

        # self.speak_dialog('meeting', data=self.getEventData())
        client.emit(
            Message('speak', data=getEventData()))

    def stop(self):
        pass


def create_skill():
    return GoogleCalendarReaderSkill()


# if __name__ == '__main__':
#     create_skill()
