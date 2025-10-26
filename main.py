


from deepface import DeepFace
import cv2
import time
import sys


def initialize_camera(camera_index=0):
    """
    Initializes the webcam for capturing video.
    """
    cap = cv2.VideoCapture(camera_index)
    if not cap.isOpened():
        print("❌ Error: Cannot access webcam. Please check permissions.")
        sys.exit(1)
    print("✅ Webcam initialized successfully!")
    print("Press 'q' to quit the program.\n")
    return cap


def analyze_frame(frame):
    """
    Analyzes the frame to detect emotions using DeepFace.
    Returns the dominant emotion or None if not detected.
    """
    try:
        result = DeepFace.analyze(
            frame,
            actions=['emotion'],
            enforce_detection=False
        )
        if isinstance(result, list) and len(result) > 0:
            return result[0].get('dominant_emotion', None)
        return None
    except Exception as error:
        print(f"⚠️ Emotion detection error: {error}")
        return None


def display_emotion(frame, emotion):
    """
    Draws the detected emotion text on the video frame.
    """
    text = f"Emotion: {emotion if emotion else 'N/A'}"
    cv2.putText(
        frame,
        text,
        (50, 60),
        cv2.FONT_HERSHEY_SIMPLEX,
        1.2,
        (0, 255, 0),
        2,
        cv2.LINE_AA
    )
    return frame


def main():
    """
    Main function for running the video mood detection system.
    """
    cap = initialize_camera()

   

    while True:
        ret, frame = cap.read()
        if not ret:
            print("❌ Failed to capture frame from camera.")
            break

        

        dominant_emotion = analyze_frame(frame)

       

        frame = display_emotion(frame, dominant_emotion)

       

        cv2.imshow("🧠 Video Mood & Stress Detector", frame)

       

        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("\n👋 Exiting the program gracefully...")
            break

       

        time.sleep(0.05)


    cap.release()
    cv2.destroyAllWindows()
    print("✅ Resources released. Program terminated successfully.")


if __name__ == "__main__":
    main()


