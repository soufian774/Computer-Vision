import cv2

img = cv2.imread("res_lezione2/elon.jpg", cv2.IMREAD_GRAYSCALE)

integral = cv2.integral(img)

print(integral)