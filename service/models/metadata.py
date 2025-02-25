class Metadata:
    title = "Resting Metabolic Rate (RMR) API"
    description = """
    A RESTful API for calculating Resting Metabolic Rate using Mifflin-St. Jeor
    equations.
    """
    summary = """
    A RESTful API for calculating Resting Metabolic Rate using Mifflin-St. Jeor
    equations. This is a simple API that can be used to:
    - Calculate a single RMR value
    - Calculate RMR over a time projection
    """
    version = "0.0.1"
    contact = {
        "name": "yifattih",
        "url": "https://github.com/yifattih",
        "email": "yifattih@protonmail.com",
    }
    license_info = {
        "name": "Apache 2.0",
        "identifier": "MIT",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    }
    tags = [
        {"name": "Root", "description": "Home page endpoint"},
        {
            "name": "RMR",
            "description": "Endpoint to calculate Resting Metabolic Rate (RMR)",
            "externalDocs": {
                "description": "Mifflin-St. Jeor equations",
                "url": "https://www.ncbi.nlm.nih.gov/books/NBK278991/table/diet-treatment-obes.table12est/",
            },
        },
        {"name": "Health", "description": "Health-check endpoint"},
    ]
