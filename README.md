# Jikan API Flask App

## Overview
This project demonstrates how to work with the [Jikan API](https://docs.api.jikan.moe/), an unofficial API for retrieving information about anime. Specifically, this app fetches and displays an anime episode and its synopsis using Flask.

The project focuses on:
- Generating a random anime ID using Python's `random` library.
- Using the random ID to construct an endpoint:  
  `https://api.jikan.moe/v4/anime/{random_number}`.
- Fetching and displaying the episode synopsis in a Flask web app.

## Features
- **Random Anime Selector**: Generates a random anime ID (1-35) and fetches its details.
- **API Integration**: Uses the Jikan API to retrieve episode synopses.
- **Flask Web App**: Displays the fetched episode and synopsis on a web page.

## How It Works
1. The `random` library generates a random number.
2. This number is used in the API endpoint:  
   `https://api.jikan.moe/v4/anime/{random_number}`.
3. The Flask app sends a GET request to the API and retrieves the episode and synopsis.
4. The results are presented in the browser.

## Installation and Usage
1. **Install required dependencies**:  
   `pip install flask requests`
2. **Run the Flask App**: To run the Flask app, execute the following command:  
   `python app.py`
3. **Access the App**: To access the app, open your browser and navigate to: [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Documentation  
Learn more about the Jikan API: [Jikan API Documentation](https://jikan.docs.apiary.io)

## License  
This project is for educational purposes only.





