void main() {
  var client = Client('Alex');
  client.add(100);
  print(client.get());
  var loyalClient = LoyalClient('Gigel');
  loyalClient.add(100);
  print(loyalClient.get());
  loyalClient.discount();
  print(loyalClient.get());
}