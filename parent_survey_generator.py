from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Checkbox

def create_parent_survey_pdf(filename):
    # Create PDF document
    pdf = SimpleDocTemplate(filename, pagesize=A4)
    elements = []

    # Define styles
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Trilingual', fontSize=16, textColor=colors.black))

    # Title
    title = Paragraph('Parent Survey / Ouersensus / Uphenyo LwababMali', styles['Trilingual'])
    elements.append(title)
    elements.append(Spacer(1, 20))

    # Device Ownership Section
    elements.append(Paragraph('1. Device Ownership (Ownership Options - Eienaarskap - Ukuziqhenya)', styles['Trilingual']))
    devices = ['Cellphone', 'Smartwatch', 'Tablet', 'Xbox', 'Wii']
    options = ['Own', "Parent's", 'Shared']
    for device in devices:
        for option in options:
            checkbox = Checkbox(eid='checkbox', checked=False)
            elements.append(Paragraph(f'{checkbox} {device} - {option}', styles['Trilingual']))
    elements.append(Spacer(1, 10))

    # Independence vs Supervision Section
    elements.append(Paragraph('2. Independence vs Supervision (Onafhanklik vs Onder toesig)', styles['Trilingual']))
    independence_options = ['Independent / Onafhanklik', 'Supervised / Onder toesig']
    for option in independence_options:
        checkbox = Checkbox(eid='checkbox', checked=False)
        elements.append(Paragraph(f'{checkbox} {option}', styles['Trilingual']))
    elements.append(Spacer(1, 10))

    # Internet Access & Freedom of Use Section
    elements.append(Paragraph('3. Internet Access & Freedom of Use (Ja/Nee Toegang)', styles['Trilingual']))
    access_options = ['Yes', 'No']
    for option in access_options:
        checkbox = Checkbox(eid='checkbox', checked=False)
        elements.append(Paragraph(f'{checkbox} {option} - Free use / Limited use', styles['Trilingual']))
    elements.append(Spacer(1, 10))

    # Websites/Apps/Games Section
    elements.append(Paragraph('4. Websites/Apps/Games (Webwerwe/Toepassings/Speletjies)', styles['Trilingual']))
    websites = ['Google', 'Facebook', 'Instagram', 'TikTok', 'WhatsApp', 'YouTube', 'Roblox', 'Minecraft']
    for website in websites:
        checkbox = Checkbox(eid='checkbox', checked=False)
        elements.append(Paragraph(f'{checkbox} {website}', styles['Trilingual']))
    elements.append(Spacer(1, 10))

    # Notes section
    elements.append(Paragraph('5. Notes Section for Parent Comments / Nota afdeling vir Ouers Kommentaar', styles['Trilingual']))
    elements.append(Spacer(1, 10))
    elements.append(Paragraph('____________________________________________________', styles['Trilingual']))

    # Build the PDF
    pdf.build(elements)

# Generate the survey PDF
create_parent_survey_pdf('parent_survey.pdf')
