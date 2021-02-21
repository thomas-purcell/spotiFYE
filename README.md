# spotiFYE

This project was completed at HackBeanpot 2021 by Rachel Li, Jacob Nguyen, Thomas Purcell, Jay Srinivasan, and Tri Watanasuparp.

spotiFYE looks at a Spotify user's top tracks and artists from a more recent time frame and compares it to a longer-term time frame. Running the flask file (app.py) generates the webpage that first prompts the user to sign into their Spotify account and authorize the access of their top tracks and artist information. The webpage shows what songs, artists, albums, and genres are in common from the user's short term and long term top tracks/artists, as well as the similiarity percentage. Each category is shown on an individual card, with one of the category's song or album cover image shown. Each category also has a progress bar representing the percentage similarity between the user's short-term and long-term top tracks/artists.

Backend engineering was done by Thomas Purcell and Rachel Li. The Spotify API was used, as well as the Spotipy library to retrieve information from the API and authorize the use of protected data. Flask was used to connect the comparison results to the front-end work.

Frontend engineering was done by Jacob Nguyen, Jay Srinivasan, and Tri Watanasuparp. HTML and CSS scripts were written to design and develop the web application. Bootstrap was used to build components of the web application. 