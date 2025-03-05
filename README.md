# Human Readable Text to Ducky Script Converter

## Overview

This repository contains a **Python script** that converts any human readable file into a **Ducky Script**. The generated script can be used with a **Flipper Zero** in **Bad USB mode** to type out the contents of the human readable file onto any computer that accepts keyboard input.

## Features

- Converts any human readable file into a **.ducky script**.
- Outputs keystrokes that can be injected via **Flipper Zero Bad USB mode**.
- Simple and lightweight with minimal dependencies.

## Requirements

- **Python 3.x**
- **Flipper Zero** (or any compatible Bad USB device)

## Installation

Clone the repository:

```sh
git clone <repo_url>
cd <repo_folder>
```

## Usage

Run the script to convert a `.txt` file or `.md` file into a `.ducky` script:

```sh
python human_readable_to_kb_inputs.py input.md output.ducky.txt
```

### Parameters

- `input.md` → Path to the human readable file to convert.
- `output.ducky.txt` → Path where the generated Ducky Script will be saved.

## Example

If you have a file named `example.md`, convert it with:

```sh
python human_readable_to_kb_inputs.py example.md example.ducky.txt
```

Then, load `example.ducky.txt` onto your **Flipper Zero**, set it to **Bad USB mode**, and execute it on the target device.

## License

This project is licensed under the **MIT License**. You are free to use, modify, distribute, and even use it commercially without restriction.

### MIT License

```
MIT License



Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE
```

