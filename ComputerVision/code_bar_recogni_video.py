import cv2
import numpy as np

# DECODIFICAR DE CÓDIGO DE BARRAS
from pyzbar.pyzbar import decode
from PIL import Image

print('aqui')
# main_path = "img_code_bar/"
# url = main_path +"img1.png"
main_path = "img_code_bar/"
# cap = cv2.VideoCapture(main_path +'DJI_0022.MOV')
cap = cv2.VideoCapture(main_path +'DJI_0008.MP4')

scale_percent = 60 # percent of original size
ret, img = cap.read()
width = int(img.shape[1] * scale_percent / 127)
height = int(img.shape[0] * scale_percent / 127)
dim = (width, height)
img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
cv2.imshow("GRUPO QAIRA", img)

# width = int(img.shape[1] * scale_percent / 60)
# height = int(img.shape[0] * scale_percent / 60)

CB_READ = []
count = 0
import time
ret, img = cap.read()
time.sleep(2)
print("INICIOOOOOOOOOOOOOOOOOOOOOOO")
startTime = time.time()
while(cap.isOpened()):
    try:
        ret, img = cap.read()
        
        for barcode in decode(img):
            # print(barcode.data)
            myData = barcode.data.decode('utf-8')
            print(myData)
            try: # YA GUARDADO
                print(CB_READ.index(myData))
                pts = np.array([barcode.polygon],np.int32)
                pts = pts.reshape((-1,1,2))
                cv2.polylines(img,[pts],True,(100,250,100),2) 
                pts2 = barcode.rect
                cv2.putText(img,myData,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,2,(100,250,100),3)
            except: # POR GUARDAR
                CB_READ.append(myData)
                pts = np.array([barcode.polygon],np.int32)
                pts = pts.reshape((-1,1,2))
                cv2.polylines(img,[pts],True,(100,0,200),2) 
                pts2 = barcode.rect
                cv2.putText(img,myData,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,2,(100,0,200),3)
                count = count + 1
            # img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
            # print('Resized Dimensions : ',resized.shape)
        img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
        cv2.imshow("GRUPO QAIRA", img)
        # cv2.imshow("result", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    except:
        print("error")
        cap.release()
        cv2.destroyAllWindows()

executionTime = (time.time() - startTime)
print(f'Execution time in seconds: {str(executionTime)}\n')
print(f'Se han contado: {str(count)}\n')
print(f'Se ha almacenado: {str(len(CB_READ))}\n')
print(CB_READ)
# while True:
#     success, img = cap.read()
    
