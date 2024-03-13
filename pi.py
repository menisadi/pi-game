import time
import mpmath


def _calculate_pi(num_digits):
    mpmath.mp.dps = (
        num_digits + 2
    )  # Set the precision to required number of digits

    # Return pi as a string with desired precision
    return str(mpmath.pi)


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


def main():
    learn_digits(10, delay=100)


if __name__ == "__main__":
    main()
