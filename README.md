# PearTrade

PearTrade is an e-commerce platform that enables users to buy and sell products. Users can sign in, browse items by category or name, chat with sellers for additional details, and manage their personal dashboards to add, edit, or delete items.

## Features

- **User Authentication**: Sign up, log in, and log out via social authentication.
- **Dashboard**: Personal dashboards for users to manage their items.
- **Browse and Search**: Browse products by category (Furniture, Clothes, Groceries) or search by name.
- **Product Listings**: Add, edit, delete, and view product details.
- **Chat System**: Buyers and sellers can chat about products.
- **Responsive Design**: Optimized for a seamless user experience on all devices.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/peartrade.git
   cd peartrade
   ```

2. Set up a virtual environment and install dependencies:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   pip install -r requirements.txt
   ```

3. Set up the database:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   ```

6. Access the application at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Usage

### Buyer Workflow:
1. Browse products by category or search by name.
2. View product details.
3. Initiate a chat with the seller for additional details.
4. Purchase the desired product.

### Seller Workflow:
1. Log in to your account.
2. Access the dashboard to add, edit, or delete items.
3. Respond to buyer inquiries through the chat system.

## File Structure

- **core**: Handles user authentication, homepage, and static pages like About and Privacy.
- **conversation**: Manages the chat system between buyers and sellers.
- **item**: Manages product listings, including adding, editing, and browsing items.

## Technologies Used

- **Backend**: Django 4.x
- **Frontend**: HTML, CSS
- **Database**: SQLite (default, can be replaced with PostgreSQL or MySQL)
- **Authentication**: Django's built-in authentication system with social login.

## Contributing

Contributions are welcome! Follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
   ```bash
   git checkout -b feature/your-feature
   ```
3. Commit your changes.
   ```bash
   git commit -m "Add your message here"
   ```
4. Push to your branch.
   ```bash
   git push origin feature/your-feature
   ```
5. Create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For any inquiries, feel free to reach out:

- **Email**: tadesseabel26@gmai.com
- **GitHub**: [https://github.com/abimatd](https://github.com/abimatd)

