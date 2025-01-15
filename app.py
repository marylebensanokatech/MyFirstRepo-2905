def build_sandwich(ingredients):
    if not ingredients:
        print("You need to choose some ingredients!")
        return
        
    print("Let's make a sandwich!")
    print("🥖 First, we grab some bread...")
    
    for i, ingredient in enumerate(ingredients, 1):
        print(f"Adding {ingredient}...")
    
    print("And top it with bread!")
    print(f"\nCongrats! You made a {' and '.join(ingredients)} sandwich!")

def main():
    try:
        print("Welcome to the Sandwich Maker!")
        ingredients_input = input("Enter ingredients (separated by commas): ")
        ingredients = [i.strip() for i in ingredients_input.split(",")]
        
        build_sandwich(ingredients)
            
    except Exception as e:
        print("Oops, something went wrong! Let's try again.")

if __name__ == "__main__":
    main()