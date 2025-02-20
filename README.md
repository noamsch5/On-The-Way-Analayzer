# README.md

# On The Way Analyzer

On The Way Analyzer is a program designed to analyze EDM-style WAV tracks, identify their genre and sub-genres, and provide SEO suggestions for YouTube. The application connects to the YouTube API to search for similar tracks and offers keyword suggestions based on the genre, related tracks, and labels.

## Features

- Analyze uploaded EDM-style WAV tracks.
- Identify genre and sub-genres of the tracks.
- Connect to the YouTube API to find similar tracks.
- Generate SEO suggestions including descriptions and tags for YouTube.
- Provide keyword suggestions based on genre and related tracks.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/on-the-way-analyzer.git
   ```

2. Navigate to the project directory:
   ```
   cd on-the-way-analyzer
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Upload your WAV track using the provided interface.
2. The program will analyze the track and identify its genre.
3. SEO suggestions and similar tracks will be generated based on the analysis.

## Configuration

Configuration settings, including API keys, can be found in the `config.yaml` file. Make sure to update it with your own credentials.

## Running Tests

To run the unit tests, use the following command:
```
pytest tests/
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.