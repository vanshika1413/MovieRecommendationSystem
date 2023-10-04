# MovieRecommendationSystem
911 Movies offers entertainment insights for film enthusiasts, aiding in movie exploration and selection. Designed for personalized recommendations, it suggests, reviews, rates, and filters movies, providing reading materials and links based on user preferences, enhancing the movie-watching experience.

# 911 Movies - Movie Recommendation System

## Project Author
- Vanshika Nijhawan

## Project Overview
911 Movies is a Python-based project designed to provide movie recommendations and information to users. The system allows users to explore, review, rate, and discuss movies, helping others in the community receive better movie recommendations.

## Hardware Specifications
- Intel Core i5 processor (Windows and macOS supported)
- Minimum of 1 GB RAM

## Software Specifications
- Python 3.8.7
- PySimpleGUI
- MySQL Connector for Python
- MySQL Database

## Project Objective
The objective of 911 Movies is to serve as a source of entertainment information with features designed to assist movie enthusiasts in exploring the world of movies and deciding what to watch. It acts as an online database related to films where users can find information about their favorite movies, engage with other movie buffs, and receive movie recommendations based on their preferences and reviews from the community.

## Project Features
- **User-friendly Interface:** Easy to navigate and use.
- **Movie Information:** Provides details like name, genre, language, duration, and release year of movies.
- **Movie Recommendations:** Offers top movie recommendations based on reviews and ratings by users.
- **Movie Reviews:** Users can read and write reviews for movies.
- **Filtering:** Allows users to filter movies based on genre and language.
- **Admin Panel:** Admins can update, delete, or add movie details.

## How It Works
1. Users can enter a movie name in the text box.
2. If the movie exists in the database, it gets highlighted, and users can check its details.
3. Users can filter movies based on genre and language.
4. Top movie recommendations are displayed based on reviews and ratings.
5. Users can read and write reviews for selected movies.
6. Admins have special privileges to manage movie details and user accounts.

## Code Structure
The code is structured into various modules, each serving a specific functionality in the application. Some of the main modules include:
- `Mainform`: The main module driving the application.
- `moviereviewwrite`: Module to handle writing of movie reviews.
- `moviereviewread`: Module to handle reading of movie reviews.
- `movies`: Module managing movie information.
- `signinsignup`: Module handling user sign-in and sign-up processes.
- `adminsigninsignup`: Module for admin sign-in and sign-up functionalities.

## Usage
To use the 911 Movies application, users need to have Python and the necessary libraries installed on their system. After installation, users can run the `Mainform` module to start the application.

