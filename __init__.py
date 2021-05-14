import cv2
yuz_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
goz_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

kamera = cv2.VideoCapture(0)

while True:
    _,goruntu = kamera.read()
    griton = cv2.cvtColor(goruntu,cv2.COLOR_BGR2GRAY)
    yuzler=yuz_cascade.detectMultiScale(griton,1.1,5)

    for (x,y,w,h) in yuzler:
        cv2.rectangle(goruntu,(x,y),(x+w,y+h),(0,255,255),3)
        roi_griton=griton[y:y+h,x:x+w]#yüzün bölgesini aldık
        roi_renkli=goruntu[y:y+h,x:x+w]#renklide
        gozler=goz_cascade.detectMultiScale(roi_griton)#gözleri tespit etmesi için bu
        for(ex,ey,ew,eh) in gozler: #tespit edilen yüzlerin içinde gözleride bu şekilde buldurduk w
            cv2.rectangle(roi_renkli,(ex,ey),(ex+ew,ey+eh),(0,0,255),1)
    cv2.imshow('goruntu,',goruntu)
    if cv2.waitKey(25) & 0xFF==ord('q'):
        break
kamera.release()
cv2.destroyAllWindows()

