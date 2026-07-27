import extractor, sys

while True:
    response = input('Do you want to extract data? (y/n)')
    if response.lower() == 'y':
        print("App is running...")
        print("Copy the text you want to extract from.")
        new_response = input('Press any key when done copying...')
        try:
            extractor.extractor()
        except KeyboardInterrupt:
            sys.exit()
    else:
        sys.exit()
