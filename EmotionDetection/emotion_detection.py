"""
Emotion Detection Module
"""
import json
import requests

def emotion_detector(text_to_analyse):
    """
    emotion detection function
    input : str
    output : Dict
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url,headers=header,json=myobj,timeout=120)
    formatted_response = json.loads(response.text)
    if response.status_code == 200:
        return emotion_predictor(formatted_response)
    elif response.status_code == 500:
        formatted_response = {
                            'anger': None,
                            'disgust': None, 
                            'fear': None, 
                            'joy': None, 
                            'sadness': None, 
                            'dominant_emotion': None}
        return formatted_response

def emotion_predictor(detected_text):
    if detected_text['emotionPredictions'] is not None:
        emotions = detected_text['emotionPredictions'][0]['emotion']
        anger = emotions['anger']
        disgust = emotions['disgust']
        fear = emotions['fear']
        joy = emotions['joy']
        sadness = emotions['sadness']
        dominant_emotion = max(emotions, key=emotions.get)
        formatted_emotions_dict = {
                                'anger': anger,
                                'disgust': disgust,
                                'fear': fear,
                                'joy': joy,
                                'sadness': sadness,
                                'dominant_emotion': dominant_emotion
                                }
        return formatted_emotions_dict
    