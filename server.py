"""
Executing this file initiates the application of emotion detection to be 
executed over the Flask channel and deployed on localhost:5000.
"""
from flask import Flask,request,render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route('/emotionDetector')
def send_detector():
    """
        This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detection()
        function. The output returned shows the overall emotions and its 
        score and dominant emotion based on scores for the provided text.
    """
    text_to_detect = request.args.get('textToAnalyze')
    if text_to_detect is None or text_to_detect == "":
        return "Invalid text! Please try again!."
    response = emotion_detector(text_to_detect)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!."
    return (f"For the given statement, the system response is 'anger': "
        f"{response['anger']}, 'disgust': {response['disgust']}, 'fear': "
        f"{response['fear']}, 'joy': {response['joy']} and 'sadness': "
        f"{response['sadness']}. The dominant emotion is "
        f"{response['dominant_emotion']}.")    

@app.route('/')
def render_index_page():
    ''' 
    This function initiates the rendering of the main application
    page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)
