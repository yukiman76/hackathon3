import cv2
import numpy as np 

# Open the default camera
cam = cv2.VideoCapture(0)

# Get the default frame width and height
frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))  # Width of the video frame
frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))  # Height of the video frame

# Define the codec and create VideoWriter object
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for the video output
# out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (frame_width, frame_height))  # Create VideoWriter object

while True:
    ret, frame = cam.read()  # Capture a frame from the camera

    # Write the frame to the output file
    # out.write(frame)  # Write the captured frame to the video file (currently commented out)

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert the frame to grayscale to simplify processing
    
    # Blur using 3 * 3 kernel
    gray_blurred = cv2.blur(gray, (3, 3))  # Apply a blur to the grayscale image to reduce noise
    
    # Apply Hough transform on the blurred image to detect circles
    detected_circles = cv2.HoughCircles(gray_blurred,  # Input image
                                        cv2.HOUGH_GRADIENT,  # Detection method
                                        1,  # Inverse ratio of accumulator resolution to image resolution
                                        20,  # Minimum distance between detected circle centers
                                        param1=50,  # Higher threshold for edge detection
                                        param2=30,  # Accumulator threshold for circle detection
                                        minRadius=1,  # Minimum radius of circles to detect
                                        maxRadius=40)  # Maximum radius of circles to detect
    
    # Draw circles that are detected
    if detected_circles is not None:  # Check if any circles were detected
        detected_circles = np.uint16(np.around(detected_circles))  # Round and convert circle parameters to integers
    
        for pt in detected_circles[0, :]:  # Iterate over each detected circle
            a, b, r = pt[0], pt[1], pt[2]  # Center coordinates (a, b) and radius (r) of the circle
    
            # Draw the circumference of the circle on the frame
            cv2.circle(frame, (a, b), r, (0, 255, 0), 2)  # Draw the circle with green color and thickness of 2
    
            # Draw a small circle to show the center of the detected circle
            cv2.circle(frame, (a, b), 1, (0, 0, 255), 3)  # Draw center with red color and thickness of 3

    # Display the captured frame with circles drawn (if any were detected)
    cv2.imshow('Camera', frame)

    # Press 'q' to exit the loop
    if cv2.waitKey(1) == ord('q'):  # Check if 'q' key is pressed to break the loop
        break

# Release the capture and writer objects
cam.release()  # Release the camera
# out.release()  # Release the video writer (currently commented out)
cv2.destroyAllWindows()  # Close all OpenCV windows
