import cv2
import imutils
from pyzbar import pyzbar
import numpy as np


class FrameEditor(object):

    def __init__(self, img, target):
        self.target = target
        self.image = img
        self.imagecopy = img.copy()

    def returnframe(self):
        frame = self.image
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        ddepth = cv2.CV_32F if imutils.is_cv2() else cv2.CV_32F
        gradX = cv2.Sobel(gray, ddepth=ddepth, dx=1, dy=0, ksize=-1)
        gradY = cv2.Sobel(gray, ddepth=ddepth, dx=0, dy=1, ksize=-1)

        # subtract the y-gradient from the x-gradient
        gradient = cv2.subtract(gradX, gradY)
        gradient = cv2.convertScaleAbs(gradient)

        blurred = cv2.blur(gradient, (9, 9))
        (_, thresh) = cv2.threshold(blurred, 225, 255, cv2.THRESH_BINARY)

        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (21, 7))
        closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

        closed = cv2.erode(closed, None, iterations=4)
        closed = cv2.dilate(closed, None, iterations=4)

        cnts = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL,
                                cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if imutils.is_cv2() else cnts[1]

        if cnts:
            c = sorted(cnts, key=cv2.contourArea, reverse=True)[0]

            rect = cv2.minAreaRect(c)
            box = cv2.boxPoints(rect) if imutils.is_cv2() else cv2.boxPoints(rect)
            box = np.int0(box)

            # cv2.drawContours(frame, [box], -1, (0, 255, 0), 3)
            x, y, w, h = cv2.boundingRect(c)
            frame_bars = frame[y:y + h, x: x + w]

            barcodes = pyzbar.decode(frame_bars)
            for i in barcodes:
                if "may-store.ru" in i.data.decode("utf-8"):
                    return True
        return None
