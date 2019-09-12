ListGPA = [2.1,2.5,4,3]

def Reward (GPA):
    bonus = 500000
    Reward = GPA*bonus
    return Reward

for GPA in ListGPA:
    if GPA >2.5:
        print("Selamat dan mendapatkan Reward : Rp", Reward(GPA))
    else :
        print("Maaf anda tidak bisa.")