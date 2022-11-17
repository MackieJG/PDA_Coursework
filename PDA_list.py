list_of_cars_models = ["Micra", "Qashqui", "Juke", "Skyline"]

def list_of_cars_starting_with_J(cars):
    check = "J"
    cars_list_with_J = [car for car in cars if car[0] == check]
    print(cars_list_with_J)

list_of_cars_starting_with_J(list_of_cars_models)