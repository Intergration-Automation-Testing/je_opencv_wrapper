import cv2

from je_open_cv.modules import template_detection

image = template_detection.find_object("test.png", "test_template.png")
