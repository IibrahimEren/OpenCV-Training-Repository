import cv2
import numpy as np

vid = cv2.VideoCapture('media/traffic.avi')
backsub = cv2.createBackgroundSubtractorMOG2()
c = 0

while True:
    ret, frame = vid.read()
    if ret:
        fgmask = backsub.apply(frame)
        cv2.imshow("img", fgmask)
        shape = frame.shape[::-1]
        print(shape)
        # cv2.line(frame, (0, 180), (640, 180), (0, 255, 255), 2)
        # cv2.line(frame, (0, 200), (640, 200), (250, 255, 0), 2)
        # other video
        cv2.line(frame, (100, 0), (100, 180), (0, 255, 255), 2)
        cv2.line(frame, (110, 0), (110, 180), (250, 255, 0), 2)

        contours, hierarchy = cv2.findContours(fgmask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        try:
            hierarchy = hierarchy[0]
        except:
            hierarchy = []
        for contours, hier in zip(contours, hierarchy):
            (x, y, w, h) = cv2.boundingRect(contours)
            if 40 < w < 90 and 40 < h < 90:
                cv2.rectangle(frame, (x, y), ((x + w), (y + h)), 255, 3)
                # if 180 < y < 200:
                #     c += 1
                # elif 200 > y >180:
                #     c -= 1
                # other video
                if 100 < x < 110:
                    c += 1
        cv2.putText(frame, f"car: {c}", (90, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2, cv2.LINE_AA)

    else:
        break

    cv2.imshow("img", fgmask)
    cv2.imshow("frame", frame)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
