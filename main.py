talabalar = [
    {"ism": "Ali", "ball": 85},
    {"ism": "Vali", "ball": 90},
    {"ism": "Hasan", "ball": 78},
    {"ism": "Husan", "ball": 92},
    {"ism": "Rustam", "ball": 88}
]

talabalar.sort(key=lambda x: x["ball"])
print(talabalar)
