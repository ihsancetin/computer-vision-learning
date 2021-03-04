import cv2          #opencv kütüphanesinin eklenmesi
resimx=cv2.imread('agacc.jpg',0)    #imread komutu ile resmin okunması 0 ile siyah beyaz yapılması
cv2.imshow('baslıkk',resimx)           #imshow komutu ile resmin basılması
cv2.imwrite('gri.png',resimx)           #resmin kaydedilmesi
cv2.waitKey(0)                          #waitkey delay
cv2.destroyAllWindows()                 #tüm pencerelerin kapatılması