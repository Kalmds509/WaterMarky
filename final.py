import  cv2
import glob
import os

def menu():
    print("1- Pou logo plase anwo a goch")
    print("2- Pou anwo a dwat")
    print("3- Pou anba a goch")
    print("4- Pou anba a dwat")
    print("5- Pou logo an santre")
    chwa=input("Kijan ouy vle modifikasyon an fet: ")
    if chwa=="1":
        logo=cv2.imread("code9.png")
        h_logo, w_logo, _=logo.shape

        images_path=glob.glob("imaj/*.*")
        # print(images_path)
        for img_path in images_path:
            img=cv2.imread(img_path)
            h_img, w_img, _=img.shape

            center_y = int(h_img/2)
            center_x = int(w_img/2)
            top_y = center_y - int(h_img/2)
            left_x = center_x - int(w_img/2)
            bottom_y = top_y + h_logo
            right_x = left_x + w_logo

            roi=img[top_y:bottom_y,left_x:right_x]
            result = cv2.addWeighted(roi, 1, logo, 0.3, 0)

            img[top_y:bottom_y, left_x:right_x] = result
            
            filename = os.path.basename(img_path)
            
            cv2.imwrite("withLogo/watermarked_"+filename,img)
            print("Add success")


    elif chwa=="2":
        logo=cv2.imread("code9.png")
        h_logo, w_logo, _=logo.shape

        images_path=glob.glob("imaj/*.*")
        # print(images_path)
        for img_path in images_path:
            img=cv2.imread(img_path)
            h_img, w_img, _=img.shape

            center_y = int(h_img/2)
            center_x = int(w_img/2)
            top_y = center_y - int(h_img/2)
            left_x = center_x - int(w_img/2)
            bottom_y = top_y + h_logo
            right_x = left_x + w_logo

            roi=img[top_y:bottom_y,left_x:right_x]
            result = cv2.addWeighted(roi, 1, logo, 0.7, 0)

            img[top_y:bottom_y, left_x:right_x] = result
            
            filename = os.path.basename(img_path)
            
            cv2.imwrite("withLogo/watermarked_"+filename,img)
            print("Add success")
        
    elif chwa=="3":
        pass
    elif chwa=="4":
        pass
    elif chwa=="5":
        pass


            # h_img, w_img, _ = resized_img.shape
            # center_y = int(h_img/2)
            # center_x = int(w_img/2)
            # top_y = center_y - int(h_img/2)
            # left_x = center_x - int(w_img/2)
            # bottom_y = top_y + h_img
            # right_x = left_x + w_img
            # roi = resized_img[top_y:bottom_y, left_x:right_x]
            # result = cv2.addWeighted(roi, 1, logo, 0.3, 0)
            # resized_img[top_y:bottom_y, left_x:right_x] = result
            # filename = os.path.basename(img_path)
            # cv2.imwrite("withLogo/watermarked_"+filename, resized_img)
            # cv2.imshow("Watermarked Image", resized_img)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()
   
menu()





