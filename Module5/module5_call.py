from module5_mod import NumberProcessor

def main():
    n = int(input("Enter N: "))
    processor = NumberProcessor()
    processor.read_numbers(n)
    x = int(input("Enter X: "))
    print(processor.search_number(x))

if __name__ == "__main__":
    main()