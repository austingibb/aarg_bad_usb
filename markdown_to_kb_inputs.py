import argparse
import time
import os

def text_to_ducky(input_file, output_file, delay=5):
    """
    Converts a text file into a Rubber Ducky script that types its contents.
    """
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Error: File {input_file} not found.")
        return
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("DEFAULT_DELAY 69\n")  # Ensures proper pacing for typing
        
        for line in lines:
            line = line.strip().replace('"', '\\"')
            if line:
                f.write(f"STRING {line}\n")
            f.write("ENTER\n")
            f.write(f"DELAY {delay}\n")  # Delay between keystrokes to avoid input issues
    
    print(f"Ducky script saved to {output_file}")

def interactive_mode():
    test_dir = "./test_markdown_files"
    try:
        files = os.listdir(test_dir)
    except FileNotFoundError:
        print(f"Directory {test_dir} not found.")
        return

    md_files = [f for f in files if os.path.isfile(os.path.join(test_dir, f))]
    if not md_files:
        print(f"No files found in directory {test_dir}.")
        return

    print("Available files:")
    for idx, file in enumerate(md_files, start=1):
        print(f"{idx}: {file}")

    choice = input("Select a file by number: ")
    try:
        choice_index = int(choice) - 1
        if choice_index < 0 or choice_index >= len(md_files):
            print("Invalid choice.")
            return
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    input_file = os.path.join(test_dir, md_files[choice_index])
    output_file = input("Enter the output file path (.duck): ")
    delay_input = input("Enter delay between keystrokes in milliseconds (default 5): ")
    try:
        delay = int(delay_input)
    except ValueError:
        delay = 5

    text_to_ducky(input_file, output_file, delay)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert a text file to a Rubber Ducky script.")
    parser.add_argument("input", nargs="?", help="Path to the input text file.")
    parser.add_argument("output", nargs="?", help="Path to the output .duck script.")
    parser.add_argument("--delay", type=int, default=5, help="Delay between keystrokes (default: 5ms)")
    parser.add_argument("--interactive", action="store_true", help="Run in interactive mode selecting from ./test_markdown_files")
    args = parser.parse_args()

    if args.interactive:
        interactive_mode()
    elif args.input and args.output:
        text_to_ducky(args.input, args.output, args.delay)
    else:
        parser.print_help()
