import numpy as np
import cv2


class Operation:

    def __init__(self):
        pass

    def merge(self, image_left, image_right, column):
        """
        Merge image_left and image_right at column (column)
        
        image_left: the input image 1
        image_right: the input image 2
        column: column at which the images should be merged

        returns the merged image at column
        """
        box = np.zeros((350, 340), np.uint8)
        shape = box.shape

        for i in range(shape[0]):
            for j in range(shape[1]):
                if i in range(0, 350) and j in range(0, column):
                    box[i, j] = image_left[i, j]
                if i in range(0,350) and j in range(column, 340):
                    box[i, j] = image_right[i, j]
        # this places left and right images on the white box i made in line 22

        return box

    def intensity_scaling(self, input_image, column, alpha, beta):
        """
        Scale your image intensity.

        input_image: the input image
        column: image column at which left section ends
        alpha: left half scaling constant
        beta: right half scaling constant

        return: output_image
        """
        box = input_image.copy()
        shape = box.shape
        for i in range(shape[0]):
            for j in range(shape[1]):
                if i in range(0, 350) and j in range(0, column):
                    box[i, j] *= alpha
                if i in range(0, 350) and j in range(column, 340):
                    box[i, j] *= beta

        # Please do not change the structure
        return box  # Currently the input image is returned, please replace this with the intensity scaled image

    def centralize_pixel(self, input_image, column):
        """
        Centralize your pixels (do not use np.mean)

        input_image: the input image
        column: image column at which left section ends

        return: output_image
        """
        total_L, count_l, total_R, count_r = 0, 0, 0, 0
        box = input_image.copy()
        shape = box.shape
        for i in range(shape[0]):
            for j in range(shape[1]):
                if i in range(0, 350) and j in range(0, column):
                    total_L += box[i,j]
                    count_l+=1
                if i in range(0,350) and j in range(column, 340):
                    total_R += box[i,j]
                    count_r += 1

        offset_L = 128 - (total_L/count_l)
        offset_R = 128 - (total_R/count_r)
#offset calculated for left and right^
#below i am adding offset to each pixel
        for i in range(shape[0]):
            for j in range(shape[1]):
                if i in range(0, 350) and j in range(0, column):
                    if box[i, j] + offset_L < 0:
                        box[i,j] = 0
                    elif box[i, j] + offset_L > 255:
                        box[i, j] = 255
                    else:
                        box[i, j] += offset_L
                if i in range(0, 350) and j in range(column, 340):
                    if box[i, j] + offset_R < 0:
                        box[i,j] = 0
                    elif box[i, j] + offset_R > 255:
                        box[i, j] = 255
                    else:
                        box[i, j] += offset_R




        return box   # Currently the input image is returned, please replace this with the centralized image
