import os
import time
import mpmath


def _calculate_pi(num_digits):
    mpmath.mp.dps = (
        num_digits + 2
    )  # Set the precision to required number of digits

    # Return pi as a string with desired precision
    return str(mpmath.pi)[:-1]


def add_space_every_four_chars(input_string):
    # TODO: not sure if this the best way to do so
    result = ""
    for i in range(0, len(input_string), 4):
        result += input_string[i : i + 4] + " "
    return result.strip()


def learn_digits(num_digits, delay=None):
    pi_digits = _calculate_pi(num_digits)
    pi_after_decimal_point = add_space_every_four_chars(pi_digits[2:])
    pi_digits = pi_digits[:2] + " " + pi_after_decimal_point
    if delay:
        for digit in pi_digits:
            print(digit, end="", flush=True)
            time.sleep(delay / 1000)
    else:
        print(" ".join(pi_digits))


def check(num):
    length_after_point = len(num) - 2
    true_pi = _calculate_pi(length_after_point)
    checked_digits = ""
    correction = ""
    for input_d, true_d in zip(num, true_pi):
        if input_d == true_d:
            checked_digits += input_d
            correction += " "
        else:
            checked_digits += "\033[91m" + input_d + "\033[0m"
            correction += true_d

    print("Endte the digits you know:")
    print(checked_digits)
    print(correction)


def main():
    os.system("clear")
    user_input = input("Enter the digits you know:\n")
    os.system("clear")
    check(user_input)

    # learn_digits(3, delay=100)


if __name__ == "__main__":
    main()
