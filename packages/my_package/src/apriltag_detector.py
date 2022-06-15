import cv2
import apriltag
import math


def dist(p1, p2):
    x_p1, y_p1 = int(p1[0]), int(p1[1])
    x_p2, y_p2 = int(p2[0]), int(p2[1])

    return math.sqrt((x_p2 - x_p1) ** 2 + (y_p2 - y_p1) ** 2)


def area(p1, p2, p3):
    return dist(p1, p2) * dist(p1, p3)


def detect_apriltag(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    options = apriltag.DetectorOptions(families="tag36h11")
    detector = apriltag.Detector(options)
    results = detector.detect(gray)
    print("[INFO] {} total AprilTags detected".format(len(results)))
    if len(results) == 0:
        # show the output image after AprilTag detection
        cv2.imshow("Image", image)
        cv2.waitKey(0)
        return

    # print(len(results))
    max_r = results[0]
    max_r_area = 0
    # for r in results:
    #     # extract the bounding box (x, y)-coordinates for the AprilTag
    #     # and convert each of the (x, y)-coordinate pairs to integers
    #     (ptA, ptB, ptC, ptD) = r.corners
    #     ptB = (int(ptB[0]), int(ptB[1]))
    #     ptC = (int(ptC[0]), int(ptC[1]))
    #     ptD = (int(ptD[0]), int(ptD[1]))
    #     ptA = (int(ptA[0]), int(ptA[1]))
    #     print(f"ptA: {ptA}, ptB:{ptB}, ptC:{ptC}")
    #     curr_area = area(ptD, ptC, ptB)
    #     print(f"Found rectangle with area {curr_area}")
    #     if curr_area > max_r_area:
    #         max_r = r

    (ptA, ptB, ptC, ptD) = max_r.corners
    ptB = (int(ptB[0]), int(ptB[1]))
    ptC = (int(ptC[0]), int(ptC[1]))
    ptD = (int(ptD[0]), int(ptD[1]))
    ptA = (int(ptA[0]), int(ptA[1]))
    # draw the bounding box of the AprilTag detection
    cv2.line(image, ptA, ptB, (0, 255, 0), 2)
    cv2.line(image, ptB, ptC, (0, 255, 0), 2)
    cv2.line(image, ptC, ptD, (0, 255, 0), 2)
    cv2.line(image, ptD, ptA, (0, 255, 0), 2)
    # draw the center (x, y)-coordinates of the AprilTag
    (cX, cY) = (int(max_r.center[0]), int(max_r.center[1]))
    cv2.circle(image, (cX, cY), 5, (0, 0, 255), -1)
    # draw the tag family on the image
    tag_title = max_r.tag_family.decode("utf-8") + str(max_r.tag_id)
    cv2.putText(image, tag_title, (ptA[0], ptA[1] - 15),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    print("[INFO] tag family: {}".format(tag_title))

    # show the output image after AprilTag detection
    cv2.imshow("Image", image)
    cv2.waitKey(0)


images = [cv2.imread(f'duckieTownTags/Pic{i}.png') for i in range(12)]

for index, image in enumerate(images):
    detect_apriltag(image)