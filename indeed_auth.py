import asyncio
from playwright.async_api import async_playwright
import os

async def save_indeed_session():

    user_data_dir = os.path.abspath("./playwright_session")

    print("Launching browser for initial authentication...")
    print("A browser window will open to authenticate you with Indeed. Please log in and close the browser when done.")
    print("You have 90 seconds to complete the login and any captcha if prompted.\n")

    async with async_playwright() as p:
        context = await p.chromium.launch_persistent_context(
            user_data_dir=user_data_dir,
            headless=False,
            args=["--disable-blink-features=AutomationControlled"]

        )

        page= await context.new_page()
        await page.goto("https://ca.indeed.com/?r=us")

        try:
            print("Waiting for login... (Press Ctrl+C in terminal if you finish early)")
            await asyncio.sleep(90)

        except KeyboardInterrupt:
            print("Manual timer interrupted")

        print("Session cookies saved successfully into './playwright_session'!")
        await context.close()

if __name__ == "__main__":
    asyncio.run(save_indeed_session())