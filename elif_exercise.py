valid_input = 0
while valid_input == 0:
    try:
        input_score = input("Enter Score: ")
        score = float(input_score)
        valid_input = 1
    except:
        continue

if score > 1 or score < 0:
    rate = 'Score out of range.'
elif score >= 0.9:
    rate = 'A'
elif score >= 0.8:
    rate = 'B'
elif score >= 0.7:
    rate = 'C'
elif score >= 0.6:
    rate = 'D'
elif score < 0.6:
    rate = 'F'
else:
    rate = 'Invalid Rating'

print(rate)
