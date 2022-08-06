
import cv2

image_path = 'anno'

image = cv2.imread(image_path + '.png')

class_list = ['using mask', 'without mask']
colors = [(0, 255, 0), (0, 255, 255)]

height, width, _ = image.shape

T=[]
with open(image_path + '.txt', "r") as file1:
    for line in file1.readlines():
        split = line.split(" ")

        # getting the class id
        class_id = int(split[0])
        color = colors[class_id]
        clazz = class_list[class_id]
        # print(class_id, color, clazz)

        # getting the xywh bounding box coordinates
        x, y, w, h = float(split[1]), float(split[2]), float(split[3]), float(split[4])
        # print(x, y, w, h)

        # re-scaling xywh to the image size
        box = [int((x - 0.5*w)* width), int((y - 0.5*h) * height), int(w*width), int(h*height)]
        # print(box)
        cv2.rectangle(image, box, color, 2)
        cv2.rectasngle(image, (box[0], box[1] - 20), (box[0] + box[2], box[1]), color,2)
        # cv2.putText(image, class_list[class_id], (box[0], box[1] - 5), cv2.FONT_HERSHEY_SIMPLEX, .5, (0,0,0))

cv2.imshow("output", image)
cv2.waitKey()
