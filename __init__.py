from mycroft.skills.core import MycroftSkill, intent_handler, intent_file_handler
from mycroft_bus_client import MessageBusClient, Message
from adapt.intent import IntentBuilder
from google_calendar import getEventData
from OpenWeather_api_client import weatherClient

client = MessageBusClient()
client.run_in_thread()
eventDataDict = getEventData()


class GoogleCalendarReaderSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        # super(GoogleCalendarReaderSkill, self).__init__(
        #     name='GoogleCalendarReaderSkill')

    @intent_file_handler("hello.intent")
    def handle_reader_calendar_google(self, message):

        self.speak_dialog("hello", data=eventDataDict)
        # client.emit(
        #     Message('speak', data=eventDataDict))

    # def stop(self):
    #     pass


def create_skill():
    return GoogleCalendarReaderSkill()


# if __name__ == '__main__':
#     create_skill()
