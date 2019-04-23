#! /usr/bin/python3
#
# schicam -- a python cv2 webcam viewer with zoom.
#
# 2019-04-15, v0.1      juergen@fabmail.org
#                       implemented warpPerspective with getPerspectiveTransform from 4 points
# 2019-04-23, v0.2      using xdootool to implement the windowsize()
#
"""
Use uvcdynctrl -f
to retrieve possible frame sizes

E.g. Logitech C920 has this

YUYV 4:2:2; MIME type: video/x-raw-yuv
 Frame size: 1024x576 Frame intervals: 1/15, 1/10, 2/15, 1/5
 Frame size: 1280x720 Frame intervals: 1/10, 2/15, 1/5
 Frame size: 1600x896 Frame intervals: 2/15, 1/5
 Frame size: 1920x1080 Frame rates: 5
 Frame size: 2304x1296 Frame rates: 2
 Frame size: 2304x1536 Frame rates: 2

H.264 and MJPG (Motion-JPEG; MIME type: image/jpeg
  Frame sizes: 
    160x90 160x120 176x144 320x180 320x240 352x288 432x240 
    640x360 640x480 800x448 800x600 864x480 960x720
    1024x576 1280x720 1600x896 1920x1080
  Frame intervals: 1/30, 1/24, 1/20, 1/15, 1/10, 2/15, 1/5


"""

import cv2, sys
import numpy as np
import subprocess, re

keybindings="""
    + -    Brightness
    a      Toggle autofocus ('A' in the lower lefthand corner indicates autofocus)
    e      Edit mode. define perspective transfor by clicking 4 green circles.
    f F5   Toggle full screen mode. Note, this requires WDITH HEIGHT parameters of the screen
           to avoid loss if quality. Default: half camera resolution.
    ?      Show this help.
    q      Quit.
"""


pts = []
edit = True
autofocus = 1
windowsizecheck = 0

def windowsize():
  out = subprocess.check_output(["xdotool", "getactivewindow", "getwindowgeometry", "%1"])
  m = re.search("Geometry: (\d+)x(\d+)", str(out))
  if m:
    return [int(m.group(1)), int(m.group(2))]
  return None


def draw_mouse(event, x, y, flags, param):
    global edit, pts
    if event == cv2.EVENT_LBUTTONDOWN:
        print('draw_mouse: ', event, x, y, flags, param)
        if edit and len(pts) < 4:
                pts.append([x,y])       # add
        else:
            edit = False
    elif event == cv2.EVENT_LBUTTONUP:
        if edit:
            pts[-1] = [x, y]
    elif (event != 0):
        print('draw_mouse: ', event)
      

def show_webcam(mirror=False, scale=0.5, device=1, win_w=None, win_h=None):
    global edit, pts, autofocus, windowsizecheck

    cam = cv2.VideoCapture(device)
#    cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1600)
#    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 896)
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
#    cam.set(cv2.CAP_PROP_FRAME_WIDTH, 3000)
#    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 2000)
    # Logitech C920: If we request 3000x2000 we get 1920x1080
    cap_w = cam.get(cv2.CAP_PROP_FRAME_WIDTH)
    cap_h = cam.get(cv2.CAP_PROP_FRAME_HEIGHT)
    if win_w is None or win_h is None:
        (win_w, win_h) = (int(scale*cap_w), int(scale*cap_h))
    print("capture size: %dx%d" % (cap_w, cap_h))
    print("display size: %dx%d" % (win_w, win_h))
    cam.set(cv2.CAP_PROP_AUTOFOCUS, autofocus)
    backlight = 0       # cam.get(cv2.CAP_PROP_BACKLIGHT)
    fullscreen = False

    ## https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_mouse_handling/py_mouse_handling.html
    cv2.namedWindow("schicam", cv2.WINDOW_NORMAL)
    cv2.setMouseCallback("schicam", draw_mouse)
    ## https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_geometric_transformations/py_geometric_transformations.html
    #
    # dst = cv2.warpPerspective(img,M,(300,300))
    win_pts = [[0,0],[win_w,0],[win_w,win_h],[0,win_h]]
    (xs, ys) = (float(cap_w)/win_w,  float(cap_h)/win_h)        # scale back from win to cam
    M = None


    while True:
        ret_val, img = cam.read()
        if mirror:
            img = cv2.flip(img, 1)
        if edit is True or M is None:
            # must scale first into screen coordinates
            if scale != 1:
                img = cv2.resize(img, (win_w, win_h))
            # green dots for corners that are already set
            # and a red dot to hint at the next corner to set
            for p in pts:
                cv2.circle(img, (p[0], p[1]), 16, (0,255,0), 2, cv2.LINE_AA)
            if len(pts) < 4:
                p = win_pts[len(pts)]
                cv2.circle(img, (p[0], p[1]), 50, (0,0,255), 1, cv2.LINE_AA)
            else:
                pts1 = np.float32([[pts[0][0]*xs, pts[0][1]*ys], [pts[1][0]*xs, pts[1][1]*ys],
                                   [pts[3][0]*xs, pts[3][1]*ys], [pts[2][0]*xs, pts[2][1]*ys]])
                pts2 = np.float32([win_pts[0], win_pts[1], win_pts[3], win_pts[2]])
                M = cv2.getPerspectiveTransform(pts1,pts2)
        else:
            # perform transformation
            img = cv2.warpPerspective(img, M, (win_w, win_h))
        if autofocus:
            img = cv2.putText(img, 'A', (5, win_h-10), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 1)
            
        cv2.imshow('schicam', img)
        # waitKey 1: as fast as possible. 30: reduced frame rate
        k = cv2.waitKey(30) & 0xff
        if k in (27, ord('q')):
            break       # esc or q to quit
        elif k in (255, 226):
            # keyWait timeout, SHIFT
            if windowsizecheck > 0:
                windowsizecheck = windowsizecheck - 1
                if windowsizecheck == 0:
                    print(windowsize())
        elif k == ord('?'):
           print("\nKey Bindings:\n"+keybindings)
        elif k == ord('e'):
           edit = not edit
           if not edit: pts = []
        elif k in ( ord('+'), ord('-') ):
           bright = cam.get(cv2.CAP_PROP_BRIGHTNESS)
           bb = bright
           if k == ord('+'):
             bright += .05
             if bright > 1.0: bright = 1.0
           else:
             bright -= .05
             if bright < 0.0: bright = 0.0
           cam.set(cv2.CAP_PROP_BRIGHTNESS, bright)
           print("brightness %f -> %f" % (bb, bright))
        elif k == ord('a'):
           autofocus = 1 - autofocus
           cam.set(cv2.CAP_PROP_AUTOFOCUS, autofocus)
        elif k == ord('b'):
           backlight = 1 - backlight
           # cam.set(cv2.CAP_PROP_BACKLIGHT, backlight)
        elif k in ( 194, ord('f') ):    # F5 Fullscreen
           fullscreen = not fullscreen
           if fullscreen:
             cv2.setWindowProperty("schicam", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
             win_pts = [[0,0],[win_w,0],[win_w,win_h],[0,win_h]]
             (xs, ys) = (float(cap_w)/win_w,  float(cap_h)/win_h)        # scale back from win to cam
             windowsizecheck = 4
           else:
             cv2.setWindowProperty("schicam", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_NORMAL)
        else:
           print("unknown key code %d" % (k))
    cam.release()
    cv2.destroyAllWindows()


def main():
    if len(sys.argv) < 2:
        print("Usage: %s DEV [WIDTH HEIGHT]" % sys.argv[0])
        sys.exit(0)
    dev = sys.argv[1]
    if dev[:10] == '/dev/video': dev = dev[10:]
    if len(sys.argv) > 3:
        show_webcam(device=int(dev), win_w=int(sys.argv[2]), win_h=int(sys.argv[3]))
    else:
        show_webcam(device=int(dev), scale=0.5)


if __name__ == '__main__':
    main()
