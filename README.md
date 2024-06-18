# image2table
This project processes images to extract text using OCR and converts the text into structured data in a CSV format.

## Setup

### Prerequisites

- Python 3.7+
- Tesseract OCR

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/ocr-image-processing.git
    cd ocr-image-processing
    ```

2. Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```

3. Ensure Tesseract is installed and the `TESSDATA_PREFIX` environment variable is set:
    ```sh
    export TESSDATA_PREFIX=/usr/local/share/tessdata/
    ```

### Installing Python and Pip

#### Windows

1. Download Python from the official website: [python.org](https://www.python.org/downloads/windows/)
2. Run the installer and follow the instructions, ensuring to check the box to add Python to your PATH.
3. Verify the installation:
    ```sh
    python --version
    pip --version
    ```

#### macOS

1. Install Homebrew if you haven't already:
    ```sh
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```
2. Install Python:
    ```sh
    brew install python
    ```
3. Verify the installation:
    ```sh
    python3 --version
    pip3 --version
    ```

#### Linux (Ubuntu)

1. Update the package list:
    ```sh
    sudo apt update
    ```
2. Install Python:
    ```sh
    sudo apt install python3 python3-pip
    ```
3. Verify the installation:
    ```sh
    python3 --version
    pip3 --version
    ```

## Usage

1. Place the images to be processed in a directory.

2. Run the main script with the images directory and output directory as arguments:
    ```sh
    python src/main.py /path/to/images /path/to/output
    ```

3. The processed CSV files will be saved in the specified output directory.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
