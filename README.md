# Medical Information Retrieval System in Amharic Language

## Project Overview
This project implements a Medical Information Retrieval System that supports Amharic language documents, enabling efficient search and retrieval of medical information for Amharic-speaking users.

## Live Demo
🌐 **Access the live application**: [Your App URL will be here after deployment]

## Features
- Amharic text preprocessing (tokenization, normalization, stop-word removal)
- TF-IDF based document indexing
- Vector Space Model for retrieval
- Cosine similarity for ranking
- Web-based user interface
- Performance evaluation metrics (Precision, Recall, F1-Score)

## System Architecture
```
User Interface → Query Processing → Retrieval Engine → Database
                      ↓
              Text Preprocessing → Indexing Module
```

## Quick Start (Local Development)
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/medical-ir-amharic.git
   cd medical-ir-amharic
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python app.py
   ```

4. Open your browser and go to: `http://localhost:8000`

## Deployment Options

### Option 1: Heroku (Recommended for Teachers)
1. Create a Heroku account at https://heroku.com
2. Install Heroku CLI
3. Deploy using the provided `Procfile` and `requirements.txt`

### Option 2: Railway
1. Connect your GitHub repository to Railway
2. Automatic deployment from main branch

### Option 3: Render
1. Connect GitHub repository
2. Use the provided configuration files

## Dataset
The system uses Amharic medical documents covering various health topics including:
- Medications and their properties (ቪታሚን C, ፓራሲታሞል, አሞክሲሲሊን, etc.)
- Symptoms and treatments
- Health guidelines
- Medical terminology

## Evaluation
The system is evaluated using standard IR metrics:
- Precision: Proportion of retrieved documents that are relevant
- Recall: Proportion of relevant documents that are retrieved
- F1-Score: Harmonic mean of precision and recall

## Technologies Used
- Python 3.8+
- Flask (Web framework)
- Whoosh (Search engine library)
- Pandas (Data manipulation)
- NumPy (Numerical operations)
- Gunicorn (Production server)

## Project Structure
```
medical_ir_amharic/
├── app.py                 # Main Flask application
├── wsgi.py               # WSGI entry point for deployment
├── Procfile              # Heroku deployment configuration
├── requirements.txt      # Python dependencies
├── src/                  # Source code modules
│   ├── data_processor.py
│   ├── indexer.py
│   ├── evaluator.py
│   └── ...
├── templates/            # HTML templates
│   ├── index.html
│   ├── search_results.html
│   └── ...
└── index/               # Search index files
```

## Usage
1. **Search**: Enter Amharic medical terms in the search box
2. **Browse Results**: View ranked search results with relevance scores
3. **Document Details**: Click on any result to view full document information
4. **Statistics**: Check system performance and document statistics

## Sample Searches (Try These)
- `ፓራሲታሞል` (Paracetamol)
- `ህመም` (Pain)
- `አንቲባዮቲክ` (Antibiotic)
- `የስኳር መድሃኒት` (Diabetes medicine)

## API Endpoints
- `GET /` - Home page
- `POST /search` - Search interface
- `GET /api/search?q=query` - JSON API for search
- `GET /statistics` - System statistics
- `GET /document/<id>` - Document details

## Contributors
- [Your Name] - Developer

## License
This project is licensed under the MIT License.