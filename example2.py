import ImageToBoard 
import RoadDefineScript
import numpy as np

image_path = 'dataset/age_of_steam/board/original3.jpg'
model_path = 'Roboflow_model/best.pt'
model_grid_path = 'Roboflow_model/best_grid.pt'
folder_path = 'runs/detect/predict'
folder_path2 = 'runs/detect/predict2'

image_to_board = ImageToBoard.ImageToBoard(image_path, model_path, model_grid_path, folder_path, folder_path2)
tab , tabNp = image_to_board.run()
map = np.array(tab)
print(tabNp.shape)

print(tab)
print(tabNp)

new_roads = RoadDefineScript.Main_Algorithm_Translated_Map(tabNp)
print(new_roads)
