# Book Bot

Welcome to Book Bot, your go-to Python program for diving deep into the heart of books with ease. Built as my very first project on boot.dev, Book Bot is designed to analyze entire books, providing a comprehensive statistical report that unveils the patterns, frequencies, and secrets hidden within the text.

## Features

- **Text Analysis:** Get detailed statistics on word count, frequency, and more.
- **Environment Friendly:** Runs in a virtual environment to manage dependencies efficiently.
- **Configurable:** Use a `.env` file to easily specify the book path without altering the source code.

## Prerequisites

Before you embark on your journey with Book Bot, ensure you have **Python 3** installed on your machine. Book Bot relies on Python's powerful libraries and virtual environments for a seamless experience.

## Installation

Follow these steps to set up Book Bot on your local machine:

1. **Clone the Repository**

   ```bash
   git clone https://your-repository-url/bookbot.git
   cd bookbot
   ```

2. **Set Up a Virtual Environment**

   Create a virtual environment to manage the project's dependencies separately from your global Python installation.

   ```bash
   python3 -m venv venv
   ```

   Activate the virtual environment:

   - On **Windows**:

     ```bash
     .\venv\Scripts\activate
     ```

   - On **macOS and Linux**:

     ```bash
     source venv/bin/activate
     ```

3. **Install Dependencies**

   With your virtual environment activated, install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the .env File**

   Book Bot uses a `.env` file to read the path of the book you want to analyze. Create a `.env` file in the root directory of the project and add the following line:

   ```plaintext
   BOOK_PATH=/path/to/your/book.txt
   ```

   Replace `/path/to/your/book.txt` with the actual path to the book file you wish to analyze.

## Usage

With Book Bot set up, you're ready to dive into the literary world. Run the program with:

```bash
python3 main.py
```

Enjoy exploring the depths of your favorite books through the lens of Book Bot's analytical prowess.

## Contributing

Your contributions are welcome! If you have suggestions to improve Book Bot, feel free to fork the repository, make your changes, and submit a pull request.

## License

[MIT License](LICENSE) - Feel free to use, modify, and distribute this software as you please.

## Acknowledgments

- Boot.dev for the inspiration and guidance on this project.
- The Python community for the invaluable resources and libraries.
