from pytube import YouTube

while True:
    print("\n   Çıkış Yapmak İçin -> Q Tuşuna Basın   ")
    link = input("İndirilecek Video Url'ini Giriniz : ")
    
    if  "https://www.youtube.com/" in link.lower():
        yt = YouTube(link)
        
        print("Kanal Sahibi : ", yt.author)
        print("Video Başlığı : ", yt.title)
        print("İzlenme Sayısı : ", yt.views)
        print("Paylaşılma Tarihi : ", yt.publish_date)
        
        yd = yt.streams.get_highest_resolution()
        
        yd.download("./video")
    elif link.upper() == "Q":
        break;
    else:
        print("Hatalı Giriş Tekrar Deneyiniz !!! \n")