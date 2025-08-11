# Bookstore Django Project

## Overview
This is a **Bookstore** web application built with Django framework. It serves as an online platform to manage notebooks with detailed information and rich features. The project is designed to be simple yet extensible, allowing users to add notebooks with comprehensive details and maintain a basic catalog of books.

---

## Features

### Notebooks
- Add notebooks with rich details such as brand, pages, size, type, price, description, and story/notes.
- Upload cover images for notebooks for a visually appealing catalog.
- Detailed notebook view page to showcase all notebook information clearly.
- Notebook list page displays all notebooks along with their cover images and price tags.
- Form inputs are validated and styled with a consistent, user-friendly design.


### User Authentication (Planned / Recommended)
- Login and signup pages with secure authentication.
- Welcome page prompting users to login or signup.
- User session management for personalized experiences.

---

## Design & UI
- The project uses a consistent CSS styling theme featuring dark backgrounds with glowing blue highlights to create a modern, sleek look.
- Forms and pages have been styled with careful attention to readability and ease of use.
- Responsive layouts are maintained using flexible box layouts and semantic HTML.
- Notebook pages include cover images with fallback default images for notebooks without uploaded covers.
- Buttons and inputs are styled uniformly for intuitive user interaction.

---

## Project Structure

- `myapp/` – Main Django app containing models, views, forms, templates, static files (CSS).
- `myproject/` – Django project configuration including settings, URLs, and WSGI.
- `templates/` – HTML templates for notebook list/detail, add notebook, login, signup, and home/welcome pages.
- `static/` – CSS files for styling the application.
- `media/` – Folder (should be created) to store uploaded notebook cover images.
- `db.sqlite3` – SQLite database storing project data.

---

