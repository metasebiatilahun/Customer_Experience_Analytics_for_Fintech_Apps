import psycopg2
import csv
import traceback

# Database connection details - USE THESE IN ALL CONNECTIONS
DB_CONFIG = {
    'host': 'localhost',
    'database': 'bank_reviews',
    'user': 'user_admin',      # Make sure this is correct
    'password': 'admin1234',   # Your actual password
    'port': '5432'
}

def test_connection():
    """Test database connection with correct credentials"""
    try:
        print("Testing database connection...")
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()
        
        # Test query
        cursor.execute("SELECT version();")
        db_version = cursor.fetchone()
        print(f"✓ Connected to PostgreSQL: {db_version[0]}")
        
        # Check current user
        cursor.execute("SELECT current_user;")
        current_user = cursor.fetchone()
        print(f"✓ Connected as user: {current_user[0]}")
        
        cursor.close()
        conn.close()
        return True
        
    except psycopg2.OperationalError as e:
        print(f"❌ Connection failed: {e}")
        print("\nTroubleshooting steps:")
        print("1. Check if PostgreSQL is running: `sudo service postgresql status`")
        print("2. Verify username/password")
        print("3. Check if user 'user_admin' exists: `psql -U postgres -c \"\\du\"`")
        print("4. Test connection as postgres: `psql -U postgres -h localhost`")
        return False

def fix_user_permissions():
    """Create user_admin if it doesn't exist"""
    try:
        # Connect as postgres first to create the user
        postgres_conn = psycopg2.connect(
            host='localhost',
            database='postgres',
            user='postgres',
            password='Ora12cesw!'  # Default postgres password
        )
        postgres_cursor = postgres_conn.cursor()
        
        # Check if user_admin exists
        postgres_cursor.execute("SELECT 1 FROM pg_roles WHERE rolname='user_admin';")
        if not postgres_cursor.fetchone():
            print("Creating user 'user_admin'...")
            postgres_cursor.execute("CREATE USER user_admin WITH PASSWORD 'admin1234';")
            postgres_cursor.execute("ALTER USER user_admin CREATEDB;")
            print("✓ Created user_admin")
        else:
            print("✓ user_admin already exists")
        
        # Grant permissions on bank_reviews database
        postgres_cursor.execute("GRANT ALL PRIVILEGES ON DATABASE bank_reviews TO user_admin;")
        
        postgres_conn.commit()
        postgres_cursor.close()
        postgres_conn.close()
        print("✓ Granted permissions to user_admin")
        
    except Exception as e:
        print(f"Note: Could not create user_admin: {e}")
        print("You may need to use 'postgres' user instead")

def main():
    """Main insertion script with pure psycopg2"""
    
    print("=" * 60)
    print("BANK REVIEWS DATA INSERTION")
    print("=" * 60)
    
    # Step 1: Test connection
    if not test_connection():
        print("\nTrying to fix permissions...")
        fix_user_permissions()
        
        # Try again with postgres user as fallback
        DB_CONFIG['user'] = 'user_admin'  # Change this
        DB_CONFIG['password'] = 'admin1234'  # Change this
        
        if not test_connection():
            print("❌ Cannot connect to database. Exiting.")
            return
    
    # Step 2: Connect and insert data
    try:
        print("\n--- Connecting to database ---")
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()
        
        # Your existing insertion code here
        # ... (copy your bank_data and review_data loading) ...
        # ... (copy your insert_bank_data and insert_review_data functions) ...
        
        print("\n✓ Data insertion completed successfully!")
        
    except psycopg2.Error as e:
        print(f"\n❌ Database error: {e}")
        traceback.print_exc()
    except Exception as e:
        print(f"\n❌ General error: {e}")
        traceback.print_exc()
    finally:
        if 'conn' in locals():
            cursor.close()
            conn.close()
            print("\nDatabase connection closed.")

if __name__ == '__main__':
    main()