import requests

def emotion_detector(text_to_analyse):
    # URL y headers de la API de emociones
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Payload con el texto a analizar
    payload = { "raw_document": { "text": text_to_analyse } }

    try:
        # Realiza la solicitud POST a la API
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()  # Lanza error si el código HTTP no es 2xx

        # Parsear la respuesta JSON
        formatted_response = response.json()

        # Extraer las emociones del primer prediction
        emotion_scores = formatted_response['emotionPredictions'][0]['emotion']

        emotions = {
            'anger': emotion_scores.get('anger', 0.0),
            'disgust': emotion_scores.get('disgust', 0.0),
            'fear': emotion_scores.get('fear', 0.0),
            'joy': emotion_scores.get('joy', 0.0),
            'sadness': emotion_scores.get('sadness', 0.0)
        }

        # Determinar la emoción dominante
        dominant_emotion = max(emotions, key=emotions.get)
        emotions['dominant_emotion'] = dominant_emotion

    except (requests.RequestException, KeyError, ValueError):
        # En caso de error, devuelve None para todos los campos
        emotions = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    return emotions

# print(emotion_detector("I am glad this happened"))    
# print(emotion_detector("I am really mad about this"))    
# print(emotion_detector("I feel disgusted just hearing about this"))    
# print(emotion_detector("I am so sad about this"))    
# print(emotion_detector("I am really afraid that this will happen"))    