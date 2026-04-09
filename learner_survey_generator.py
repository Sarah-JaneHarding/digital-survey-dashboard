import pdfkit

# Function to generate a learner survey PDF

def generate_learner_survey():
    survey_data = {
        'Heading': {'en': 'Learner Survey', 'af': 'Leerling Opname', 'zu': 'Ingcwadi Yokufunda'},
        'Questions': [
            {
                'question': {'en': 'Do you own a device?', 'af': 'Besit jy 'n toestel?', 'zu': 'Uthanda umshini?'},
                'options': ['Yes', 'No']
            },
            {
                'question': {'en': 'Do you work independently or supervised?', 'af': 'Werk jy onafhanklik of onder toesig?', 'zu': 'Usebenza ungazenzisi noma uphansi kwenkokheli?'},
                'options': ['Independently', 'Supervised']
            },
            {
                'question': {'en': 'Do you have internet access?', 'af': 'Het jy toegang tot die internet?', 'zu': 'Unokufinyelela kwi-inthanethi?'},
                'options': ['Yes', 'No']
            },
            {
                'question': {'en': 'Which websites/apps/games do you use?', 'af': 'Watter webwerwe/toepassing/imidlalo gebruik jy?', 'zu': 'Yiziphi amawebhusayithi/izinhlelo/imidlalo ozisebenzisayo?'},
                'options': []  # Open-ended question
            }
        ]
    }
    
    # Generate PDF content
    pdf_content = f"<h1 style='color: black;'>{survey_data['Heading']['en']}</h1>"
    pdf_content += f"<h1 style='color: black;'>{survey_data['Heading']['af']}</h1>"
    pdf_content += f"<h1 style='color: black;'>{survey_data['Heading']['zu']}</h1>"

    for question in survey_data['Questions']:
        pdf_content += f"<p style='color: black;'>{question['question']['en']}</p>"
        pdf_content += f"<p style='color: black;'>{question['question']['af']}</p>"
        pdf_content += f"<p style='color: black;'>{question['question']['zu']}</p>"
        if question['options']:
            pdf_content += "<ul>"
            for option in question['options']:
                pdf_content += f"<li style='color: black;'>{option}</li>"
            pdf_content += "</ul>"
        else:
            pdf_content += "<p style='color: black;'>[Your answer here]</p>"

    pdf_content += "<h2 style='color: black;'>Notes:</h2>"
    pdf_content += "<p style='color: black;'>[Your notes here]</p>"

    # Convert to PDF
    pdfkit.from_string(pdf_content, 'learner_survey.pdf')

# Generate the survey PDF
if __name__ == '__main__':
    generate_learner_survey()