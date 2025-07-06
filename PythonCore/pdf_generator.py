import pdfkit
import sys
import os

def generate_pdf(input_html, output_pdf):
    config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")
    pdfkit.from_file(input_html, output_pdf, configuration=config)
    print(f"PDF generated successfully: {output_pdf}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python pdf_generator.py input.html output.pdf")
        sys.exit(1)

    input_path = os.path.abspath(sys.argv[1])
    output_path = os.path.abspath(sys.argv[2])

    if not os.path.isfile(input_path):
        print(f"Input file does not exist: {input_path}")
        sys.exit(1)

    generate_pdf(input_path, output_path)
