from textColor import Color


# 4th programm

def find_fractional(float_number: float) -> int:
    return int(float_number * 100 % 100)


first_number = 13.42
second_number = 42.13

result = (find_fractional(first_number) == int(second_number)
          or find_fractional(second_number) == int(first_number))
print("\nЛадно, остался один вопрос, и я отвяжу тебя от батареи:...")
print(f"{Color.GREEN}Ура! Домой! Убедиться в том, что целая часть хотя бы одного\n" +
      f"из чисел {first_number} и {second_number} равна дробной части другого? " +
      f"Легко! Ответ:{Color.WHITE}{result}")
print("КАК ТЫ УЗНАЛ?! 0_0")
