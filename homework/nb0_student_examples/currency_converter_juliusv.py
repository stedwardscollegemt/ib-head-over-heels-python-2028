# Mostly copied from AI-generated response

# My program asks the user for an amount in (USD) and converts it
# into (EUR) using a fixed exchange rate. It keeps asking until
# the user types q to quit.

# Exchange rate: 1 USD = 0.8887 EUR
# We tell the computer what eur p usd means
EUR_PER_USD = 0.8887 

def convert_usd_to_eur(amount_usd):
    """Convert an amount in US dollars to euros."""
    return amount_usd * EUR_PER_USD

def main():
    print("Currency converter: US Dollar > Euro")
    print("Rate: 1 USD = " + str(EUR_PER_USD) + " EUR (Stand 18.10.2026)")
    print("Type q to quit.\n")

    while True:
        user_input = input("Amount in USD: ")

        # Stop the program if the user types q
        if user_input.lower() == "q":
            print("Goodbye!")
            break

        try:
            amount_usd = float(user_input)
        except ValueError:
            print("Please enter a number, for example 25.50\n")
            continue

        # Checks if the amount_usd is valid
        if amount_usd < 0:
            print("The amount cannot be negative.\n")
            continue

        # Calculates - rounded to 2 dec places
        amount_eur = convert_usd_to_eur(amount_usd)
        print(f"{amount_usd:.2f} USD = {amount_eur:.2f} EUR\n")

main()