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
        threshold = 40
        low_color = np.array([hue - threshold, saturation - threshold, brightness - threshold])
        high_color = np.array([hue + threshold, saturation + threshold, brightness + threshold])

        # hsv_image = self.load_hsv_image(file_name)
        # return cv.inRange(hsv_image, low_color, high_color)
        raw_image = self.load_raw_image(file_name)
        return cv.inRange(raw_image, low_color, high_color)

    def contour_image(self, file_image):
        #  輪郭の抽出モード一覧　https://bit.ly/3nPMHEm
        #  輪郭の近似 https://bit.ly/3HUYdqj
        image, contours, hierarchy = cv.findContours(file_image, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

        max_area_list = list(map(cv.contourArea, contours))
        max_area_value = max(max_area_list)
        if(max_area_value == 0):
            return 0

        max_area_index = max_area_list.index(max_area_value)
        # 抽出した領域のうち、最大面積の領域
        # contours[max_area_index]
        # モーメントを取得する
        moment_result = cv.moments(contours[max_area_index])
        # 産出したモーメントから各種情報を取得する方法　https://bit.ly/3cJD9ER

        # これはXY座標情報
        cx = int(moment_result['m10'] / moment_result['m00'])
        cy = int(moment_result['m01'] / moment_result['m00'])

        return image
