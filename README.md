# DirectoryTreeWeb

DirectoryTreeWeb is a Flask-based web application that generates a visual representation of directory structures. Users can input a local directory path, and the application will display the directory tree in a web interface.

## Features

- Generate directory trees from local file paths
- Web-based interface for easy interaction
- Copy generated tree structure to clipboard
- Clear output functionality
- Responsive and modern UI design

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/DirectoryTreeWeb.git
   cd DirectoryTreeWeb
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On macOS and Linux: `source venv/bin/activate`

4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the Flask application:
   ```
   python app.py
   ```

2. Open a web browser and navigate to `http://localhost:5000`

3. Enter a valid directory path in the input field and click "Generate Tree"

4. Use the "Copy" button to copy the generated tree to your clipboard

5. Use the "Clear Output" button to reset the display

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.