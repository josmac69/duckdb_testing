import csv
import random
import string
import uuid
import datetime
import os

def generate_csv(target_size_gb):
    target_size_bytes = target_size_gb * 1024 ** 3  # Convert GB to bytes
    output_file = f'data_{target_size_gb}.csv'
    
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        
        # Write the header row
        writer.writerow([
            'user_id',
            'first_name',
            'last_name',
            'email',
            'signup_date',
            'last_login',
            'is_active',
            'account_balance',
            'country_code',
            'favorite_number',
            'profile_text',
            'checksum'
        ])

        file_size = csvfile.tell()
        row_count = 0
        
        while file_size < target_size_bytes:
            # Generate random data for each column
            user_id = row_count + 1
            first_name = ''.join(random.choices(string.ascii_letters, k=random.randint(3, 10)))
            last_name = ''.join(random.choices(string.ascii_letters, k=random.randint(3, 10)))
            email = f'{first_name.lower()}.{last_name.lower()}{user_id}@example.com'
            signup_date = datetime.datetime.now() - datetime.timedelta(days=random.randint(0, 1000))
            delta_days = (datetime.datetime.now() - signup_date).days
            last_login = signup_date + datetime.timedelta(days=random.randint(0, max(0, delta_days)))
            is_active = random.choice([True, False])
            account_balance = round(random.uniform(0, 10000), 2)
            country_code = random.choice(['US', 'CA', 'GB', 'FR', 'DE', 'JP', 'CN', 'IN', 'BR', 'AU'])
            favorite_number = random.randint(1, 100)
            profile_text = ''.join(random.choices(
                string.ascii_letters + string.digits + ' ',
                k=random.randint(20, 200)
            ))
            checksum = str(uuid.uuid4())
            
            # Write the row to the CSV file
            writer.writerow([
                user_id,
                first_name,
                last_name,
                email,
                signup_date.strftime('%Y-%m-%d %H:%M:%S'),
                last_login.strftime('%Y-%m-%d %H:%M:%S'),
                is_active,
                account_balance,
                country_code,
                favorite_number,
                profile_text,
                checksum
            ])
            
            row_count += 1
            
            # Update the file size every 1000 rows
            if row_count % 1000 == 0:
                csvfile.flush()
                file_size = os.stat(output_file).st_size
                print(f'Generated {row_count} rows, file size: {file_size / (1024 ** 3):.2f} GB', end='\r')
    
    print(f'\nFinished generating {row_count} rows, total file size: {file_size / (1024 ** 3):.2f} GB')

if __name__ == '__main__':
    generate_csv(100)  # Change the number to the desired size in GB
