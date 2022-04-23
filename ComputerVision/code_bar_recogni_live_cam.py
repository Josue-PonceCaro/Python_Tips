import cv2
import numpy as np

# DECODIFICAR DE CÓDIGO DE BARRAS
from pyzbar.pyzbar import decode
from PIL import Image


# main_path = "img_code_bar/"
# url = main_path +"img1.png"

cap = cv2.VideoCapture(0)
cap.set(3,640) # whith
cap.set(4,480) # height
dim = (640, 480)
CB_READ = []
count = 0
while True:
    success, img = cap.read()
    try:
        # ret, img = cap.read()
        
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
                cv2.putText(img,myData,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,1,(100,250,100),3)
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

print(f'Se han contado: {str(count)}\n')
print(f'Se ha almacenado: {str(len(CB_READ))}\n')
print(CB_READ)

# cap = cv2.VideoCapture(0)
# cap.set(3,640) # whith
# cap.set(4,480) # height

# while True:
#     success, img = cap.read()
#     for barcode in decode(img):
#         # print(barcode.data)
#         myData = barcode.data.decode('utf-8')
#         print(myData)
#         pts = np.array([barcode.polygon],np.int32)
#         pts = pts.reshape((-1,1,2))
#         cv2.polylines(img,[pts],True,(255,0,255),5) 
#         pts2 = barcode.rect
#         cv2.putText(img,myData,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,0.9,(255,0,255),2)
#     cv2.imshow("result", img)
#     cv2.waitKey(1)
