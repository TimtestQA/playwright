from playwright.sync_api import sync_playwright, Playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(viewport={"width": 1280, "height": 720})
    page = context.new_page()

    # Navigate to the URL
    page.goto("https://google.com")

    # Wait for the page to load completely
    page.wait_for_load_state("networkidle")

    # Take a screenshot of the page
    page.screenshot(path="example_screenshot.png")

    # Close the browser
    browser.close()

