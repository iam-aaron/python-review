def computepay(h,r):
    if in_hrs > 40:
        min_hrs = 40
        exc_hrs = in_hrs - min_hrs
    else:
        min_hrs = in_hrs
        exc_hrs = 0

    payout = (min_hrs * rate) + (exc_hrs * (rate * 1.5))
    return payout

user_input_hrs = input("Enter Hours: ")
in_hrs = float(user_input_hrs)
user_input_rate = input("Enter Rate per Hour: ")
rate = float(user_input_rate)

p = computepay(in_hrs,rate)

print("Pay",p)
