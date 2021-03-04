import cv2
kopek_resmi=cv2.imread('kopek.jpg')
print(str(kopek_resmi.item(100,100,0)))  #resimdeki 100x100 luk pikseldeki rgb rengin değeri 0,mavi 1,yesil 2,kırmzı
print(str(kopek_resmi.shape))           #resimin piksel değerleri 300x300x3 gibi
print(str(kopek_resmi.size))            #resimdeki piksel sayısı
print(str(kopek_resmi.dtype))           #uint8 gibi
bolge=kopek_resmi[400:500,900:1100]     #resmin ilgili bölesini bulma
kopek_resmi[200:300,800:1000]=bolge     #ilgili aynı büyüklükler eşitlenebilir
"""mavi,yesil,kırmızı=cv2.split(kopek_resmi)  resmi rgb matrislerini parçalar daha rahat işlem yapmak için
kopek_resmi=cv2.merge((mavi,yesil,kırmızı))   resmi katmanları birleştirir 
#ama bu yöntem bilgisayarı kastırabilir
#kopek_resmi[:,:,0]=255 gibi değiştirilebilir 0 mavi 1 yeşil 2 kırmızı
"""
"""
for i in range(100):
    for j in range(100):
        kopek_resmi.itemset(i,j,2,255)      #resimde seçilmiş piksel değerini değiştirir
        kopek_resmi.itemset(i,j,1,0)
        kopek_resmi.itemset(i,j,0,0)
"""
cv2.imshow('sfds',kopek_resmi)
cv2.imshow('fsdf',bolge)
cv2.waitKey(0)
cv2.destroyAllWindows()