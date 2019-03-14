import cv2
import numpy as np

def match_all(imagePath, templatePath, confidence):
    # load image
    img_rgb = cv2.imread(imagePath)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    img_gray = img_gray[0:1000, 0:300]
    #load template
    template = cv2.imread(templatePath,0)
    w, h = template.shape[::-1]
    image_width, image_height = img_gray.shape[::-1]

    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    loc = np.where( res >= confidence)

    for pt in list(zip(*loc[::-1])):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
        # value = (pt[0], pt[1]+13)
        # cv2.rectangle(img_rgb, value, (image_width, value[1]+13), (0,0,255), 1)

    cv2.imwrite('res1.png',img_rgb)
    return list(zip(*loc[::-1]))

print(match_all('test.png', 'target.png', 0.75))