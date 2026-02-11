# Photo Gallery

A modern web-based photo gallery application built with Django, featuring user authentication, photo management, album creation, and social features like liking and tagging.

## Features

- **User Authentication**: Register, login, and manage user accounts
- **Photo Management**: Upload, view, and organize photos with descriptions and tags
- **Album Creation**: Create custom albums and group photos together
- **Social Features**: Like photos and interact with the community
- **Tag System**: Filter photos by tags for easy discovery
- **User Profiles**: Customize user profiles with bio and profile images
- **Cloud Storage**: Photos stored securely on Cloudinary
- **Responsive Design**: Works across desktop and mobile devices

## Tech Stack

| Component | Technology |
|-----------|-----------|
| **Backend** | Django 6.0.2 |
| **Database** | PostgreSQL |
| **Frontend** | HTML5, CSS3 |
| **Image Storage** | Cloudinary |
| **Web Server** | Gunicorn |
| **Static Files** | WhiteNoise |
| **Python Version** | 3.8+ |

## Prerequisites

- Python 3.8 or higher
- PostgreSQL installed and running
- Git
- Cloudinary account (for image storage)
- pip (Python package manager)

## Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/vicjam3s/photo-gallery.git
cd photo-gallery
```

### 2. Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory:

```env
SECRET_KEY=your-django-secret-key-here
DEBUG=True
DATABASE_URL=postgresql://user:password@localhost:5432/photo_gallery
CLOUDINARY_URL=cloudinary://api_key:api_secret@cloud_name
```

### 5. Create PostgreSQL Database

```bash
# Connect to PostgreSQL
psql -U postgres

# Create database
CREATE DATABASE photo_gallery;
\q
```

### 6. Run Migrations

```bash
python manage.py migrate
```

### 7. Create Superuser (Admin Account)

```bash
python manage.py createsuperuser
```

### 8. Collect Static Files

```bash
python manage.py collectstatic --noinput
```

### 9. Run Development Server

```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

## How to Use & Navigate

### Landing Page
- Navigate to the home page to see the landing/welcome page
- Unauthenticated users can browse the gallery

### Gallery
- **View All Photos**: Go to `/gallery/` to see all uploaded photos
- **Filter by Tags**: Click on tags to filter photos by category
- **View Photo Details**: Click on any photo to see full details, description, and tags

### Authentication
- **Register**: Create a new account at `/register/`
- **Login**: Access your account at `/login/`
- **Logout**: Click logout to end your session

### User Profile
- **Access Profile**: Logged-in users can visit `/profile/` (visible after login)
- **Edit Profile**: Add a bio and upload a profile picture
- **Update Bio**: Write a personal bio to share with others

### Photo Interaction
- **Like Photos**: Logged-in users can like photos on the photo detail page
- **Unlike Photos**: Click the like button again to unlike a photo

### Albums
- **View Albums**: Navigate to `/albums/` to see your personal albums
- **Create Album**: Click "Create Album" to make a new album
- **Add to Album**: From a photo detail page, add photos to your albums
- **View Album**: Click on an album to see all photos within it

##  Project Structure

```
photo-gallery/
├── manage.py                 # Django management script
├── requirements.txt          # Python dependencies
├── readme.md                 # This file
├── render.yaml              # Render deployment config
│
├── photogallery/            # Main project settings
│   ├── settings.py          # Django configuration
│   ├── urls.py              # URL routing
│   ├── wsgi.py              # WSGI configuration
│   └── asgi.py              # ASGI configuration
│
├── galleryapp/              # Main application
│   ├── models.py            # Database models (Photo, Album, Profile, etc.)
│   ├── views.py             # View logic
│   ├── urls.py              # App URL patterns
│   ├── forms.py             # Django forms
│   ├── admin.py             # Admin panel configuration
│   ├── signals.py           # Django signals
│   └── migrations/          # Database migrations
│
├── templates/               # HTML templates
│   ├── base.html           # Base template
│   ├── landing.html        # Landing page
│   ├── photo_list.html     # Photo gallery view
│   ├── photo_detail.html   # Individual photo view
│   ├── album_list.html     # User albums
│   ├── album_detail.html   # Album contents
│   ├── album_create.html   # Create album form
│   ├── profile.html        # User profile
│   ├── login.html          # Login page
│   └── registration.html   # Registration page
│
├── static/                  # Static files
│   └── css/
│       └── style.css       # Stylesheet
│
└── staticfiles/             # Collected static files (generated)
```

##  Key URL Routes

| Route | Purpose | Requires Login |
|-------|---------|---|
| `/` | Landing page | No |
| `/gallery/` | View all photos | No |
| `/photo/<id>/` | View photo details | No |
| `/login/` | User login | No |
| `/logout/` | User logout | Yes |
| `/register/` | Create new account | No |
| `/profile/` | View/edit user profile | Yes |
| `/albums/` | View user albums | Yes |
| `/albums/create/` | Create new album | Yes |
| `/albums/<id>/` | View album contents | Yes |
| `/photo/<id>/like/` | Like/unlike photo | Yes |

##  Database Models

### Profile
- User's extended profile with bio and profile image

### Photo
- Title, description, image, tags
- Uploaded by user
- Creation timestamp
- Associated likes

### Album
- Belongs to a user
- Contains multiple photos
- Creation timestamp

### Tag
- Used for categorizing photos
- Unique tag names

### Like
- Tracks which users liked which photos
- Unique per user-photo combination

##  Deployment

The project includes a `render.yaml` file for easy deployment on [Render](https://render.com/). Simply connect your GitHub repository to Render, and the deployment will be automated.

##  Security Notes

- Never commit `.env` files with real credentials to version control
- Change `SECRET_KEY` in `.env` for production
- Set `DEBUG=False` in production
- Use environment variables for sensitive data
- Ensure PostgreSQL is properly secured

##  License

This project is open source and available for personal and commercial use.

##  Author

Created by vicjam3s

##  Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests.

##  Support

For issues or questions, please open an issue on the GitHub repository.
