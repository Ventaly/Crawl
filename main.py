import os.path
from time import sleep
import requests
from bs4 import BeautifulSoup
from playwright.async_api import async_playwright
import asyncio
import cv2
import numpy as np
from PIL import Image
from io import BytesIO
from playwright.sync_api import sync_playwright
import time
from bs4 import  BeautifulSoup
from playwright.sync_api import sync_playwright
import time
from GetImage import get_image_src_and_download

from Slider_Captcha import solve_slider
async def launch_browser(playwright):
    """启动浏览器实例"""
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.new_context(
        user_agent='xxxxxxxx'
    )
    return browser, context


async def navigate_to_recommend(context):
    """导航至推荐页面并处理登录"""
    page = await context.new_page()
    await page.goto('https://lpt.liepin.com/user/login')
    if "login" in page.url:
        await login(page)
    await page.locator('a.navItemWraper--FBaIV').get_by_text('沟通').click()
    await chat(page)


async def login(page):
    """执行登录操作"""
    await page.get_by_text('密码登录').click()
    await page.fill('input#username', 'XXXXX')
    await page.fill('input#password', 'XXXXXXX')
    await page.get_by_role("button", name="登录", exact=True).click()
    # 等待图片加载完成



    # 等待所有网络请求完成
    await asyncio.sleep(5)







    #处理滑动验证码
    try:
        await solve_slider( page)  # 替换为实际的选择器

        print("滑动验证码完成")
    except ValueError as e:
        print(e)

    await asyncio.sleep(2)







# async def handle_page(page):
#     await asyncio.sleep(5)
#     """根据页面URL执行相应操作"""
#     await page.locator('a.navItemWraper--FBaIV').get_by_text('沟通').click()
#     print(page.url)
#     if "recommend" in page.url:
#         await recommend(page)
#     elif "chat" in page.url:
#         await chat(page)
#     elif "apply" in page.url:
#         await apply(page)
#     else:
#         await other_operations(page)


async def recommend(page):
    """处理推荐页面的操作"""
    print(f"当前页面为{page.url}")
    #选择过滤条件
    await page.click('.filterEntryWraper--UfSKr')
    await page.locator('div.ant-lpt-drawer-body').get_by_text('1-3年').click()

    await page.locator('div.ant-lpt-drawer-body').get_by_text('本科').click()
    await page.locator('div.ant-lpt-drawer-body').get_by_text('10-15K').click()
    await page.locator('div.ant-lpt-space-item').get_by_text('确定').click()

    await asyncio.sleep(2)
    # 获取所有 .newResumeItem--ppozw 匹配的 div
    communicate_buttons = page.locator('div.newResumeItem--ppozw')

    # 获取匹配的数量
    count = await communicate_buttons.count()

    # 遍历所有 div
    click_GT=0
    for index in range(count-1,-1,-1):
        # 获取当前 div
        div = communicate_buttons.nth(index)

        # 在当前 div 内定位按钮
        button = div.locator('span.btnContainer--gocvg')
        if await check_text1(page, "立即沟通"):
            # # 检查按钮是否存在并可见
            # if await button.is_visible():
                # 点击按钮
            await button.get_by_text("立即沟通").click()


            await asyncio.sleep(1)
            # 定位目标元素
            close_button1 = page.locator('span.ant-im-modal-close-x span[aria-label="close"]')
            close_button2 =  page.locator('button.ant-lpt-modal-close span.ant-lpt-modal-close-x button span[aria-label="close"]')
            # 检查是否存在且可见
            if await close_button1.is_visible():
                    #await close_button1.nth(index).click()
                    await close_button1.click()
                    print("沟通更多候选人页面关闭")
                    # 检查元素是否存在并可见
            if await close_button2.is_visible():
                    await close_button2.click()
                    print("付费按钮关闭")
                    break
            click_GT = click_GT + 1
            if click_GT >= 3:
                    print(f"已点击 {click_GT} 个按钮，退出循环。")
                    break



async def Talent_Search(page):
        """处理推荐页面的操作"""
        print(f"当前页面为{page.url}")
        #选择过滤条件 page.locator
        await page.get_by_text('不限职位').click()

        job_item= page.locator('div.job-info')
        job_item_count=await job_item.count()
        #for index in range(job_item_count):

        await job_item.nth(0).click()
        job_item = page.locator('div.select-condition')
        job_item_count=await job_item.count()
        for index in range(1,job_item_count):
            await page.locator('div.select-condition').nth(index).click()
        await page.locator('div.jobs-handle').get_by_text('确定').click()
        await page.locator('div.searchInputBox--R_eer').get_by_text('搜索',exact=True).click()

        await page.locator('span.ant-lpt-select-selection-item').get_by_text('沟通状态').click()
        await  page.locator('div.rc-virtual-list').get_by_text('隐藏我和同事已沟通').click()
        await  page.locator('label.ant-lpt-checkbox-wrapper').get_by_text('隐藏已查看').click()
        await asyncio.sleep(2)
        # 获取所有 .newResumeItem--ppozw 匹配的 div
        #communicate_buttons = page.locator('div.resumeCard--uwSqc')
        communicate_buttons = page.locator('button.ant-lpt-btn.ant-lpt-btn-primary.ant-lpt-teno-btn.ant-lpt-teno-btn-secondary')
        # 获取匹配的数量communicate_buttons
        count = await communicate_buttons.count()

        # 遍历所有 div
        click_GT=0
        for index in range(count-1,-1,-1):
                # 获取当前 div
                div = communicate_buttons.nth(index)

                # 在当前 div 内定位按钮
                # button = div.locator('span.btnContainer--NUXPG')
                if await check_text1(page, "立即沟通"):
                    # # 检查按钮是否存在并可见
                    # if await button.is_visible():
                        # 点击按钮
                    await div.get_by_text("立即沟通").click()


                    await asyncio.sleep(1)
                    # 定位目标元素
                    close_button1 = page.locator('span.ant-im-modal-close-x span[aria-label="close"]')
                    close_button2 =  page.locator('button.ant-lpt-modal-close span.ant-lpt-modal-close-x button span[aria-label="close"]')
                    # 检查是否存在且可见
                    if await close_button1.is_visible():
                            #await close_button1.nth(index).click()
                            await close_button1.click()
                            print("沟通更多候选人页面关闭")
                            # 检查元素是否存在并可见
                    if await close_button2.is_visible():
                            await close_button2.click()
                            print("付费按钮关闭")
                            break
                    click_GT = click_GT + 1
                    if click_GT >= 3:
                            print(f"已点击 {click_GT} 个按钮，退出循环。")
                            break



async def chat(page):
    """处理聊天页面的操作"""
    print("进入chat功能块")
    await page.get_by_text('沟通',exact=True).click()
    print(f"当前页面为{page.url}")
    #点击未读，来进行今日的简历收取
    #await page.get_by_text('未读').click()
    await asyncio.sleep(3)
    contacts =  page.locator('.im-ui-contact-info')
    count = await contacts.count()
    for index in range(count):
        div = contacts.nth(index)
        await div.click()
        # 等待目标 div 元素加载完毕
         # 等待 60 秒
        # 找到招聘者求职岗位，为后面下载文件做准备

        div_text = page.locator('a.im-ui-pro-chat-header-ellipsis.im-ui-pro-chat-header-job-title')

        span_texts1 = div_text.locator('span')
        # 检查 div 下是否有 span
        Job_Titl = await span_texts1.text_content()

        div_text2=page.locator('div.im-ui-pro-chat-header-ellipsis.im-ui-pro-chat-header-text.im-ui-pro-chat-header-name')
        # 打印文本内容
        Applicant_Name=await div_text2.text_content()

        print(Applicant_Name)
        if index>=15:
            break
        await page.get_by_text('查看简历').click()
        # 定位目标 <span> 标签
        # span_texts2 = page.locator('span.name--tU2DG')
        #
        # # 提取 <span> 内的文本内容
        # Applicant_Name = await span_texts2.text_content()
        # print(Applicant_Name)
        # 定位关闭按钮
        close_button = page.locator('span.ant-lpt-modal-close-x')

        # 检查按钮是否存在且可见
        if await close_button.nth(0).is_visible():
            await close_button.nth(0).click()  # 点击按钮
            print("今天查看简历次数已达20次，需要付费")
            break
            # 检查按钮是否存在且可见
        if await close_button.nth(1).is_visible():
            await close_button.nth(1).click()  # 点击按钮
            print("今天查看简历次数已达20次，需要付费")
            break

        if await check_text1(page, "下载"):

            await download_resume(page, Job_Titl, Applicant_Name)
            await page.get_by_text('继续沟通').nth(1).click()

        elif await check_text1(page, "向TA索要"):
            print("当前候选人未公开简历")
            await page.get_by_role("button", name="向TA索要").click()
            #await page.get_by_text('继续沟通').nth(1).click()
        else:
            print("当前候选人未上传简历")
            await page.get_by_text('继续沟通').nth(0).click()


    await asyncio.sleep(1)
    await page.get_by_text('搜索人才',exact=True).click()
    await Talent_Search(page)

async def apply(page):
    """处理申请页面的操作"""
    print(f"当前页面为{page.url}")
    contacts = await page.query_selector_all('.newApplyCardContent--IIss4')
    for contact in contacts:
        await contact.click()
        await asyncio.sleep(1)

        if await check_text1(page, '下载'):
            await download_resume(page)
        elif await check_text1(page, "向TA索要"):
            print("当前候选人未公开简历")
            await page.get_by_role("button", name="向TA索要").click()
        else:
            print("出现未知错误")


async def download_resume(page, Job_Title, Applicant_Name):
    """尝试下载简历"""
    dir_name = "E:\Email-Attachments"

    async with page.expect_download() as download_info:
        await page.locator('div.b-portfolio-wrap-gray').get_by_text('下载').nth(0).click()
    download = await download_info.value
    path = await download.path()
    file_path1 = os.path.join(dir_name, Job_Title)
    file_path = os.path.join(file_path1, f"{Applicant_Name}.pdf")

    await download.save_as(file_path)
    print(f"下载简历至 {path}")


async def check_text1(page, text):
    """检查页面上是否存在指定文本"""
    elements =await page.query_selector_all(f'text="{text}"')
    print(elements)
    if elements:
        print(f"页面上存在文本为‘{text}’的元素")
        return True
    else:
        print(f"页面上不存在文本为‘{text}’的元素")
        return False


async def other_operations(page):
    """处理其他页面的操作"""
    print(f"出现错误，跳转了其他页面，当前网址是: {page.url}")


async def main():
    """主函数，程序入口点"""
    async with async_playwright() as playwright:
        browser, context = await launch_browser(playwright)
        await navigate_to_recommend(context)
        await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
