import password_detector

while True:
    response = input('Enter Password:\n')
    result = password_detector.strength_detector(response)
    print(response)
    match result:
        case 'Invalid':
            print("The password you entered was invalid.")

            continue
        case _: # Default case
            print(f"Password strength: {result}.")
            break   

