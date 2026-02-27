from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase): 
    
    def test_emotion_detector(self):
        # Lista de frases y la emoción esperada
        test_cases = [
            ("I am glad this happened", "joy"),
            ("I am really mad about this", "anger"),
            ("I feel disgusted just hearing about this", "disgust"),
            ("I am so sad about this", "sadness"),
            ("I am really afraid that this will happen", "fear")
        ]

        for i, (text, expected_emotion) in enumerate(test_cases, start=1):
            result = emotion_detector(text)

            # Validar que la dominant_emotion coincida con la emoción esperada
            self.assertEqual(
                result['dominant_emotion'],
                expected_emotion,
                msg=f"Test case {i} falló: '{text}' → se esperaba '{expected_emotion}' pero se obtuvo '{result['dominant_emotion']}'"
            )

            # Validar que el score de la emoción dominante sea mayor que 0
            self.assertGreater(
                result[expected_emotion],
                0.0,
                msg=f"Test case {i} falló: el score de '{expected_emotion}' debe ser > 0"
            )

if __name__ == '__main__':
    unittest.main()
