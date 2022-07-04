from datetime import date

d=(2013,3,15)

date(d[0], d[1], d[2])


def new_user(active=False, admin=False):
    print(active)
    print(admin)

config = {"active" : False, "admin":True}

new_user(**config)