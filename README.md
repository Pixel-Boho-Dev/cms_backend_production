# ALSI CMS BACKEND

CMS Backend for the ALSI project done by PixelBoho

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/pixel-boho/cms_backend.git
    ```

2. Navigate to the project directory:

    ```bash
    cd cms_backend
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Configure Django settings:

    - Copy `.env.example` to `.env` and configure your environment variables.
    - Modify `settings.py` as needed for your environment (database settings, secret key, etc.).

5. Apply migrations:

    ```bash
    python manage.py migrate
    ```

6. Create a superuser (optional):

    ```bash
    python manage.py createsuperuser
    ```

## Usage

1. Start the development server:

    ```bash
    python manage.py runserver
    ```

2. Open a web browser and go to `http://localhost:8000` to view the application.

3. Access the Django admin interface at `http://localhost:8000/admin` (if a superuser is created).

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/my-feature`.
3. Make your changes and commit them: `git commit -am 'Add new feature'`.
4. Push to the branch: `git push origin feature/my-feature`.
5. Submit a pull request.

## License

[License](LICENSE)
