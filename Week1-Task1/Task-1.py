import random

def generate_password(length=12, complexity='hard'):
    # Define character sets based on complexity level
    characters = ''
    if complexity == 'easy':
        characters += '0123456789abcdefghijklmnopqrstuvwxyz'
    elif complexity == 'medium':
        characters += 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    else:  # Default to 'hard'
        characters += 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    length = int(input("Enter password length: "))
    complexity = input("Select password complexity (easy/medium/hard): ").lower()

    if complexity not in ['easy', 'medium', 'hard']:
        print("Invalid complexity level. Defaulting to 'hard'.")
        complexity = 'hard'

    password = generate_password(length, complexity)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
