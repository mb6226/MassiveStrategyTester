from weasyprint import HTML

INPUT_HTML = "Reports/final_report.html"
OUTPUT_PDF = "Reports/final_report.pdf"

def convert_html_to_pdf():
    HTML(INPUT_HTML).write_pdf(OUTPUT_PDF)
    print(f"✅ PDF report saved to {OUTPUT_PDF}")

if __name__ == "__main__":
    convert_html_to_pdf()
