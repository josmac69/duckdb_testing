import csv
import random
import datetime
import os

def generate_csv(target_size_gb):
    target_size_bytes = target_size_gb * 1024 ** 3  # Convert GB to bytes
    output_file = f'table2_data_{target_size_gb}.csv'
    print(f'Generating {target_size_gb} GB of data to {output_file}')
    
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        
        # Write the header row
        writer.writerow([
            'measurement_id',
            'probe_id',
            'measurement_time',
            'temperature',
            'pressure',
            'humidity',
            'voltage',
            'current',
            'resistance',
            'sample_rate'
        ])

        file_size = csvfile.tell()
        row_count = 0
        
        while file_size < target_size_bytes:
            # Generate random data for each column
            measurement_id = row_count + 1
            probe_id = random.randint(1, 1000)
            measurement_time = datetime.datetime.now() - datetime.timedelta(seconds=random.randint(0, 1000000))
            temperature = round(random.uniform(-50, 50), 2)
            pressure = round(random.uniform(900, 1100), 2)
            humidity = round(random.uniform(0, 100), 2)
            voltage = round(random.uniform(0, 5), 2)
            current = round(random.uniform(0, 10), 2)
            resistance = round(random.uniform(0, 10000), 2)
            sample_rate = random.randint(1, 1000)
            
            # Write the row to the CSV file
            writer.writerow([
                measurement_id,
                probe_id,
                measurement_time.strftime('%Y-%m-%d %H:%M:%S'),
                temperature,
                pressure,
                humidity,
                voltage,
                current,
                resistance,
                sample_rate
            ])
            
            row_count += 1
            
            # Update the file size every 1000 rows
            if row_count % 1000 == 0:
                csvfile.flush()
                file_size = os.stat(output_file).st_size
                print(f'Generated {row_count} rows, file size: {file_size / (1024 ** 3):.2f} GB', end='\r')
    
    print(f'\nFinished generating {row_count} rows, total file size: {file_size / (1024 ** 3):.2f} GB')

if __name__ == '__main__':
    generate_csv(50)  # Change the number to the desired size in GB
