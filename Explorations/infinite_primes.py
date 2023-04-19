import sqlite3
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0: return False
    return True

if __name__ == "__main__":
    conn = sqlite3.connect('Explorations/primes.db')
    c = conn.cursor() # Connection object

    c.execute('''CREATE TABLE IF NOT EXISTS numbers
             (number INTEGER, is_prime INTEGER)''')

    # Insert number 1 into the table and mark it as not prime
    # Ignores, if DB already contains first row
    c.execute("INSERT OR IGNORE INTO numbers (number, is_prime) VALUES (?, ?)", (1, 0))
    conn.commit()

    while True:
        c.execute("SELECT * FROM numbers ORDER BY number DESC LIMIT 1")
        last_row = c.fetchone()

        new_number = last_row[0] + 1
        is_prime_val = 1 if is_prime(new_number) else 0 # Ternary conditional operator

        c.execute("INSERT INTO numbers (number, is_prime) VALUES (?, ?)", (new_number, is_prime_val))
        print(f'Created row for {new_number}, Prime: {is_prime_val==1}')
        conn.commit()