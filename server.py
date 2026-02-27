''' Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Analyzer")

@app.route("/emotionDetector")
def detect_emotion():
    ''' 
    Recibe el texto desde la interfaz HTML y ejecuta el análisis de emociones
    usando la función emotion_detector(). La salida mostrará todas las emociones
    y la emoción dominante con su score.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    # Verifica que el texto no esté vacío
    if not text_to_analyze:
        return "¡Entrada no válida! Por favor proporciona un texto."

    # Pasa el texto a la función emotion_detector y almacena la respuesta
    response = emotion_detector(text_to_analyze)
    # Si la API falla y devuelve None
    if response['dominant_emotion'] is None:
        return "¡No se pudo analizar el texto! Intenta de nuevo."

    # Construye un mensaje con todas las emociones y la dominante
    emotions_text = ", ".join(
        [
            f"{k}: {v:.3f}"
            for k, v in response.items()
            if k != 'dominant_emotion'
        ]
    )
    dominant_text = f"Emoción dominante: {response['dominant_emotion']}"

    return f"Análisis de emociones:\n{emotions_text}\n{dominant_text}"

@app.route("/")
def render_index_page():
    ''' Renderiza la página principal de la aplicación '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
