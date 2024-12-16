# Twitter User Data Scraper

This task given to me by Banao as a second shortlisting task. This script uses the Tweepy library to scrape Twitter user data from a list of links.
It extracts the **username**, **bio**, **following count**, **followers count**, **location**, and **website** from each user's profile.
The data is then written to a CSV file.

### Requirements

- Tweepy library
- pandas library
- csv library
- urllib library
- dotenv library
- Twitter API credentials (API key, API secret, access token, access token secret, bearer token)

### Usage

- Clone the repository:

```bash
git clone https://github.com/mfonekpo/banao-scraping-2-.git
```
- Install the required modules
  
```bash
python3 -m pip install -r requirements.txt
```
- Run the script:

```bash
python xScraper.py
```

1. Create a `.env` file in the same directory as the script and add the following lines:
2. Replace the placeholder values in the `.env` file with your actual Twitter API credentials.

3. Place a CSV file named `twitter_links.xlsx` in a directory named `datafile` in the same directory as the script. The CSV file should contain a column named `Links` with Twitter links.

4. Run the script using Python:
5. The script will create a CSV file named `users_data.csv` in the same directory.

### Code Structure

The code is organized into several functions:

- `read_csv(data_file="./datafile/twitter_links.xlsx")`: Reads a CSV file containing Twitter links and returns a list of links.
- `get_username(links)`: Extracts the username from a Twitter link.
- `get_user_data(username)`: Retrieves Twitter user data using the Tweepy client.
- `extract_information(user)`: Extracts relevant information from a Twitter user object.
- `write_to_csv(data, filename="users_data.csv")`: Writes user data to a CSV file.
- `main()`: Main function that runs the script.

### Example Output

The resulting CSV (products.csv) will look like this:
| Bio | Following_Count | Followers_Count | Location | Website|
|---|---|---|---| ---|
| user_1 | 499 | 4 | USA | https://user1/site1
| user_2 | 1299 | 400 | India | NaN

### License

There is no License for this product. This product is strictly for learning purposes

### Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.

### Authors

- Mfon Nsikak Ekpo

### Acknowledgements

- Tweepy library
- pandas library
- csv library
- urllib library
- dotenv library
- Banao

-----
### Demo Video

A short demonstration video is included, explaining the script's functionality and showing how it runs. The video was submitted to the instructor as a grading criteria

# Note:
There are two scripts in this repository. The first one is the `selenium_scraper.py` which is the modified script, and the second one is the `xScraper.py` which is the one used in the demo video.
