import cv2 as cv
from pyzbar.pyzbar import decode
def Qr_code():
    camera = cv.VideoCapture(0)
    data = {"ID": [], "Text": []}
    j = 0

    valid = 0
    user = []
    with open("names.txt", "r") as file:
        names = file.read().split(",")
        # print(names)
        user = names
        print(user)
    while True:
        ret, frame = camera.read()

        for i in user:
            # image = cv.imread(filename=f"{user}.png")
            # if frame is not None:
            decoded_objects = decode(frame)
            # print(decoded_objects)
            if decoded_objects:
                for obj in decoded_objects:
                    qr_data = obj.data.decode('utf-8')
                    # print(qr_data)
                    if qr_data in user:
                        print(f"QR code data for {qr_data}: {qr_data}")
                        print("\n access granted \n")
                        valid = 1
                        return valid

                    else:
                        print("access denied")
                        continue
        if cv.waitKey(1) & 0xFF == ord('q'):
            break  # Press 'q' key to exit the loop

    camera.release()
    cv.destroyAllWindows()
    return valid
if __name__=="__main__":
    x=Qr_code()
    print(x)
