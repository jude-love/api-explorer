from database import SessionLocal, engine, Base, User, Product, Purchase, Complaint
import random
import string
from datetime import datetime, timedelta
from sqlalchemy.orm import sessionmaker

# Create the tables if they don't exist
# Base.metadata.create_all(bind=engine) # This is handled in database.py

# Create the table if it doesn't exist
Base.metadata.create_all(bind=engine)

# Create a session local class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def create_fake_user():
    """Generates fake user data."""
    name = ''.join(random.choices(string.ascii_letters, k=10))
    email = f"{name.lower()}@example.com"
    return {"name": name, "email": email}

def create_fake_product():
    """Generates fake product data."""
    name = ''.join(random.choices(string.ascii_letters, k=10))
    price = round(random.uniform(1.0, 1000.0), 2)
    return {"name": name, "price": price}

def create_fake_complaint():
    """Generates fake complaint text."""
    complaint_texts = ["Product was damaged upon arrival.", "Item did not match the description.", "Delivery was significantly delayed.", "Poor customer service when attempting to return.", "Received the wrong item.", "Product stopped working after a few uses."]
    return random.choice(complaint_texts)


if __name__ == "__main__":
    db = SessionLocal()
    try:
        # Add fake users
        for _ in range(20):
            fake_user_data = create_fake_user()
            fake_user = User(name=fake_user_data["name"], email=fake_user_data["email"])
            db.add(fake_user)
        db.commit()
        print("Successfully added 20 fake users.")

        # Add fake products
        products = []
        for _ in range(10):
            fake_product_data = create_fake_product()
            fake_product = Product(name=fake_product_data["name"], price=fake_product_data["price"])
            db.add(fake_product)
            products.append(fake_product)
        db.commit()
        print("Successfully added 10 fake products.")

        # Add fake purchases
        users = db.query(User).all()
        for _ in range(30):
            random_user = random.choice(users)
            random_product = random.choice(products)
            random_date = datetime.now() - timedelta(days=random.randint(1, 365))
            fake_purchase = Purchase(user_id=random_user.id, product_id=random_product.id, purchase_date=random_date)
            db.add(fake_purchase)
        db.commit()
        print("Successfully added 30 fake purchases.")

        # Add fake complaints
        purchases = db.query(Purchase).all()
        for _ in range(30):
            random_purchase = random.choice(purchases)
            fake_complaint_text = create_fake_complaint()
            fake_complaint = Complaint(purchase_id=random_purchase.id, complaint_text=fake_complaint_text, complaint_date=datetime.now() - timedelta(days=random.randint(1, 365)))
            db.add(fake_complaint)
        db.commit()
        print("Successfully added 30 fake complaints.")
    except Exception as e:
        db.rollback()
        print(f"An error occurred: {e}")
    finally:
        db.close()
