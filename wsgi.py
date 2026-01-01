"""
WSGI entry point for production deployment
"""

import os
import sys

# Add current directory to path
sys.path.insert(0, os.path.dirname(__file__))

from app import app

if __name__ == "__main__":
    # For local development
    port = int(os.environ.get('PORT', 5000))
    host = os.environ.get('HOST', '0.0.0.0')
    
    app.run(
        host=host,
        port=port,
        debug=os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    )