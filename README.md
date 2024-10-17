# DirectoryTreeWeb

DirectoryTreeWeb is a Flask-based web application that generates a visual representation of directory structures. Users can input a local directory path, and the application will display the directory tree in a web interface.

## Features

- Generate directory trees from local file paths
- Web-based interface for easy interaction
- Copy generated tree structure to clipboard
- Clear output functionality
- Responsive and modern UI design
- Custom favicon
- One-click run script for easy startup
- Blacklist folders: Hide content of specified folders to prevent lengthy outputs (e.g., virtual environments or library directories)


## Blacklist Functionality

DirectoryTreeWeb includes a feature that allows users to exclude the contents of certain folders (e.g., `venv`, `node_modules`) from the displayed tree. This is particularly useful for directories with many files or nested structures, as it helps keep the output concise.

The blacklist is defined within `app.py` as a list of folder names.

# Example of blacklist definition
   ```
   blacklist = ["venv", "node_modules", "dist", "build"]
   ```

To customize, simply add or remove folder names in this list.

# How It Works

When generating the directory tree, if a folder name matches one in the blacklist, only the folder name is shown in the output, without listing its contents.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/GeoShaPoH/DirectoryTreeWeb.git
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

### Method 1: Using the run script

1. Double-click the `run_directory_tree_web.bat` file in the project directory.
2. The application will start and open in your default web browser automatically.

### Method 2: Manual startup

1. Activate the virtual environment (if not already activated)
2. Run the Flask application:
   ```
   python app.py
   ```
3. Open a web browser and navigate to `http://localhost:5000`

### Using the application

1. Enter a valid directory path in the input field and click "Generate Tree"
2. Use the "Copy" button to copy the generated tree to your clipboard
3. Use the "Clear Output" button to reset the display

## Creating a Desktop Shortcut

1. Right-click on your desktop
2. Select "New" > "Shortcut"
3. Browse to the location of `run_directory_tree_web.bat` and select it
4. Name the shortcut (e.g., "DirectoryTreeWeb")

Now you can double-click this shortcut to start the application quickly.

## Project Structure

```
DirectoryTreeWeb/
│
├── venv/
├── static/
│   └── favicon.svg
├── templates/
│   └── index.html
├── app.py
├── requirements.txt
├── run_directory_tree_web.bat
├── .gitignore
├── LICENSE
└── README.md
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.