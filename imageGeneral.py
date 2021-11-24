import cv2 as cv
import numpy as np

class LoadImage:
    @staticmethod
    def __load_image(file_name):
        return cv.imread(file_name)

    @staticmethod
    def show_image(file_image):
        cv.imshow("title", file_image)
        cv.waitKey(0)
        cv.destroyAllWindows()

    def load_raw_image(self, file_name):
        return self.__load_image(file_name)

    def load_hsv_image(self, file_name):
        img = self.__load_image(file_name)
        return cv.cvtColor(img, cv.COLOR_BGR2HSV)

    def extract_color_image(self, file_name, hue, saturation, brightness):
        threshold = 10
        low_color = [hue - threshold, saturation - threshold, brightness - threshold]
        high_color = [hue + threshold, saturation + threshold, brightness + threshold]

        hsv_image = self.load_hsv_image(file_name)





