def verify_card_number(card_number):
    """
    Verify the validity of a credit card number using the Luhn algorithm.

    Parameters:
    - card_number (str): The credit card number to be validated.

    Returns:
    - bool: True if the card number is valid, False otherwise.
    """
    # Initialize variables to store the sum of odd and even digits
    sum_of_odd_digits = 0
    
    # Reverse the card number
    card_number_reversed = card_number[::-1]
    
    # Select every other digit starting from the last digit (odd indices)
    odd_digits = card_number_reversed[::2]

    # Calculate the sum of the odd digits
    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    sum_of_even_digits = 0
    # Select every other digit starting from the second-to-last digit (even indices)
    even_digits = card_number_reversed[1::2]
    
    # Calculate the sum of the even digits after doubling them and adjusting if necessary
    for digit in even_digits:
        number = int(digit) * 2
        if number >= 10:
            number = (number // 10) + (number % 10)
        sum_of_even_digits += number
        
    # Calculate the total sum of digits
    total = sum_of_odd_digits + sum_of_even_digits
    
    # Check if the total sum modulo 10 equals 0, indicating a valid card number
    return total % 10 == 0

def main():
    """
    Entry point of the program.
    """
    # Example card number
    card_number = '4111-1111-4555-11'
    
    # Remove hyphens and spaces from the card number
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

    # Validate the card number using the verify_card_number function
    # and print the result    
    if verify_card_number(translated_card_number):
        print('VALID!')
    else:
        print('INVALID!')

main()