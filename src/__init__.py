import traceback

try:
    from src.job.models import JobPosting
    from src.resume.models import ResumePostings
except Exception:
    traceback.print_exc()