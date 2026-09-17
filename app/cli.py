import click
from app.generator import generate_pdf_report
from app.scheduler import start_scheduled_jobs

@click.group()
def cli():
    """Enterprise Automation Tool - PDF Generator & Scheduler CLI"""
    pass

@cli.command()
@click.option('--output', default='Enterprise_Report.pdf', help='Output PDF file name.')
def generate(output):
    """Generate a single executive telemetry PDF report immediately."""
    click.echo("[*] Generating report...")
    file_path = generate_pdf_report(output)
    click.echo(f"[✓] Report generated successfully: {file_path}")

@cli.command()
@click.option('--interval', default=60, help='Execution interval in seconds.')
def schedule(interval):
    """Start the background scheduler for automated PDF generation."""
    start_scheduled_jobs(interval_seconds=interval)

if __name__ == '__main__':
    cli()