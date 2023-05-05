"""
  안녕하세요. 관련 함수 설명드립니다!
  imread : cv2의 imread는 경로에 한글이 있을 경우 인식을 못합니다
  이를 인코더로 유니코드로 변경 후 인식할 수 있게끔 만들었습니다. imwrite도 동일합니다
  사용하려는 파일 안에 xml을 넣어주세요
  모든 file path는 맨 끝에 / 를 붙여주세요 ex. 'C:/Users/hop09/Desktop/ToyProject/'
  
"""
import numpy as np
import cv2
import os
import mycv2
        

def ImageCrop(file_path , xml_path , new_img_name) : 
  os.chdir(file_path)
  xml_name = "haarcascade_frontalface_default.xml"
  file_list = os.listdir(file_path)
  for i in range(len(file_list)) :
    image = mycv2.newImread(os.path.join(file_path, file_list[i]))
    face_cascade = cv2.CascadeClassifier(os.path.join(xml_path, xml_name))

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.5, 5) 
    """첫번째 -> gray이미지를 가져오겠다, 두번째 : 이미지 스케일 조정, 세번째 얼굴 감지기 민감도 조정, 스케일 조정인자가 클수록 얼굴이 아무리 작아도 감지될 가능성이 높고, 세번째인자가 작을 수록 얼굴이 작못된 위치에서 감지될 가능성이 높아짐
    scaleFactor: 1.1에서 1.5 사이 
    minNeighbors: 0에서 10 사이 -> 단, 보통 3-6사이로 지정
    """
    
    for (x,y,w,h) in faces :
        # cv2.rectangle(image, (x+10,y+10), (x+w+10, y+h+10), (255,0,0), 2) #10 만큼의 유예를 줌
        cropped = image[y:y+h+10, x:x+w+10]
        resize = cv2.resize(cropped, (180,180))
        
        mycv2.newImwrite(f"{new_img_name}_{i}.jpg", resize)

# def ImageCrop(image_file_path , xml_file_path , new_img_name) : 
#   file_list_name = get_file(image_file_path)
#   for i in range(len(file_list_name)) :
#     image = mycv2.newImread(os.path.join(image_file_path, file_list_name[i]))
#     face_cascade = cv2.CascadeClassifier(xml_file_path)

#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     faces = face_cascade.detectMultiScale(gray, 1.5, 5) 
#     """첫번째 -> gray이미지를 가져오겠다, 두번째 : 이미지 스케일 조정, 세번째 얼굴 감지기 민감도 조정, 스케일 조정인자가 클수록 얼굴이 아무리 작아도 감지될 가능성이 높고, 세번째인자가 작을 수록 얼굴이 작못된 위치에서 감지될 가능성이 높아짐
#     scaleFactor: 1.1에서 1.5 사이 
#     minNeighbors: 0에서 10 사이 -> 단, 보통 3-6사이로 지정
#     """
    
#     for (x,y,w,h) in faces :
#         # cv2.rectangle(image, (x+10,y+10), (x+w+10, y+h+10), (255,0,0), 2) #10 만큼의 유예를 줌
#         cropped = image[y:y+h+10, x:x+w+10]
#         resize = cv2.resize(cropped, (180,180))
#         mycv2.newImwrite(f"{new_img_name}{i}.jpg", resize)