from hinh.hinh_2d import hinh_tron as hi_tron
from hinh.hinh_2d import hinh_vuong as hi_vuong
from hinh.hinh_3d import hinh_tru as hi_tru

ban_kinh_hinh_tron = float(input("ban kinh hinh tron: "))
chu_vi_hinh_tron = hi_tron.chu_vi(ban_kinh_hinh_tron)
dien_tich_hinh_tron = hi_tron.dien_tich(ban_kinh_hinh_tron)
print("chu vi hinh tron: ", chu_vi_hinh_tron)
print("dien tich hinh tron: ", dien_tich_hinh_tron)

canh_hinh_vuong = float(input("canh hinh vuong: "))
chu_vi_hinh_vuong = hi_vuong.chu_vi(canh_hinh_vuong)
dien_tich_hinh_vuong = hi_vuong.dien_tich(canh_hinh_vuong)
print("chu vi hinh vuong: ", chu_vi_hinh_vuong)
print("dien tich hinh vuong: ", dien_tich_hinh_vuong)


ban_kinh_day = float(input("ban kinh day: "))
duong_cao = float(input("duong cao: "))
the_tich_hinh_tru = hi_tru.the_tich(ban_kinh_day, duong_cao)
print("the tich hinh tru: ", the_tich_hinh_tru)

