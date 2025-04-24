# RT-Project

## Overview
The **RT-Project** project is a full-stack application designed for planning trips and managing travel-related tasks. It is implemented using **Flask** for the backend and **HTML, CSS, JavaScript** for the frontend. Users can register, log in, plan a trip, and calculate expenses with ease.

This project is a simple travel assistant that allows users to plan their trips, manage their expenses, and store travel-related data.

## Features

- **User Registration and Login:** Secure user authentication system using HTML forms.
- **Trip Planning:** Users can input their travel details such as destination, budget, number of travelers, and days.
- **Expense Management:** Users can manage travel-related expenses like food, shopping, and hotels.
- **Itinerary Generator:** Generate a trip itinerary based on preferences and inputs.
- **Responsive Design:** The project uses a responsive layout for mobile and desktop views.

## Installation

### Prerequisites
1. Python 3.7+ (for running the backend with Flask)
2. A text editor like Visual Studio Code or Sublime Text.
3. A modern web browser to run the frontend.

### Steps to Set Up the Project

1. Clone the repository:
    ```bash
    git clone <repository_url>
    ```

2. Navigate into the project folder:
    ```bash
    cd RT-Project
    ```

3. Install Flask:
    ```bash
    pip install Flask
    ```

4. To start the server, run the `app.py` file:
    ```bash
    python app.py
    ```

5. Visit `http://127.0.0.1:5000` in your web browser to access the application.

## File Structure

```bash
RT-Project/
├── app.py               # Backend Flask application
├── templates/           # HTML templates
│   ├── register.html    # Registration page
│   ├── login.html       # Login page
│   ├── trip.html        # Trip planning page
│   └── expense.html     # Expense management page
├── static/              # Static files (CSS, JS, images)
│   ├── styles.css       # CSS for styling
│   ├── script.js        # JavaScript file
│   └── images/          # Images folder
└── README.md            # Project documentation
```

## Contributing

Feel free to fork the repository, make improvements, and submit a pull request. If you find any bugs or issues, please open an issue in the GitHub repository.

## License

This project is open-source and available under the MIT License. See the LICENSE file for more details.

