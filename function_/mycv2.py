import cv2
import numpy as np
import os

def newImread(filenameread, flags=cv2.IMREAD_COLOR, dtype=np.uint8):
    try:
        n = np.fromfile(filenameread, dtype)
        img = cv2.imdecode(n, flags)
        return img
    except Exception as e:
        print(e)
        return None


def newImwrite(filenamewrite, img, params=None):
    try:
        ext = os.path.splitext(filenamewrite)[1]
        result, n = cv2.imencode(ext, img, params)

        if result:
            with open(filenamewrite, mode='w+b') as f:
                n.tofile(f)
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False