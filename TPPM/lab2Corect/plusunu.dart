void main(List<String> args) {
  // plusunu.dart 1 2 3
  // plusunu.dart 9 9 9
  print(args);
  int number = 0;
  for (var i = 0; i < args.length; i++) {
    number = number * 10 + int.parse(args[i]);
  }
  number++;
  // print(number);
  var result = [];
  while (number > 0) {
    result.add(number % 10);
    number = number ~/ 10;
  }
  print(result.reversed.toList());
}
