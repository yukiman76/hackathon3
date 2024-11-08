import cv2
import numpy as np

# eyes will be able to see the board and return what the colors sequence is

# BGR  not RGB
GREEN = (0,128,0)
RED = (0, 0, 255)
WHITE = (255, 255, 255)

class myEyes:

    def __init__(self, bTesting=False):
        self.bTesting = bTesting

    def find_bars(self):
        # Load image, convert to grayscale, Otsu's threshold
        colors = {}
        if self.bTesting:
            image = cv2.imread('Jeff-Front.JPG')
        else:
            cap = cv2.VideoCapture(0)
            if not cap.isOpened():
                print("Cannot open camera")
                exit()
            else:
                ret, image = cap.read()
                # if frame is read correctly ret is True
                if not ret:
                    print("Can't receive frame (stream end?). Exiting ...")
                    exit()

        result = image.copy()
        gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

        # Detect horizontal lines
        horizontal_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (40,1))
        detect_horizontal = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, horizontal_kernel, iterations=2)
        cnts = cv2.findContours(detect_horizontal, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if len(cnts) == 2 else cnts[1]
        i = 1
        for c in cnts:
            # print(c)
            cv2.drawContours(result, [c], -1, (36,255,12), 2)
            # with in the contour need to find the color and distance
            # compute the center of the contour
            M = cv2.moments(c)
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            # draw the contour and center of the shape on the image
            cv2.drawContours(result, [c], -1, (0, 255, 0), 2)
            cv2.circle(result, (cX, cY), 7, (255, 255, 255), -1)
            img_circle = image.copy()
            mask = np.zeros_like(gray)
            cv2.circle(img_circle, (cX, cY), 7, (0, 0, 255), 2)
            cv2.circle(mask, (cX, cY), 7, 255, -1)
            # now we grab the avrage color in the contour
            scolor = ""
            ave_color = cv2.mean(image, mask=mask)[:3]
            print(ave_color)
            if ave_color[0] > 140:
                print("Blue {}".format(i))
                scolor ="B"
            if ave_color[1] > 140:
                print("Green {}".format(i))
                scolor ="G"
            if ave_color[2] > 140:
                print("Red {}".format(i))
                scolor ="R"

            if scolor != "":
                colors[scolor] = i - 1
            cv2.putText(result, "center {} {}".format(scolor, i), (cX - 20, cY - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)

            i += 1

        if self.bTesting:
            cv2.imshow('result', result)
            cv2.waitKey()

        return colors

if __name__ == '__main__':
    print("testing")
    e = myEyes(True)
    print(e.find_bars())
