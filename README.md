# **News-Agency - Django-Based News Agency**

### **Overview**
**News-Agency** is a modern and dynamic news portal built using Django, allowing users to read and manage articles, and for journalists (or "Redactors") to create, edit, and manage their own articles with ease. The platform supports features like multiple topics, article publishing, and a professional user interface.


### **Features**

- **User Authentication**:
  - Custom user model extending `AbstractUser` for enhanced control over user roles.
  - Login and logout functionality for secure access.
  
- **CRUD Operations**:
  - Full Create, Read, Update, Delete (CRUD) support for articles (`Newspaper`).
  - Journalists can write and manage their articles with rich text support.

- **Topics and Categories**:
  - Articles are organized by categories (topics) for easier navigation and relevance.
  
- **Role-based Permissions**:
  - **Redactor**: Journalists or content creators who can write, edit, and manage their articles.

- **Responsive Design**:
  - The portal is designed to be responsive, ensuring an optimal reading experience across all devices.
  
- **Admin Panel**:
  - Django's built-in admin panel for managing users, articles, and other data.

---

### **Technologies Used**

- **Django** - Web framework powering the application.
- **SQLite/PostgreSQL** - The database management system (SQLite is used by default).
- **Tailwind CSS** - For styling, ensuring modern and responsive design.
- **Python 3.12** - Backend programming language.

---

### **Installation**

1. **Clone the repository:**
   ```bash
   git clone https://github.com/10kkyvl/News-Agency.git
   cd News-Agency
   ```

2. **Set up a virtual environment:**
   ```bash
   python -m venv .env
   source .env/bin/activate  # on Linux/macOS
   .\.env\Scripts\activate  # on Windows
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create `.env` file:**
   Create a `.env` file in the root directory and add your configuration values like:

   ```
   SECRET_KEY=your-secret-key-here
   DEBUG=True
   ```

5. **Set up the database:**
   - Run migrations to set up the database schema:
     ```bash
     python manage.py migrate
     ```

6. **Load sample data (fixtures):**
   - To load initial data for `Redactors`, `Topics`, and `Newspapers`, use the following command:
     ```bash
     python manage.py loaddata sample_data.json
     ```
   - This will populate your database with example users, articles, and topics.

7. **Create superuser (or use admin:admin from fixture):**
   ```bash
   python manage.py createsuperuser
   ```

8. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

   Your portal should now be running on `http://127.0.0.1:8000`.

---

### **Project Structure**

```
News-Agency/
│
├── agency/                     # Main app for articles and users
│   ├── migrations/             # Database migrations
│   ├── models.py               # Models (Redactor, Newspaper, Topic)
│   ├── views.py                # Views (for article CRUD operations)
│   ├── urls.py                 # URL routing for the app
│   ├── templates/              # Templates for the frontend
│   └── fixtures/               # Directory containing fixtures (sample data)
│       └── sample_data.json    # JSON fixture with sample users and articles
│
│
├── manage.py                   # Django management commands
├── requirements.txt            # List of dependencies
├── db.sqlite3                  # SQLite database file (or Postgres config)
└── README.md                   # Project documentation (this file)
```

---

### **Endpoints**

**later...**

---

### **Customization**

- **User Roles**: 
  The project is designed with a flexible user role system. The default role is `Redactor` for journalists. You can expand this system to include more roles such as admin, viewer, etc.

- **Styling**: 
  The project uses **Tailwind CSS** for styling. You can easily customize the look and feel by modifying the Tailwind configuration or overriding styles in `static/css`.

---

### **License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

### **Contact**

If you have any questions, feel free to reach out:

- **GitHub**: [https://github.com/10kkyvl](https://github.com/10kkyvl)

---