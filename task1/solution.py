def helper(month, day, all_months_and_sign):
    if month == 12 and day > 21: 
        return "Козирог"
    elif month * 100 + day <= all_months_and_sign[0][0]:  
        return all_months_and_sign[0][1]
    else:
        return helper(month, day, all_months_and_sign[1:])


def what_is_my_sign(day, month):
    return helper(
        month, day, [(119, "Козирог"), (218, "Водолей"), (320, "Рибa"),
                     (420, "Овен"), (520, "Телец"), (620, "Близнаци"),
                     (721, "Рак"), (822, "Лъв"), (922, "Дева"),
                     (1022, "Везни"), (1121, "Скорпион"), (1221, "Стрелец")])
