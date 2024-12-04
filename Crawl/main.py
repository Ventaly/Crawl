
from playwright.async_api import async_playwright
import asyncio
from Operations.Login import  login
from Operations.Chat import  chat

async def launch_browser(playwright):
    """启动浏览器实例"""
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.new_context(
        user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
    )
    return browser, context
async def navigate_to_recommend(context):
    """导航至推荐页面并处理登录"""
    page = await context.new_page()
    await page.goto('https://lpt.liepin.com/user/login')
    if "login" in page.url:
        await login(page)
    await page.get_by_text('沟通',exact=True).click()
    await chat(page)

async def main():
    """主函数，程序入口点"""
    async with async_playwright() as playwright:
        browser, context = await launch_browser(playwright)
        await navigate_to_recommend(context)
        await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
