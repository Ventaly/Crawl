import asyncio



from  Utils.Slider_Captcha import solve_slider
async def login(page):
    """执行登录操作"""
    await page.get_by_text('密码登录').click()
    await page.fill('input#username', 'LeVent')
    await page.fill('input#password', '123456789@')
    await page.get_by_role("button", name="登录", exact=True).click()

    # 等待所有网络请求完成
    await asyncio.sleep(5)

    #处理滑动验证码
    try:
        await solve_slider( page)  # 替换为实际的选择器

        print("滑动验证码完成")
    except ValueError as e:
        print(e)

    await asyncio.sleep(2)