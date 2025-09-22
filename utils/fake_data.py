from faker import Faker
import time
import random

fake = Faker('pt_BR')

class FakeDataGenerator:
    @staticmethod
    def generate_unique_user_data():
        timestamp = int(time.time())
        random_id = random.randint(1000, 99999)
        random_string = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=6))
        
        return {
            'email': f'test{timestamp}{random_id}{random_string}@fake.email',
            'name': f'{fake.first_name()} {fake.last_name()} {random_id}',
            'password': f'Test{random_id}@{random_string}123'
        }