def convert_hex_to_pcn6(hex_number):
    # Convert the hexadecimal number to decimal
    decimal_value = int(hex_number, 16)
    
    # Add 10000 to the decimal value
    pcn6_number = decimal_value + 10000
    
    return pcn6_number

def generate_and_convert_combinations(symbols, length, limit):
    import itertools
    
    # Generate combinations using itertools.product
    combinations = itertools.product(symbols, repeat=length)
    
    # Define sets of numbers and letters for filtering
    number_set = set('0123456789')
    letter_set = set('BCDEF')  # Exclude 'A' from letters to be used in filtering
    
    count = 0
    for combo in combinations:
        if count >= limit:
            break
        combo_str = ''.join(combo)
        if 'A' in combo_str:
            continue  # Skip combinations with 'A'
        if any(char in number_set for char in combo_str) and any(char in letter_set for char in combo_str):
            # Convert and print the results
            pcn6_number = convert_hex_to_pcn6(combo_str)
            print(f"For transmitter: {combo_str}, for PCN : {pcn6_number}")
            count += 1

# Define symbols and parameters
symbols = '0123456789BCDEF'  # Include 'A' initially but filter it out later
length = 4
limit = 200

# Generate, filter, convert, and display the results
generate_and_convert_combinations(symbols, length, limit)
