"""
QUICK START GUIDE - LUXA Luxury Watches eCommerce

This script will help you get the application up and running quickly.
"""

import os
import sys
import subprocess

def print_header(title):
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}\n")

def print_section(title):
    print(f"\n>>> {title}")

def run_command(command, description):
    """Run a shell command and handle errors."""
    print(f"  {description}...", end=" ")
    try:
        subprocess.run(command, shell=True, check=True, capture_output=True)
        print("✓")
        return True
    except subprocess.CalledProcessError as e:
        print("✗")
        print(f"  Error: {e}")
        return False

def main():
    print_header("LUXA LUXURY WATCHES - QUICK START")
    
    # Check Python version
    print_section("Checking Python version")
    if sys.version_info < (3, 8):
        print("  ✗ Python 3.8 or higher is required")
        sys.exit(1)
    print(f"  ✓ Python {sys.version.split()[0]} detected")
    
    # Check if venv exists
    print_section("Checking virtual environment")
    venv_path = "venv"
    if os.path.exists(venv_path):
        print(f"  ✓ Virtual environment found at {venv_path}")
    else:
        print(f"  Virtual environment not found. Creating...")
        if sys.platform == "win32":
            run_command("python -m venv venv", "Creating virtual environment")
        else:
            run_command("python3 -m venv venv", "Creating virtual environment")
    
    # Activate venv and install dependencies
    print_section("Installing dependencies")
    if sys.platform == "win32":
        activate_cmd = "venv\\Scripts\\activate.bat && "
    else:
        activate_cmd = "source venv/bin/activate && "
    
    run_command(f"{activate_cmd}pip install --upgrade pip", "Upgrading pip")
    run_command(f"{activate_cmd}pip install -r requirements.txt", "Installing packages")
    
    # Create .env file
    print_section("Setting up environment")
    if not os.path.exists(".env"):
        if os.path.exists(".env.example"):
            import shutil
            shutil.copy(".env.example", ".env")
            print("  ✓ Created .env file from template")
        else:
            print("  ! .env.example not found, skipping")
    else:
        print("  ✓ .env file already exists")
    
    # Initialize database
    print_section("Setting up database")
    print("  Initializing database...")
    if sys.platform == "win32":
        run_command(f"{activate_cmd}python run.py init-db", "Initializing database")
        run_command(f"{activate_cmd}python run.py seed-db", "Seeding sample products")
        run_command(f"{activate_cmd}python run.py create-admin", "Creating admin user")
    else:
        run_command(f"{activate_cmd}python run.py init-db", "Initializing database")
        run_command(f"{activate_cmd}python run.py seed-db", "Seeding sample products")
        run_command(f"{activate_cmd}python run.py create-admin", "Creating admin user")
    
    # Display completion message
    print_header("SETUP COMPLETE!")
    print("✓ LUXA is ready to run!\n")
    
    print("Next steps:")
    print("-" * 60)
    print("1. Start the development server:")
    
    if sys.platform == "win32":
        print("   venv\\Scripts\\activate.bat")
        print("   python run.py")
    else:
        print("   source venv/bin/activate")
        print("   python run.py")
    
    print("\n2. Open your browser and visit:")
    print("   http://localhost:5000")
    
    print("\n3. Admin credentials:")
    print("   Email: admin@luxurywatches.com")
    print("   Password: admin123")
    
    print("\n4. Change admin password immediately in production!")
    print("-" * 60)
    
    print("\n📖 For more information, see README.md")
    print("🎨 Customize the site in app/templates and app/static\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nSetup cancelled by user.")
        sys.exit(0)
