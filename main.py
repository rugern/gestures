import cv2

from masks import skinMask, binaryMask

def main():
    font = cv2.FONT_HERSHEY_SIMPLEX
    size = 0.5
    fx = 10
    fy = 355
    fh = 18
    minValue = 70
    x0 = 400
    y0 = 200
    height = 200
    width = 200
    binaryMode = True

    inputStream = cv2.VideoCapture(0)
    success = inputStream.set(3, 640)
    success = inputStream.set(4, 480)

    while True:
        success, frame = inputStream.read()
        frame = cv2.flip(frame, 3)

        if success:
            if binaryMode:
                modified = binaryMask(frame, x0, y0, width, height, minValue)
            else:
                modified = skinMask(frame, x0, y0, width, height)

        cv2.putText(frame,'b: Toggle Binary/SkinMask',(fx,fy + fh), font, size,(0,255,0),1,1)
        cv2.putText(frame,'ESC: Exit',(fx,fy + 6*fh), font, size,(0,255,0),1,1)

        cv2.imshow('Original', frame)
        cv2.imshow('Modified', modified)

        key = cv2.waitKey(10) & 0xff

        # ESC closes program
        if key == 27:
            break
        elif key == ord('b'):
            binaryMode = not binaryMode

    inputStream.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
