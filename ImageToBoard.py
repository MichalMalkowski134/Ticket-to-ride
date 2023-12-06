from ultralytics import YOLO
from PIL import Image, ImageDraw, ImageFont
import cv2
import shutil
import matplotlib.pyplot as plt
import math
import numpy as np
import os

class ImageToBoard:
    def __init__(self, image_path, model_path, model_grid_path, folder_path, folder_path2):
        self.image_path = image_path
        self.model_path = model_path
        self.model_grid_path = model_grid_path
        self.folder_path = folder_path
        self.folder_path2 = folder_path2
        self.columns = 18
        self.rows_in_columns = [11, 10, 11, 10, 11, 10, 11, 10, 11, 10, 11,10,11,10,11,10,11,10]
        self.rows = 11
        self.tab = [[None for _ in range(self.columns)] for _ in range(self.rows)]
        self.initialize_tab()
        self.model = None
        self.model_grid = None
        self.data = None
        self.data_detect = None
        if os.path.exists(folder_path):
            shutil.rmtree(folder_path)

        if os.path.exists(folder_path2):
            shutil.rmtree(folder_path2)

    def initialize_tab(self):
        self.tab[5][7]  = "1B"
        self.tab[9][5]  = "2B"
        self.tab[10][0] = "3B"
        self.tab[7][2]  = "4B"
        self.tab[2][1]  = "5B"
        self.tab[0][2]  = "6B"
        self.tab[9][9]  = "1C"
        self.tab[8][12] = "2C"
        self.tab[3][13] = "3C"
        self.tab[8][16] = "4C"
        self.tab[5][17] = "5C"
        self.tab[1][16] = "6C"
        self.tab[9][13] = "M"
        self.tab[2][17] = "M"
        self.tab[4][15]  = "M"
        self.tab[5][12]  = "M"
        self.tab[6][11]  = "M"
        self.tab[8][10]  = "M"
        self.tab[3][10]  = "M"
        self.tab[5][9]  = "M"
        self.tab[8][8]  = "M"
        self.tab[1][7]  = "M"
        self.tab[3][7]  = "M"
        self.tab[8][6]  = "M"
        self.tab[6][5]  = "M"
        self.tab[3][4] = "M"
        self.tab[0][3] = "J"
        self.tab[0][4] = "J"
        self.tab[5][8] = "J"
        self.tab[4][8] = "J"
        self.tab[3][8] = "J"
        self.tab[2][8] = "J"
        self.tab[1][8] = "J"
        self.tab[4][9] = "J"
        self.tab[3][9] = "J"
        self.tab[2][9] = "J"
        self.tab[1][9] = "J"
        self.tab[0][9] = "J"
        self.tab[0][10] = "J"
        self.tab[0][11] = "J"
        self.tab[0][12] = "J"
        self.tab[1][12] = "J"
        self.tab[2][12] = "J"
        self.tab[0][13] = "J"
        self.tab[1][13] = "J"
        self.tab[2][13] = "J"
        self.tab[4][13] = "J"
        self.tab[0][14] = "J"
        self.tab[4][14] = "J"
        self.tab[3][15] = "J"
        self.tab[3][16] = "J"
        self.tab[1][17] = "J"

    def load_model(self):
        self.model = YOLO(self.model_path)
        self.model_grid = YOLO(self.model_grid_path)
        
    def predict(self):
        self.model.predict(self.image_path, save=True, imgsz=640, conf=0.25,save_txt=True, save_conf=True)
        self.model_grid.predict(self.image_path, save=True, imgsz=640, conf=0.25,save_txt=True, save_conf=True)

    def load_data(self):
        self.data = np.loadtxt('runs/detect/predict2/labels/original.txt')
        self.data_detect = np.loadtxt('runs/detect/predict/labels/original.txt')
        row_numbers1 = np.arange(1, self.data_detect.shape[0] + 1)
        row_numbers2 = np.arange(1, self.data_detect.shape[0] + 1)
        self.data_detect = np.column_stack((self.data_detect, row_numbers1))
        self.data_detect = np.column_stack((self.data_detect, row_numbers2))

    def delete_duplicates(self, data_):
        # sortujemy dane po wierszach
        data_ = data_[data_[:, 1].argsort()]
        # iterujemy po wierszach
        in_len = len(data_)
        for i in range(in_len):
            # iterujemy po pozostałych wierszach
            for j in range(i + 1, in_len):
                # jeśli rows są podobne
                if abs(data_[i][1] - data_[j][1]) < 0.0015 and abs(data_[i][2] - data_[j][2]) < 0.0015:
                    # usuwamy wiersz o mniejszym confidence
                    if data_[i][5] > data_[j][5]:
                        data_ = np.delete(data_, j, axis=0)
                        in_len -= 1
                        break
                    else:
                        data_ = np.delete(data_, i, axis=0)
                        in_len -= 1
                        break
        
        return data_

    def draw_hex(self, x_, y_, board_,size_, angle_, text_=None):
        draw = ImageDraw.Draw(board_)

        x0, y0 = x_ + size_ * math.cos(angle_), y_ - size_ * math.sin(angle_)
        x1, y1 = x_ + size_ * math.cos(angle_ + math.radians(60)), y_ - size_ * math.sin(angle_ + math.radians(60))
        x2, y2 = x_ + size_ * math.cos(angle_ + math.radians(120)), y_ - size_ * math.sin(angle_ + math.radians(120))
        x3, y3 = x_ + size_ * math.cos(angle_ + math.radians(180)), y_ - size_ * math.sin(angle_ + math.radians(180))
        x4, y4 = x_ + size_ * math.cos(angle_ + math.radians(240)), y_ - size_ * math.sin(angle_+ math.radians(240))
        x5, y5 = x_ + size_ * math.cos(angle_ + math.radians(300)), y_ - size_* math.sin(angle_ + math.radians(300))

        points = [x0, y0, x1, y1, x2, y2, x3, y3, x4, y4, x5, y5]
        draw.polygon(points, outline=(0, 0, 0),fill='green')

        if text_:
            color = "yellow"
            if text_ == "J":
                draw.polygon(points, outline=(0, 0, 0),fill='blue')
                color = "red"
            if text_ == "M":
                draw.polygon(points, outline=(0, 0, 0),fill='gray')
                color = "red"
            if text_ == "1B" or text_ == "2B" or text_ == "3B" or text_ == "4B" or text_ == "5B" or text_ == "6B" or text_ == "1C" or text_ == "2C" or text_ == "3C" or text_== "4C" or text_ == "5C" or text_ == "6C":
                draw.polygon(points, outline=(0, 0, 0),fill='yellow')
                color = "red"
            center_x = x_
            center_y = y_
            font = ImageFont.load_default()
            text_length = draw.textlength(text_, font=font)
            text_x = center_x - text_length/2
            text_y = center_y-5  

            draw.text((text_x, text_y), text_, fill=color, font=font)

    def draw_board(self, columns_, rows_in_columns_, tab_):
        hex_size = 20
        weight = 640
        height = 400

        board = Image.new('RGB', (weight, height), (255, 255, 255))
        x = hex_size
        y = hex_size
        space = hex_size * 3**0.5 / 2  # Odległość między środkami heksów

        for i, column in enumerate(range(columns_)):
            if i % 2 == 0:
                y = hex_size
            else:
                y = hex_size + hex_size * 3**0.5/2
            for j, rows in enumerate(rows_in_columns_):
                if i < columns_ and j < rows:
                    if tab_[j][i] is not None:
                        if i % 2 != 1 or j!=10:
                            self.draw_hex(x, y,board, hex_size, 0, text_=tab_[j][i])
                    else:
                        if i % 2 != 1 or j!=10:
                            self.draw_hex(x, y,board, hex_size, 0, text_="")
                y += space * 2
            x += space * 2
        board.save('board.png')
        return board

    def draw_rectangles(self, data_,path_):
        image = Image.open(path_)
        draw = ImageDraw.Draw(image)
        image_width, image_height = image.size
        i = 0
        data_ = data_[data_[:, 1].argsort()]
        m = 0
        l = 11


        for i in range(18): 

            if (i+1)%2 == 1:
                first_11_elements = data_[m:l]
                sorted_first_11_elements = first_11_elements[first_11_elements[:, 2].argsort()]
                data_[m:l] = sorted_first_11_elements
                m = l
                l = l + 10

            if (i+1)%2 == 0:
                first_10_elements = data_[m:l]
                sorted_first_10_elements = first_10_elements[first_10_elements[:, 2].argsort()]
                data_[m:l] = sorted_first_10_elements
                m = l
                l = l + 11

        row_numbers1 = np.arange(1, data_.shape[0] + 1)
        row_numbers2 = np.arange(1, data_.shape[0] + 1)
        row_numbers3 = np.arange(1, data_.shape[0] + 1)

        # Dodawanie nowych kolumn do tablicy data
        data_ = np.column_stack((data_, row_numbers1))
        data_ = np.column_stack((data_, row_numbers2))
        data_ = np.column_stack((data_, row_numbers3))
        

        k = 0
        j = 0

        for ix,row in enumerate(data_):
            data_[ix][8] = k
            data_[ix][7] = j
            j = j + 1
            if k%2 == 0:
                if j == 11:
                    k = k + 1
                    j = 0
            if k%2 == 1:
                if j == 10:
                    k = k + 1
                    j = 0



        i = 1

        for row in data_:
            # Get the class and dimensions
            class_, x_prop, y_prop, width_prop, height_prop, conf,index,o,p = row

            x = x_prop * image_width
            y = y_prop * image_height
            width = width_prop * image_width
            height = height_prop * image_height
            x1 = x + width/2
            x2 = x - width/2
            y1 = y + height/2
            y2 = y - height/2

            # Draw a circle at the center
            draw.ellipse((x - 5, y - 5, x + 5, y + 5), fill='red')
            draw.rectangle([(x2,y2), (x1,y1)], outline="red")

            # Draw the class label
            text = f'{index:.0f}'
            font = ImageFont.truetype("fonts/Ubuntu-Regular.ttf", size=100)
            draw.text((x2, y2 - 10), text, fill="red",font= font)
            i += 1
        image.save('output.jpg')
        return image, data_ 
    
    def process_data(self):
        self.data = self.delete_duplicates(self.data)
        self.data_detect = self.delete_duplicates(self.data_detect)
        image2 = Image.open(self.image_path)
        image3,grid = self.draw_rectangles(self.data,self.image_path)

        for i in range(self.data_detect.shape[0]):
            distances = np.sqrt(np.sum((grid[:, [1, 2]] - self.data_detect[i, [1, 2]])**2, axis=1))
            closest_index = np.argmin(distances)
            self.data_detect[i, [6, 7]] = grid[closest_index, [7, 8]]

        for row in self.data_detect:
            class_, x_prop, y_prop, width_prop, height_prop, conf,o,p = row
            o = int(o)
            p = int(p)
            self.tab[o][p] = str(class_)

        image = self.draw_board(self.columns, self.rows_in_columns, self.tab)

        fig = plt.figure(figsize=(10, 8))
        plt.imshow(image)
        plt.axis('off')
        plt.show()
        fig1 = plt.figure(figsize=(10, 8))
        plt.imshow(image2)
        plt.axis('off')
        plt.show()
        fig12 = plt.figure(figsize=(10, 8))
        plt.imshow(image3)
        plt.axis('off')
        plt.show()

    def run(self):
        self.load_model()
        self.predict()
        self.load_data()
        self.process_data()
        tab = self.tab
        return tab
    