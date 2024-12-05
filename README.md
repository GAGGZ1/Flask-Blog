# Flask Blog Website

## Overview
Flask Blog is a web application that allows users to create, view, and manage blog posts. Users can register, log in, and perform various tasks such as creating posts, updating their profiles, and viewing posts from other users. The application is designed to be user-friendly and supports key features like pagination for better content organization.

---

## Features

### User Management
- **Registration**: Users can sign up by providing a username, email, and password.
- **Login/Logout**: Users can securely log in and log out of their accounts.
- **Password Reset**: Users can reset their passwords if forgotten.
- **Profile Management**: Users can update their username, email, and profile picture.

### Blog Functionality
- **Create Posts**: Users can write and publish blog posts.
- **Edit Posts**: Users can update the content of their posts.
- **Delete Posts**: Users can remove posts they no longer want.
- **View Posts**: 
  - All posts are displayed on the home page with pagination for better organization.
  - Users can view posts created by a specific user.
  - Posts can be browsed individually.

### Pages
- **Home Page**: Displays all blog posts with pagination for a clean and organized layout.
- **About Page**: A static page providing information about the website.

---

## Installation

### Prerequisites
- Python 3.8 or higher
- Flask (install via `pip install flask`)
- Flask extensions:
  - `Flask-SQLAlchemy` for database management
  - `Flask-Bcrypt` for secure password hashing
  - `Flask-Login` for user authentication
  - `Flask-WTF` for forms
  - `Flask-Mail` for password reset functionality (optional)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/GAGGZ1/Flask-Blog.git
   cd flask-blog
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up the database:
   ```bash
   flask db upgrade
   ```
4. Run the application:
   ```bash
   flask run
   ```
5. Access the app in your browser at `http://127.0.0.1:5000/`.

---

## Usage
1. **Register**: Create an account to access the platform's features.
2. **Log In**: Use your credentials to log in and manage your blog.
3. **Create a Post**: Navigate to the "New Post" section to publish your content.
4. **Manage Your Profile**: Update your details and upload a profile picture from the "Account" section.
5. **Explore Posts**: Browse all posts on the home page or view posts by specific users.

---

## Screenshots
<img width="1512" alt="Screenshot 2024-12-06 at 12 56 08 AM" src="https://github.com/user-attachments/assets/2ecb731d-7f2a-4d8c-a45b-c3daa4d202f8">
<img width="1512" alt="Screenshot 2024-12-06 at 12 56 25 AM" src="https://github.com/user-attachments/assets/3dffc669-7416-4f30-ab11-c4ee21edde42">
<img width="1512" alt="Screenshot 2024-12-06 at 12 56 35 AM" src="https://github.com/user-attachments/assets/958f69a1-e6ca-400a-b2f0-d19277f3b3fc">


---

## Technologies Used
- **Backend**: Flask
- **Database**: SQLite (or PostgreSQL/MySQL for production)
- **Frontend**: HTML, CSS, Bootstrap
- **Authentication**: Flask-Login and Flask-Bcrypt
- **Email Integration**: Flask-Mail (for password resets)

---

## Future Improvements
- Add post categories and tags for better filtering.
- Implement a rich text editor for post creation.
- Introduce comment functionality for posts.
- Enhance the search functionality for posts and users.

---

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature/bug fix.
3. Commit your changes and push to the branch.
4. Open a pull request.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

## Contact
For questions or suggestions, please reach out to [chauhangagan117@gmail.com].
```
