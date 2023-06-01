import json

APP_PATH = '/usr/share/nginx/html/data/'

# REST_ENDPOINT_QUESTION = 'https://nrtest.masterliveaboards.com/questions/'
# REST_ENDPOINT_GUEST = 'https://nrtest.masterliveaboards.com/guests/'
# REST_ENDPOINT_ANSWER = 'https://nrtest.masterliveaboards.com/answers/'


def syncJSON(link, destination):
    with open(link) as json_file:
        data = json.load(json_file)
        jstr = json.dumps(data, indent=4)

    with open(destination, "w") as outfile:
        outfile.write(jstr)

def syncSurvey(jsonPath):
        with open(jsonPath + "guests.json") as json_file:
            guests = json.load(jsonPath + "guests.json")

            for guest in guests:
                with open(APP_PATH + guest.id + ".json") as survey_file:
                    surveyData = json.load(survey_file)
                    # response = requests.post(destination, json=surveyData)

                    with open(APP_PATH + guest.id + ".json", "w") as survesy_file_write:
                        surveyData['is_completed'] = 'YES'
                        survesy_file_write.dump(surveyData, jsonPath + guest.id + ".json")

                    # if response.status_code == '200':
