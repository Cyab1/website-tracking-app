# Website Tracking App

# 📊 Website Tracking App

This project is a simple website tracking system built with Django and JavaScript. It tracks user interactions, including page loads, clicks, and time spent on the website.

## 🚀 Features

- Track page views
- Track user clicks on elements
- Track time spent on a webpage
- Send event data to a Django backend

## 🛠️ Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/Cyab1/website-tracking-app.git
   cd website-tracking-app

   ```

2. Create and activate a virtual environment:

```sh
python -m venv venv
source venv/bin/activate # For Mac/Linux
venv\Scripts\activate # For Windows

```

3. Install dependencies:

```sh
pip install -r requirements.txt
```

4. Run migrations:

```sh
python manage.py migrate
```

5 Start the server:

```sh
python manage.py runserver
```

6. Add the JavaScript tracker to your HTML file:

```html
<script src="public/tracker.js"></script>
```

Tracking Example
The tracker script (tracker.js) sends events to the Django backend using fetch().

js
window.addEventListener('load', () => sendEvent('page_load'));
document.addEventListener('click', (event) => {
sendEvent('click', { element: event.target.tagName });
});

🤝 Contributing
Feel free to fork this repo, open issues, or submit PRs.

📜 License
This project is licensed under the MIT License.
