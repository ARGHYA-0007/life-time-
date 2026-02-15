import cv2
def start():
    x=input("enter your image path or location")
    y=input("for \nshow the image-->show\ngrayscale the image-->gray\nsave the image-->save")
    if(y.lower()=='show'):
        print("Showing image....")
        image=cv2.imread(x,1)
        cv2.imshow("your image",image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif(y.lower()=='gray'):
        print("converting your image to grayscale....")
        image=cv2.imread(x,0)
        cv2.imshow("your image",image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        wannasave=input("wanna save that gray scaled image? y/n")
        if(wannasave.lower()=="y"):
           imname=input("enter what you want to name of the image:\n")
           cv2.imwrite(f"{imname}.png",image) 
        else:
            return
    elif(y.lower()=="save"):
        imname=input("enter what you want to name of the image:\n")
        image=cv2.imread(x,1)
        cv2.imwrite(f"{imname}.png",image)
        print(f"file name successfully saved as name of {imname}.png")
    else:
        print("umm.. i think you enter some invalid input try again")
        start()
start()