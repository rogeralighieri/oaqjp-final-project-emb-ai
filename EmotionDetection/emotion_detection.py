import requests

def emotion_detector(text_to_analyse):
    """
    Analyze the input text and return emotion scores along with
    the dominant emotion.
    """

    url = ("https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict")
    headers = {"grpc-metadata-mm-model-id":"emotion_aggregated-workflow_lang_en_stock"}
    payload = {"raw_document": {"text": text_to_analyse}}

    # Diccionario estándar para errores
    error_response = {
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': None
    }

    try:
        response = requests.post(url, json=payload, headers=headers)

        # Manejo explícito de entrada en blanco
        if response.status_code == 400:
            return error_response
        if response.status_code != 200:
            return error_response

        formatted_response = response.json()
        emotion_scores = (formatted_response['emotionPredictions'][0]['emotion'])

        emotions = {
            'anger': emotion_scores.get('anger', 0.0),
            'disgust': emotion_scores.get('disgust', 0.0),
            'fear': emotion_scores.get('fear', 0.0),
            'joy': emotion_scores.get('joy', 0.0),
            'sadness': emotion_scores.get('sadness', 0.0)
        }

        emotions['dominant_emotion'] = max(emotions, key=emotions.get)

        return emotions

    except (requests.RequestException, KeyError, ValueError):
        return error_response
