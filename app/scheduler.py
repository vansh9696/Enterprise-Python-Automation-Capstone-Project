import time
from apscheduler.schedulers.background import BackgroundScheduler
from app.generator import generate_pdf_report

def start_scheduled_jobs(interval_seconds: int = 60):
    scheduler = BackgroundScheduler()
    scheduler.add_job(
        generate_pdf_report, 
        'interval', 
        seconds=interval_seconds, 
        kwargs={'output_filename': 'Automated_Scheduled_Report.pdf'}
    )
    scheduler.start()
    print(f"[+] Automated Scheduler Active: Generating reports every {interval_seconds} seconds.")
    try:
        while True:
            time.sleep(1)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
        print("\n[-] Scheduler stopped gracefully.")