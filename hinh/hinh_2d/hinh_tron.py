import math

# tinh chu vi hinh tron
# ten function: chu_vi
# input: ban_kinh
# output: chu_vi 
def chu_vi(ban_kinh):
    chu_vi =  ban_kinh * 2 * math.pi
    return chu_vi

# tinh dien tich hinh tron
# ten function: dien_tich
# input: ban_kinh
# output: dien_tich 
def dien_tich(ban_kinh):
    dien_tich =  (ban_kinh**2)*math.pi
    return dien_tich