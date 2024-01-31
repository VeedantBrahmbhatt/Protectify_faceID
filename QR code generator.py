# import qrcode

# names = ["kunj", "vedant", "nikunj", "devarsh"]
# count=1
# with open("names.txt","w+") as file:
#     for i in names:
#         if count==len(names):
#             file.write(i)

#         else:
#            count=count+1
#            file.write(i+",")
#            print(count)



#     names = file.read().split(",")

# for name in names:
#     qr = qrcode.QRCode(
#         version=5,
#         box_size=10,
#         border=4
#     )
    
#     qr.add_data(name)
#     qr.make(fit=True)
    
#     qr_image = qr.make_image(fill_color="black", back_color="blue")
#     qr_image.save(f"{name}.png")

#     print(f"QR code generated for {name}")


#APScheduler and Celery
import qrcode
import os
import cv2 as cv
from pyzbar.pyzbar import decode
import signal
import time
names = ["kunj", "vedant", "nikunj", "devarsh"]
# def timeout_handler(signum, frame):
#     raise TimeoutError("Function execution timed out")
# timeout_duration=5
# signal.signal(signal.SIGALRM, timeout_handler)
# signal.alarm(timeout_duration)
Flag=False
def user_check():
    cam=cv.VideoCapture(0)
    while True:
        success,img= cam.read()
        for i in names:
            #image = cv.imread(filename=f"{name}.png")
            if img is not None:
                decoded_objects = decode(img)
                print(decoded_objects)
            if decoded_objects:
                for obj in decoded_objects:
                    qr_data = obj.data.decode('utf-8')
                    # print(qr_data)
                    if qr_data in names:
                        # global Flag
                        # Flag=True
                        # while Flag==True:
                            #run two threads onr for checking user another for admin add function
                            
                        x=adding_user()
                        # names.append(x)
                        print(f"user added {x}")
                        qr = qrcode.QRCode(
                            version=5,  # size of the QRCode
                            box_size=10,  # box size of the QRCode
                            border=4  # denotes the width of border of the QRCode
                        )

                        qr.add_data(x)  # add data to the QRCode using qr object
                        qr.make(fit=True)

                        qr_image = qr.make_image(fill_color="red", back_color="yellow")  # set colours
                        qr_image.save(
                            f"/Users/veedantbrahmbhatt/Pycharm/py/QrCodes Section/qr_images/{x}.png")  # save QRCode image

                        print(f"QR code generated for {x}")
                        if cv.waitKey(1) & 0xFF == ord('q'):
                            break  # Press 'q' key to exit the loop
                        cam.release()
                        cv.destroyAllWindows()
                        print("Functioing")
                        adder()
                        break

                        # print("\n access granted \n")

                    else:
                        print("access denied")
                        cam.release()
                        cv.destroyAllWindows()
                        exit()

                break
            break


# def permission_checker():
#     try:
#         file_path='/Users/veedantbrahmbhatt/Pycharm/py/QrCodes Section/names.txt'
#         # Get the current permissions
#         file_stats = os.stat('/Users/veedantbrahmbhatt/Pycharm/py/QrCodes Section/names.txt')
#         current_permissions = file_stats.st_mode
#
#         # Define permission flags
#         write_permission = 0o200  # Write permission value (octal)
#
#         # Add the write permission to the current permissions
#
#         new_permissions = current_permissions | write_permission
#
#         # Apply the new permissions
#         os.chmod(file_path, new_permissions)
#
#         print(f"Write access granted to {new_user} for {file_path}")
#     except Exception as e:
#         print(f"An error occurred: {e}")


def adding_user():
    x=input("enter the name :")
    names.append(x)
    file_creation()
    return x
def file_creation():
    count = 1 
    
    # Open the "names.txt" file for writing and reading ('w+' mode).
    with open("names.txt", "w+") as file:
        # Iterate through each name in the 'names' list.
        for i in names:
            # Write the current name to the file.
            file.write(i)
            if count < len(names):
                file.write(",")
            count += 1
        # names_1 = file.read().split(",")
def generator():
    for name in names:
        qr = qrcode.QRCode(
            version=5, # size of the QRCode
            box_size=10, # box size of the QRCode
            border=4 # denotes the width of border of the QRCode
        )

        qr.add_data(name) # add data to the QRCode using qr object
        qr.make(fit=True)

        qr_image = qr.make_image(fill_color="red", back_color="yellow") # set colours
        qr_image.save(f"/Users/veedantbrahmbhatt/Pycharm/py/QrCodes Section/qr_images/{name}.png") # save QRCode image

        print(f"QR code generated for {name}")

def adder():

    x = input("Add a new User?\n")
    if isinstance(x, str):
        x = x.lower()

    if x == '1' or x == 'yes':
        user_check()
        exit(0)
    elif x == '0' or x == 'no':
        file_creation()
        generator()
        exit(0)
    else:
        print("Invalid Input ")
        exit(0)
    
if __name__=="__main__":

    adder()
    print("Program Continuing....")

