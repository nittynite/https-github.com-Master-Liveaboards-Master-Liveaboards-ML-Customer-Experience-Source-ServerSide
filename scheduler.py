import os
import datetime
import schedule
import time
import syncJSON

APP_PATH = '/user/share/nginx/html/'

REST_ENDPOINT_QUESTION = 'https://nrtest.masterliveaboards.com/questions/'
REST_ENDPOINT_GUEST = 'https://nrtest.masterliveaboards.com/guests/'
REST_ENDPOINT_ANSWER = 'https://nrtest.masterliveaboards.com/answers/'

def syncFiles():

    # for Questions
    # if os.path.isdir(APP_PATH + "json/questions.json"):
    #     fileTimestamp = os.path.getmtime(APP_PATH + "json/questions.json")
    #     fileDateTime = datetime.datetime.fromtimestamp(fileTimestamp)
    #
    #     if datetime.now() - fileDateTime > 36000:
    #         syncJSON(REST_ENDPOINT_QUESTION, APP_PATH + "json/questions.json")
    #
    # else:
    #     syncJSON(REST_ENDPOINT_QUESTION, APP_PATH + "json/questions.json")


    # for Guests
    if os.path.isdir(APP_PATH + "json/guests.json"):
        fileTimestamp = os.path.getmtime(APP_PATH + "json/guests.json")
        fileDateTime = datetime.datetime.fromtimestamp(fileTimestamp)

        if datetime.now() - fileDateTime > 36000:
            syncJSON(REST_ENDPOINT_QUESTION, APP_PATH + "json/guests.json")

    else:
        syncJSON(REST_ENDPOINT_QUESTION, APP_PATH + "json/guests.json")

    # for Survey Answers
        syncJSON.syncSurvey(os.path.getmtime(APP_PATH))


def job():
    schedule.every(60).minutes.do(syncFiles)

while True:

    schedule.run_pending()
    time.sleep(1)

