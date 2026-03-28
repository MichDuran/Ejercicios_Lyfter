numbers_list = [53, 60, 32, 62, 400, 10]


def remove_tenths():
  index = 0
  while (index < len(numbers_list)):
    if numbers_list[index] % 10 == 0:
      numbers_list.pop(index)
    else:
      index += 1


def multiply_numbers_by_2():
  for index, number in enumerate(numbers_list):
    numbers_list[index] = number * 2


def main():
  remove_tenths()
  multiply_numbers_by_2()
  print(numbers_list)


if __name__ == "__main__":
  main()
  