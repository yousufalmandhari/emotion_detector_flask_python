import requests
import json
def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, json = myobj, headers=header)
    formatted_response = json.loads(response.text)

    if response.status_code == 200:
        emotion_predictor = formatted_response['emotionPredictions'][0]['emotion']
    
    elif response.status_code == 400:
        emotion_predictor = None

    return emotion_predictor



# from emotion_detection import emotion_detector
# emotion_detector("I am so happy I am doing this.")