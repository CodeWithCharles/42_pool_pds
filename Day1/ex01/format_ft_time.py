import time
from datetime import datetime

now_seconds = time.time()

formatted_seconds = f"{now_seconds:,.4f}"

formatted_scientific = f"{now_seconds:.2e}"

print(f"Seconds since January 1, 1970: {formatted_seconds} or {formatted_scientific} in scientific notation")

now_date = datetime.now()
formatted_date = now_date.strftime("%b %d %Y")

print(formatted_date)
