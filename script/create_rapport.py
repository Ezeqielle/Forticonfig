## import modules ##
from fpdf import FPDF

def get_title(repport):
    global title
    title = repport

## define pdf class ##
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 15)
        w = self.get_string_width(title) + 6
        self.set_x((210 - w) / 2)
        self.set_fill_color(255, 255, 255)
        self.set_text_color(0, 0, 0)
        self.cell(w, 9, title, 1, 1, 'C', 1)
        self.ln(10)
    
    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.set_text_color(128)
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'R')

    def chapter_title(self, ip, port):
        self.set_font('Arial', 'B', 12)
        self.set_fill_color(200, 220, 255)
        self.set_text_color(0, 0, 0)
        self.cell(0, 6, 'IP: %s // ' %ip + 'Port: %s'%port, 0, 1, 'L', 1)
        self.ln(4)

    def chapter_body(self, name):
        self.set_font('Times', '', 12)
        self.set_text_color(0, 0, 0)
        self.multi_cell(0, 5, txt=name)
        self.ln()
        self.set_font('', 'I')

    def chapter_usb(self, name):
        self.set_font('Times', '', 12)
        self.set_text_color(150, 0, 0)
        self.multi_cell(0, 5, txt=name)
        self.ln()
        self.set_font('', 'I')

    def new_page(self):
        self.add_page()

#if __name__ == "__main__":
#    pdf = PDF()
#    ip = ['192.168.1.1','192.168.1.2','192.168.1.3']
#    pdf.set_title(title)
#    for x in range(len(ip)):
#        pdf.print_chapter(ip[x], "22", "test.txt")
#    pdf.output('test.pdf', 'F')



## générate pdf ##
#def generate_rapport(rapportName):
#    rapportFolder = path = Path(__file__).parent.parent.resolve() / 'rapports'
#    pdf = FPDF()
#    pdf.add_page()
#    pdf.set_font("Arial", size=12)
#    pdf.cell(200, 10, f"Rapport for {rapportName}", ln=1, align="C")
#    pdf.output(f"{rapportFolder}/{rapportName}.pdf")
#    return rapportFolder