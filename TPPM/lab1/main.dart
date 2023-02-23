isPrime(int number) {
  for (var i = 2; i * i <= number; i++) {
    if (number % i == 0) {
      return false;
    }
  }
  return true;
}

ex1([int numberOfPrimes = 100]) {
  int count = 0;
  int number = 2;
  var list = [];
  while (count < numberOfPrimes) {
    if (isPrime(number)) {
      list.add(number);
      count++;
    }
    number++;
  }
  return list;
}

ex2(String phrase) {
  var listOfWords = [];
  phrase.trim().split(" ").forEach((element) {
    element.length > 0
        ? (",/!?\'".contains(element[element.length - 1]) == false)
            ? listOfWords.add(element)
            : listOfWords.add(element.substring(0, element.length - 1))
        : null;
  });
  return listOfWords;
}

ex3(String phrase) {
  var words = ex2(phrase);
  var numbers = [];
  for (var word in words) {
    if (int.tryParse(word) != null) {
      numbers.add(int.parse(word));
    } else if (double.tryParse(word) != null) {
      numbers.add(double.parse(word));
    }
  }
  return numbers;
}

bool isCapitalLetter(String character) {
  return character.codeUnitAt(0) >= 65 && character.codeUnitAt(0) <= 90;
}

String ex4(String characters) {
  var sb = StringBuffer();

  for (int i = 0; i < characters.length; i++) {
    if (isCapitalLetter(characters[i]) == true)
      sb.write('_' + characters[i].toLowerCase());
    else
      sb.write(characters[i]);
  }

  return sb.toString();
}

void main() {
  int optiune = 3;
  switch (optiune) {
    case 1:
      print(ex1());
      break;
    case 2:
      print(ex2("Salut!, eu sunt     Alex    "));
      break;
    case 3:
      print(ex3(
          "11Salu11t!, 12312312 eu sunt 23123 11.32  Alex    . Am 3 chestiute"));
      break;
    case 4:
      print(ex4("SalutCeMaaiFaci"));
      break;
    default:
      print("Hello World");
  }
}
