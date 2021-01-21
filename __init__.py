# from mycroft import MycroftSkill, intent_file_handler
from google_calendar import getEventData
from OpenWeather_api_client import weatherClient


# class GoogleCalendarReader(MycroftSkill):
#     def __init__(self):
#         MycroftSkill.__init__(self)

#     @intent_file_handler('reader.calendar.google.intent')
#     def handle_reader_calendar_google(self, message):
#         self.speak_dialog('reader.calendar.google')


def create_skill():
    print('Getting data......')
    CalendarData = getEventData()
    weatherData = weatherClient()
    print('Mycroft received:', CalendarData)
    print('Mycroft received:', weatherData)
    # return GoogleCalendarReader()


if __name__ == '__main__':
    create_skill()
