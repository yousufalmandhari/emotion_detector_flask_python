from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        result_1 = emotion_detector('I am glad this happened')
        self.assertEqual(result_1['emotion'][0], 'joy')
        result_2 = emotion_detector('I am really mad about this')
        self.assertEqual(result_2['emotion'][0], 'anger')
        result_3 = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(result_3['emotion'][0], 'disgust')

        result_3 = emotion_detector('I am so sad about this')
        self.assertEqual(result_3['emotion'][0], 'sadness')

        result_3 = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(result_3['emotion'][0], 'fear')

unittest.main()