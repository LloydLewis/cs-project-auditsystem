"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'audit_system.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # If no command is provided, automatically start the Django server
    if len(sys.argv) == 1:
        sys.argv.append("runserver")

    # Ensure 'runserver' is appended before setting the IP address
    if "runserver" in sys.argv and "127.0.0.1:8000" not in sys.argv:
        sys.argv.append("127.0.0.1:8000")  # Bind to localhost explicitly

    # Prevent Django from auto-reloading in case of issues with PyInstaller
    if "runserver" in sys.argv:
        sys.argv.append('--noreload')

    execute_from_command_line(sys.argv)

    # Keeps the window open to view errors
    input("\nPress Enter to exit...")


if __name__ == "__main__":
    main()
