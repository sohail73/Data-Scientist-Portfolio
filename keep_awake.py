"""Opens the deployed Streamlit app in a real (headless) browser so it never goes to sleep.
A plain HTTP ping does NOT work: the sleeping page is just a static shell, the app only wakes
when a browser actually connects. If the app is asleep, this script clicks the wake-up button."""
import os, sys, time
from playwright.sync_api import sync_playwright, TimeoutError as PWTimeout

URL = os.environ.get("APP_URL", "").strip()
if not URL:
    sys.exit("APP_URL is not set (add it as a GitHub repository secret).")

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(URL, wait_until="domcontentloaded", timeout=120_000)
    page.wait_for_timeout(6_000)

    wake = page.get_by_text("get this app back up", exact=False)
    if wake.count():
        print("App was asleep -> clicking the wake-up button")
        wake.first.click()
    else:
        print("No wake-up button -> app was already awake")

    # wait until the real app has rendered (Streamlit Cloud puts it inside an iframe)
    deadline, ok = time.time() + 240, False
    while time.time() < deadline and not ok:
        for root in [page.frame_locator('iframe[title="streamlitApp"]'), page]:
            try:
                root.locator('[data-testid="stApp"]').first.wait_for(timeout=5_000)
                ok = True
                break
            except PWTimeout:
                pass
    browser.close()

print("App is awake and rendered." if ok else "Could not confirm the app rendered.")
sys.exit(0 if ok else 1)
