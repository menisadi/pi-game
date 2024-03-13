import argparse
import time
import os
import mpmath  # For high precision arithmetic


def _calculate_pi(num_digits):
    mpmath.mp.dps = (
        num_digits + 2
    )  # Set the precision to required number of digits
    return str(mpmath.pi)  # Return pi as a string with desired precision


def learn_digits(num_digits, delay=None):
    pi_digits = _calculate_pi(num_digits)
    if delay:
        for digit in pi_digits:
            print(digit, end=" ", flush=True)
            time.sleep(delay / 1000)
    else:
        print(" ".join(pi_digits))


def test_digits(interactive=False):
    num_digits = len(_calculate_pi(1000))  # Get the number of digits of pi
    user_input = input(f"Enter the digits of pi you know: ")
    correct_pi = _calculate_pi(num_digits)
    wrong_digits = []
    for i, digit in enumerate(user_input):
        if digit != correct_pi[i]:
            wrong_digits.append(correct_pi[i])
        if interactive:
            os.system("cls" if os.name == "nt" else "clear")
            print(
                "".join(correct_pi[: i + 1])
                + "".join(
                    "\033[91m" + d + "\033[0m" for d in correct_pi[i + 1 :]
                )
            )
    total_digits = len(user_input)
    correct_digits = total_digits - len(wrong_digits)
    print(f"Total digits entered: {total_digits}")
    print(f"Correct digits: {correct_digits}")
    print(f"Incorrect digits: {' '.join(wrong_digits)}")


def history():
    try:
        with open("pi_practice_history.txt", "r") as file:
            data = file.read()
            print(data)
    except FileNotFoundError:
        print("No history available yet.")


def main():
    parser = argparse.ArgumentParser(
        description="Practice memorizing digits of pi."
    )
    parser.add_argument(
        "-l", "--learn", type=int, help="Number of digits to learn"
    )
    parser.add_argument(
        "-d",
        "--delay",
        type=int,
        default=None,
        help="Delay between displaying digits in milliseconds",
    )
    parser.add_argument(
        "-t", "--test", action="store_true", help="Test your knowledge of pi"
    )
    parser.add_argument(
        "-i",
        "--interactive",
        action="store_true",
        help="Enable interactive testing",
    )
    parser.add_argument(
        "-H", "--history", action="store_true", help="Display test history"
    )

    args = parser.parse_args()

    if args.learn:
        learn_digits(args.learn, args.delay)
    elif args.test:
        test_digits(args.interactive)
    elif args.history:
        history()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
