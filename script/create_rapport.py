from fpdf import FPDF
from pathlib import Path

## générate pdf ##
def generate_rapport(rapportName):
    rapportFolder = path = Path(__file__).parent.parent.resolve() / 'rapports'
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, f"Rapport for {rapportName}", ln=1, align="C")
    pdf.output(f"{rapportFolder}/{rapportName}.pdf")
    return rapportFolder
