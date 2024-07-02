from textColor import Color

# 3rd programm
first_number = 1234
second_number = 5678

first_number = int(str(first_number)[1:3])
second_number %= 1000
second_number //= 10
print("\nСмотри дальше... Есть два стула...\n" +
      "В смысле, есть 2 числа: 1234 и 5678.\n" +
      "Правда они очень оригинальны?:3..." +
      "Найди сумму их серединных чисел.")
print("{}Вот их сумма: {}{}".format(Color.GREEN,
                                    Color.WHITE,
                                    first_number + second_number))
