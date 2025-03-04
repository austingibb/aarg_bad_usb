import argparse
import time
import os
import mimetypes

ENTER_DELAY_DEFAULT = 500
TEST_MARKDOWN_FILES = "./test_markdown_files"

# Static help prompt constants
HELP_INPUT = "Path to the input text file."
HELP_OUTPUT = "Path to the output .ducky.txt script."
HELP_DELAY_BETWEEN_STROKES = f"Delay between keystrokes after each ENTER (default: 5ms)"
HELP_ENTER_DELAY = f"Delay before issuing the ENTER command (default: {ENTER_DELAY_DEFAULT}ms)"
HELP_INTERACTIVE = f"Run in interactive mode selecting from {TEST_MARKDOWN_FILES}"

def is_text_file(filepath, blocksize=512):
    """
    Checks if a file is human readable by looking for null bytes and valid UTF-8 encoding.
    """
    try:
        with open(filepath, 'rb') as file:
            data = file.read()
            if b'\0' in data:
                return False
            try:
                data.decode('utf-8')
            except UnicodeDecodeError:
                return False
    except Exception as e:
        print(f"Error reading file: {e}")
        return False
    return True

def ensure_extension(output_file):
    """
    Checks if output_file has a recognized extension using mimetypes.
    If not, appends '.ducky.txt'.
    """
    base, ext = os.path.splitext(output_file)
    if not ext:
        return output_file + ".ducky.txt"

# If the guessed MIME type is None or 'application/octet-stream' (often means unrecognized)
    mime_type, _ = mimetypes.guess_type(output_file)
    if not mime_type or mime_type == "application/octet-stream":
        return output_file + ".ducky.txt"
    
    return output_file

def text_to_ducky(input_file, output_file, delay=5, enter_delay=0):
    """
    Converts a human-readable text file into a Rubber Ducky script.
    Lines inside triple backtick code blocks preserve leading spaces 
    (to maintain code indentation). Lines outside code blocks are stripped.
    Empty lines become a single space to ensure no empty STRING is generated.
    """
    if not is_text_file(input_file):
        print("Error: Input file is not human readable (non-UTF or binary content detected).")
        return

    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Error: File {input_file} not found.")
        return
    
    output_file = ensure_extension(output_file)
    
    in_code_block = False
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"DEFAULT_DELAY {delay}\n")
        
        for line in lines:
            # Toggle code block state if we see a line containing triple backticks
            if "```" in line:
                in_code_block = not in_code_block

            if in_code_block:
                # Remove only trailing newline; keep other whitespace for indentation
                line = line.rstrip("\n").replace('"', '\\"')
            else:
                # Outside code blocks, strip as usual
                line = line.strip().replace('"', '\\"')

            # If the line is empty, replace with a single space so we don't create an empty STRING
            if not line:
                line = " _ "

            f.write(f"STRING {line}\n")
            f.write("ENTER\n")
            f.write(f"DELAY {enter_delay}\n")
    
    print(f"Ducky script saved to {output_file}")

def interactive_mode():
    test_dir = TEST_MARKDOWN_FILES
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
    output_file = input(f"Enter {HELP_OUTPUT.lower()[:-1]} (.ducky.txt will be added if no ext is provided): ")
    delay_input = input("Enter delay between keystrokes in milliseconds (default 5): ")
    try:
        delay = int(delay_input)
    except ValueError:
        delay = 5

    enter_delay_input = input(f"Enter delay before creating new line in milliseconds (default {ENTER_DELAY_DEFAULT}): ")
    try:
        enter_delay = int(enter_delay_input)
    except ValueError:
        enter_delay = ENTER_DELAY_DEFAULT

    output_file = ensure_extension(output_file)
    text_to_ducky(input_file, output_file, delay, enter_delay)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert a text file to a Rubber Ducky script (human-readable text only).")
    parser.add_argument("input", nargs="?", help=HELP_INPUT)
    parser.add_argument("output", nargs="?", help=HELP_OUTPUT)
    parser.add_argument("--delay", type=int, default=5, help=HELP_DELAY_BETWEEN_STROKES)
    parser.add_argument("--enter-delay", type=int, default=ENTER_DELAY_DEFAULT, help=HELP_ENTER_DELAY)
    parser.add_argument("--interactive", action="store_true", help=HELP_INTERACTIVE)
    args = parser.parse_args()

    if args.interactive:
        interactive_mode()
    elif args.input and args.output:
        out_path = ensure_extension(args.output)
        text_to_ducky(args.input, out_path, args.delay, args.enter_delay)
    else:
        parser.print_help()
