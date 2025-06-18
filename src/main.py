import joblib

if __name__ == '__main__':
    print("main")
    modelo = joblib.load("../model/random_forest.pkl")
    number_of_rooms = input("Enter the number of rooms: ")
    lstat = input("Enter the lower status population percentage: ")
    ptratio = input("Enter the pupil-teacher rate by town: ")
    model_input = [[number_of_rooms, lstat, ptratio]]
    house_value = modelo.predict(model_input)
    print(f"Predicted house value: {house_value[0]}")
