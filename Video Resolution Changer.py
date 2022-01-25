import cv2
import sys

class ResolutionChanger:
    def __init__(self, path, val):
        self.path = path
        self.val = val
        
        self.change_resolution()
    
    def change_resolution(self):
        video = cv2.VideoCapture(self.path)
        
        _, frame = video.read()
        
        video_name = self.path.split('\\')[-1]
        
        mode = ''
        if self.val > 1:
            mode = 'Increasing'
        else:
            mode = 'Decreasing'
        
        print(f"{mode} {video_name} Video Resolution Process Started")
        
        codec = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D') # WMV2, WMV1, MJPG, DIVX, XVID, H264
        framerate = 20
        resolution = (int(frame.shape[1]*self.val), int(frame.shape[0]*self.val))
        
        video_out = cv2.VideoWriter('out.avi', codec, framerate, resolution)
        frame = cv2.resize(frame, resolution)
        video_out.write(frame)
        
        while video.isOpened():
            ret, frame = video.read()
            
            if ret == True:
                frame = cv2.resize(frame, resolution)
                video_out.write(frame)
            else:
                print(f"{mode} {video_name} Video Resolution Process Completed!")
                break
        
        cv2.destroyAllWindows()
        video_out.release()
        video.release()

if __name__ == '__main__':
    path = input('Enter the path and name of the video: (ex: /video/example.mp4) ')
    val = float(input('Enter resolution changing value: (ex: 0.5) '))
    
    if val < 0:
        print('Negative values are not allowed!')
        sys.exit()
    elif val == 1.0:
        print('If changing value is 1, output video resolution will be same!')
        sys.exit()
    else:
        ResolutionChanger(path, val)
