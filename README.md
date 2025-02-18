Face Recognition Attendance System
This is a Python-based system that utilizes face recognition to automatically mark attendance for individuals using their facial features. The system uses the OpenCV and face_recognition libraries for detecting faces in real-time through a webcam, and it compares the captured face with pre-existing images stored in a directory. Once a match is found, it marks the individual’s attendance along with the time they were recognized.

Modules Used:
cv2 (OpenCV): Used for image processing, capturing real-time video feed, and displaying frames.
face_recognition: A Python library that simplifies the process of detecting faces, encoding facial features, and comparing them.
numpy: For handling numerical data like arrays and matrices.
os: For file handling and accessing the directory containing images.
datetime: For capturing the current time and logging the attendance with timestamps.
How the System Works:
Preprocessing Phase (Setup):

A directory is specified that contains the images of individuals (e.g., staff members or students).
The system reads the images from the directory and extracts their facial encodings using the face_recognition.face_encodings() function.
It stores these encodings and associates each encoding with the name of the individual (extracted from the image file name) into two lists: encodeListKnown and className.
Attendance Marking:

The system captures real-time video from a webcam using cv2.VideoCapture().
For each frame, it detects faces and calculates their encodings.
It compares these encodings with the stored known encodings (from the preprocessed images) using face_recognition.compare_faces().
The closest match (smallest face distance) is identified, and the person's name is displayed on the screen along with the bounding box around their face.
Attendance Logging:

If a face is recognized, the system checks whether the individual’s name is already recorded in an "attendance.csv" file.
If the name is not present, it appends the person's name and the time of recognition to the file in the format: name,time.
This ensures that each person is logged only once during the session.
Real-time Interaction:

The system continuously captures frames, detects faces, and displays the live webcam feed with annotations (bounding boxes and name labels).
The attendance is logged in real-time as the faces are recognized.
Key Functions:
findEncodings(images): This function reads the images, converts them into RGB format (since face_recognition works with RGB), and generates facial encodings for each image.
markAttendance(name): This function checks if the person's name is already present in the "attendance.csv" file and, if not, records the name along with the current timestamp.

Key Features:
Real-time Face Recognition: The system processes the webcam feed in real-time, continuously detecting faces.
Attendance Logging: Once a face is recognized, the system automatically records the person's name and time into a CSV file, ensuring accurate attendance tracking.
Efficient Face Matching: The system uses the face_recognition library’s compare_faces method and face_distance method to identify the best match for faces.
User-Friendly Interface: The real-time webcam feed is displayed with names and bounding boxes around the recognized faces for visual feedback.

Requirements:
Python 3.x
opencv-python for image processing and webcam access.
face_recognition for face detection and recognition.
numpy for numerical operations.

Conclusion:
This Face Recognition Attendance System automates the process of marking attendance using facial recognition technology. It is particularly useful in environments like schools, universities, or workplaces, where manually tracking attendance can be time-consuming and error-prone. By utilizing computer vision and machine learning algorithms, this system provides an efficient and seamless solution for attendance management.
