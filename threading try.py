import cv2
import threading

# Function for object recognition
def object_recognition():
    # Load pre-trained object detection model
    net = cv2.dnn.readNet('yolov3.weights', 'yolov3.cfg')
    classes = []
    with open('coco.names', 'r') as f:
        classes = f.read().strip().split('\n')

    # Open the camera
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Object detection
        blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
        net.setInput(blob)
        outs = net.forward()

        # Process the detection results
        for out in outs:
            for detection in out:
                    #Process detection data and draw bounding boxes
                  # ...

        # Display the frame
        cv2.imshow('Object Detection', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Simultaneously run another function
def other_function():
    while True:
        print("Running other function...")
        # Your code for the other function
        # ...

# Create threads for both functions
object_recognition_thread = threading.Thread(target=object_recognition)
other_function_thread = threading.Thread(target=other_function)

# Start both threads
object_recognition_thread.start()
other_function_thread.start()

# Wait for both threads to finish
object_recognition_thread.join()
other_function_thread.join()
