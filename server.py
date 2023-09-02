from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    max_emotion = max(response, key=lambda x: response[x])

    emotion_predictor = f"For the given statement, the system response is {', '.join([f'{emotion}: {value}' for emotion, value in response.items()])}. The dominant emotion is {max_emotion}."

    if response is None:
        return "Invalid input ! Try again."
    else:
        return emotion_predictor

    

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5010)