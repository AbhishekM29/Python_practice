def get_places(city):

places = {

'mumbai': ['Gateway of India', 'Marine Drive', 'Siddhivinayak Temple', 'Juhu Beach'],

'pune': ['Shaniwar Wada', 'Aga Khan Palace', 'Sinhagad Fort', 'Dagdusheth Ganpati

Temple'],

'nagpur': ['Deekshabhoomi', 'Futala Lake', 'Ambazari Lake', 'Raman Science Centre'],

'nashik': ['Trimbakeshwar Temple', 'Sula Vineyards', 'Pandavleni Caves', 'Anjneri Hill'],

'aurangabad': ['Ajanta Caves', 'Ellora Caves', 'Bibi Ka Maqbara', 'Daulatabad Fort']

}

city = city.lower()

if city in places:

return f"Popular places in {city.capitalize()} are: " + ", ".join(places[city])

else:

return "Sorry, I don't have information about that city."

def chatbot():

print("Hello! I can help you find popular places in cities of Maharashtra.")

print("Type 'exit' to end the chat.")

while True:

user_input = input("\nEnter the name of the city: ")

if user_input.lower() == 'exit':

print("Goodbye! Have a nice day!")

break

response = get_places(user_input)

print(response)

chatbot()
