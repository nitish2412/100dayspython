age: int
name: str
is_human: bool
height: float

def police_check(age:int)->bool:
    if(age>18):
        car_drive = True
    else:
        car_drive = False
    return car_drive

print(police_check(19))