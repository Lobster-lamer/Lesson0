from textColor import Color

# 2nd programm
print("\nХорошо, но может у тебя проблемы с логикой? Правда ли, что\n" +
      "9.99 больше, чем 9.98 и 1000 не равно 1000.1 одновременно?")
print(Color.GREEN, "Легко отвечу на ваш вопрос, ответ:", Color.WHITE,
      (9.99 > 9.98 and 1000 != 1000.1))
