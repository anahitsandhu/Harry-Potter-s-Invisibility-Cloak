import cv2
import numpy as np
import time

def create_background(cap, num_frames=30):
    print("Capturing background. Please move out of frame.")
    backgrounds=[]
    for i in range(num_frames):
        ret, frame= cap.read()
        if ret:
            backgrounds.append(frame)
        else:
            print(f"Warning: Could not read frame {i+1}/{num_frames}")
        time.sleep(0.1)
    if backgrounds:
        return np.median(backgrounds, axis=0).astype(np.uint8)
    else:
        raise ValueError("Could not capture any frames for background")
    
def create_mask(frame, lower_color, upper_color):
    hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask=cv2.inRange(hsv,lower_color, upper_color)
    mask=cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3,3),np.uint8), iterations=2)
    mask=cv2.morphologyEx(mask, cv2.MORPH_DILATE, np.ones((3,3),np.uint8),iterations=1)
    return mask

def apply_cloak_effect(frame, mask, background):
    mask_inv=cv2.bitwise_not(mask)
    fg=cv2.bitwise_and(frame,  frame,mask=mask_inv)
    bg=cv2.bitwise_and(background, background, mask=mask)
    if np.sum(mask_inv) == 0:
        print("no black surface")
        return frame
    return cv2.add(fg,bg)
    
def main():
    print("OpenCv version:",cv2.__version__)

    cap=cv2.VideoCapture(0)
    if not cap.isOpened():
        print("camera not found")
        return
    try:
        background=create_background(cap)
    except ValueError as e:
        print(f"Error: {e}")
        cap.release()
        return
    upper_black=np.array([180,255,30])
    lower_black=np.array([0, 0, 0])

    print("Press q to quit")
    while True:
        ret, frame=cap.read()
        if not ret:
            print("No frame exists")
            time.sleep(1)
            continue
        
        mask= create_mask(frame, lower_black, upper_black)
        result= apply_cloak_effect(frame, mask, background)
        
        cv2.imshow("Invisiblity Cloak",result)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

