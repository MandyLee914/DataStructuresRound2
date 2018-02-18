## Mandy Ewing
## Part A
## Feb. 18, 2018
## Worked w/ Autumn


def RECPractice(number):
    steps = 0

    while(number > 1):

        if number % 2 == 0:
            steps += 1
            number = number //2
        else:
            number = (number * 3) + 1
            steps += 1

            
    print("Steps Taken: ", steps)
            






RECPractice(number = int(input("Enter your desired number choice: ")))
