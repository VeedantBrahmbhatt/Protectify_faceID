import threading
import subprocess
import time

# Function to run the VolumeHandControl.py process for 10 seconds
def run_volume_hand_control():
    subprocess.run(['python', 'VolumeHandControl.py'])

def run_scanning_user(choice):
    while True:
        if choice == 1:
            valid = 0
            result = subprocess.run(['python', 'FunctionQr.py'], stdout=subprocess.PIPE, text=True)
            print(result.stdout)
            print(result)
            if result.stdout.strip() == '1':
                valid = 1
            else:
                pass
            if valid == 1:
                # Start a thread to run VolumeHandControl.py for 10 seconds
                volume_thread = threading.Thread(target=run_volume_hand_control)
                volume_thread.start()
                # Wait for 10 seconds
                time.sleep(20)
                run_scanning_user(1)
                # Stop the VolumeHandControl thread
                # volume_thread._wait()
            else:
                print('Access Denied')
                target_process_name = 'Code'
                try:
                    subprocess.check_call(["pkill", target_process_name])
                    print(f"Terminated {target_process_name}")
                except subprocess.CalledProcessError:
                    print(f"Failed to terminate {target_process_name}")
                # print(valid)
                # print("Exit code done")
                exit()
        elif choice==2:
            validface = 0
            result = subprocess.run(['python', 'captured_to_predict.py'], stdout=subprocess.PIPE, text=True)
            # print(result.stdout.strip())
            result1,result2=result.stdout.strip().split('step')
            # print(result2)
            # print(result.stdout)
            if result2.strip() == '1':
                validface = 1
                print("Access Granted")
                # exit()
            else:
                pass
            if validface == 1:
                # Start a thread to run VolumeHandControl.py for 10 seconds
                volume_thread = threading.Thread(target=run_volume_hand_control)
                volume_thread.start()
                # Wait for 10 seconds
                time.sleep(20)
                # Stop the VolumeHandControl thread
                run_scanning_user(2)
                # subprocess.run(['python', 'captured_to_predict.py'], stdout=subprocess.PIPE, text=True)
                # volume_thread._stop()
            else:
                print('Access Denied')
                target_process_name = 'PyCharm'
                try:
                    subprocess.check_call(["pkill", target_process_name])
                    print(f"Terminated {target_process_name}")
                except subprocess.CalledProcessError:
                    print(f"Failed to terminate {target_process_name}")
                # print(validface)
                # print("Exit code done")
                exit()
        else:
            exit()
        time.sleep(5)

def main():
    choice = int(input("Enter 1 for QR_Code and 2 for FaceID: "))
    run_scanning_user(choice)

if __name__ == '__main__':
    main()
