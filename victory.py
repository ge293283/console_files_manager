# Module 1

# Launching the game means automatic consent
consentToTheGame = "y"

# The first, general part of the link and a dictionary with answers (key = answer, value = id number to form the link)
link = "https://orpheusradio.ru/persons/id/"
dict_answers  = {"Abbado Claudio 26.06.1933": "52087",
                 "Ives Charles Edward 20.10.1874": "48039",
                 "Palestrina Giovanni 17.12.1725": "12085",
                 "Пастернак Борис Леонидович 10.02.1890": "45978",
                 "Janáček Leoš 03.07.1854": "49015",}

# Set the number of attempts in 0
user_attempt = 0

# As long as the user agrees to the game - the loop is running
while consentToTheGame == "y":
    print("Начинаем викторину!")

    # Number of questions
    num_of_questions = 5
    # Correct answer counter
    sum_CorrectAnswers = 0
    # Correct wrong counter
    sum_WrongAnswers = 0

    # We check if there are less than 1 attempts, then we ask for the username, if less we display the number of the attempt
    if user_attempt < 1:
        user_name = input("Представтесь, пожалуйста: ")
        print("{},викторина состоит из {} вопросов.".format(user_name, num_of_questions),"НАЧИНАЕМ!\n")
        user_attempt += 1
    else:
        print("{},викторина состоит из {} вопросов. Попытка № {}.\n".format(user_name, num_of_questions, user_attempt))
    # Define a counter for the loop
    counter = 0
    # Until we ask all the questions, we do not exit the cycle
    while counter < num_of_questions:
        # 1. Abbado Claudio 26.06.1933 (https://orpheusradio.ru/persons/id/52087)
        yearOfBirth_AbbadoClaudio = input("1. Введите год рождения Аббадо Клаудио (например: 1900): ")
        if yearOfBirth_AbbadoClaudio == "1933":
            sum_CorrectAnswers += 1
        else:
            sum_WrongAnswers += 1
        counter += 1
        # 2. Ives Charles Edward 20.10.1874 (https://orpheusradio.ru/persons/id/45978)
        yearOfBirth_IvesCharlesEdward = input("2. Введите год рождения Айвза Чарлза Эдварда (например: 1900): ")
        if yearOfBirth_IvesCharlesEdward == "1874":
            sum_CorrectAnswers += 1
        else:
            sum_WrongAnswers += 1
        counter += 1
        # 3. Palestrina Giovanni 17.12.1725 (https://orpheusradio.ru/persons/id/48039)
        yearOfBirth_PalestrinaGiovanni = input("3. Введите год рождения Палестрина Джованни (например: 1900): ")
        if yearOfBirth_PalestrinaGiovanni == "1725":
            sum_CorrectAnswers += 1
        else:
            sum_WrongAnswers += 1
        counter += 1
        # 4. Пастернак Борис Леонидович 10.02.1890 (https://orpheusradio.ru/persons/id/12085)
        yearOfBirth_PasternakBorisLeonidovich = input("4. Введите год рождения Пастернака Бориса Леонидовича (например: 1900): ")
        if yearOfBirth_PasternakBorisLeonidovich == "1890":
            sum_CorrectAnswers += 1
        else:
            sum_WrongAnswers += 1
        counter += 1
        # 5. Janáček Leoš 03.07.1854 (https://orpheusradio.ru/persons/id/49015)
        yearOfBirth_JanacekLeos = input("5. Введите год рождения Яначека Леоша (например: 1900): ")
        if yearOfBirth_JanacekLeos == "1854":
            sum_CorrectAnswers += 1
        else:
            sum_WrongAnswers += 1
        counter += 1

    # Percentage of correct answers
    percentage_CorrectAnswers = sum_CorrectAnswers * 100 / num_of_questions
    # Percentage of wrong answers
    percentage_WrongAnswers  = sum_WrongAnswers * 100 / num_of_questions

    # Displaying the test result
    print()
    print("Количество правельных ответов: {} ({} %)".format(sum_CorrectAnswers, percentage_CorrectAnswers))
    print("Количество ошибок: {} ({} %)".format(sum_WrongAnswers, percentage_WrongAnswers))
    print()

    # We suggest another attempt to pass the test
    consentToTheGame = input("Вы хотите начать сначала? y/n: ")
    print()
    # If you agree, increase the number of attempts by 1, otherwise we offer to show the answers
    if consentToTheGame == 'y':
        user_attempt += 1
    else:
        answers = input("{}, показать правельные ответы? y/n: ".format(user_name, user_attempt))
        print()
        if answers == 'y':
            # Cycle output answers by the number of questions
            i = 1
            while i < num_of_questions:
                for value, key in zip(dict_answers.values(), dict_answers.keys()):  # Using the zip() method to traverse the values and keys of a dictionary in parallel
                    print("{}. {} ({}{})".format(i, key, link, value))
                    i += 1
        break