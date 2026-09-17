import os
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from app.fetcher import fetch_telemetry_data

def generate_pdf_report(output_filename: str = "Enterprise_Executive_Report.pdf") -> str:
    df = fetch_telemetry_data()
    doc = SimpleDocTemplate(output_filename, pagesize=letter)
    story = []
    
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontSize=20,
        textColor=colors.HexColor('#1E293B'),
        spaceAfter=12
    )
    
    story.append(Paragraph("Enterprise Infrastructure Telemetry Report", title_style))
    story.append(Paragraph("Automated System Performance Analytics & Operational Metrics", styles['Normal']))
    story.append(Spacer(1, 18))
    
    # Format Table Data
    table_data = [["Service Name", "Total Requests", "Uptime (%)", "Avg Latency (ms)"]]
    for idx, row in df.iterrows():
        table_data.append([row["Service"], f"{row['Requests']:,}", f"{row['Uptime_Pct']}%", f"{row['Avg_Latency_ms']} ms"])
        
    t = Table(table_data, colWidths=[150, 100, 100, 100])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0F172A')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0,0), (-1,0), 10),
        ('BACKGROUND', (0,1), (-1,-1), colors.HexColor('#F8FAFC')),
        ('GRID', (0,0), (-1,-1), 1, colors.HexColor('#CBD5E1')),
    ]))
    
    story.append(t)
    doc.build(story)
    return os.path.abspath(output_filename)