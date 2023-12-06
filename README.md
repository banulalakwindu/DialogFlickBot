# BluRay-Bot 🎬🤖

BluRay-Bot is a movie purchasing and information retrieval system that uses Dialogflow for natural language processing (NLP), Python for backend development, and MySQL for database management. It's designed to handle two main tasks: buying a movie and retrieving details about a movie.

## Technologies/Languages Used

- **Dialogflow:** Used for natural language processing to understand user intents and facilitate interactive conversations.
- **Python:** Used for backend development to process user requests, interact with the database, and handle business logic.
- **MySQL:** Used for data storage to store information related to movie orders and details.
- **The Movie DB:** If the movie is not in the database, details will be retrieved from the API.

## Tasks

### 1. Buy a Movie 💳

#### Workflow:

- **User Interaction:**
  The user initiates a conversation expressing an intent to buy a movie.
- **Dialogflow NLP:**
  Dialogflow processes the user's input, identifies intents, and extracts relevant information.
- **Python Backend Processing:**
  The backend handles the business logic related to movie purchases.
- **MySQL Database Interaction:**
  The backend communicates with the MySQL database to store order details.
- **Response to User:**
  BluRay-Bot provides a confirmation to the user, including order details.

#### Example:

User: "I want to buy the movie."

BluRay-Bot: "Great choice! To assist you better, please provide the name of the movie you'd like to buy, the type (DVD or Blu-ray), and the quantity."

User: "I want to buy Pathaan Blu-ray disks."

BluRay-Bot: "How many items do you want to buy?"

User: "Five."

BluRay-Bot: "Confirm Order Movie Name – Pathaan Disk Type – Blu-Ray Quantity - 5"

User: "Yes, Confirm."

BluRay-Bot: "Awesome. We have placed your order." 🎉

### 2. Get Details about a Movie 🎥

#### Workflow:

- **User Interaction:**
  The user asks BluRay-Bot for details about a specific movie.
- **Dialogflow NLP:**
  Dialogflow processes the user's request, identifies the intent to get movie details, and extracts the movie title.
- **Python Backend Processing:**
  The backend retrieves relevant information from the MySQL database based on the requested movie title.
- **Response to User:**
  BluRay-Bot provides details about the requested movie, including its age-group, story line, and release date.

#### Example:

User: "Tell me about the movie."

BluRay-Bot: "Which movie do you want to know?"

User: "Pathaan."

BluRay-Bot: "You can buy this movie from our Store. Pathaan is a PG-13 movie released in 2022. IMDB rating is 8.5/10. Story Line: [Movie Story Line]."

_If the movie is not in the database:_

BluRay-Bot: "This movie is not found in our store. Below are the details I retrieved from TMDB website, and I will request to admins to add this movie to the store. [TMDB Movie Details]."

## Running the Project

1. Install dependencies:

   ```bash
   pip install mysql-connector-python
   pip install fastapi[all]
   ```

2. Run the Backend:

   ```bash
    uvicorn main:app --reload
   ```

3. Run ngrok:

   ```bash
   ngrok http 8000

   ```

4. Copy the HTTPS address from ngrok and set it as the Dialogflow webhook.

## Live Demo

Check out the live demo on the [BluRay-Bot GitHub Page](https://banulalakwindu.github.io/DialogFlickBot/).

Feel free to customize the content further based on your preferences!
