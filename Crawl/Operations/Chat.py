import asyncio


from Operations.Talent import  Talent_Search
from  Utils.GetImage import check_text1, download_resume


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