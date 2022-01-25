import cv2

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
