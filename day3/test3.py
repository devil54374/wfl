import pandas as pd
import time
import random
import os
from pathlib import Path
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent

# 待爬取的文章列表
paper_titles = [
    "Automatic crater detection and age estimation for mare regions on the lunar surface",
    "The origin of planetary impactors in the inner solar system",
    "Deep learning based systems for crater detection: A review",
    "A preliminary study of classification method on lunar topography and landforms",
    "The CosmoQuest Moon mappers community science project: The effect of incidence angle on the Lunar surface crater distribution",
    "Fast r-cnn",
    "You only look once: Unified, real-time object detection",
    "Attention is all you need",
    "End-to-end object detection with transformers"
]

# 创建目标目录
save_dir = r"D:\shixun\论文爬取"
os.makedirs(save_dir, exist_ok=True)

# 初始化用户代理生成器
ua = UserAgent()


def get_random_headers():
    """生成随机请求头"""
    return {
        'User-Agent': ua.random,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': random.choice(['en-US,en;q=0.9', 'zh-CN,zh;q=0.9', 'ja,en-US;q=0.9,en;q=0.8']),
        'Referer': 'https://scholar.google.com/'
    }


def human_like_delay(min_delay=2.0, max_delay=8.0):
    """模拟人类操作间隔（智能延时）"""
    delay = random.uniform(min_delay, max_delay)
    print(f"⏳ 模拟思考，等待 {delay:.1f} 秒...")
    time.sleep(delay)
    return delay


def simulate_human_typing(element, text):
    """模拟人类打字行为"""
    actions = ActionChains(driver)
    for char in text:
        actions.send_keys_to_element(element, char)
        actions.perform()
        time.sleep(random.uniform(0.05, 0.3))  # 随机按键间隔


def scroll_randomly():
    """随机滚动页面模拟人类浏览"""
    scroll_height = driver.execute_script("return document.body.scrollHeight")
    scroll_times = random.randint(2, 5)

    for _ in range(scroll_times):
        # 随机滚动位置
        scroll_pos = random.randint(200, int(scroll_height * 0.8))
        driver.execute_script(f"window.scrollTo(0, {scroll_pos});")

        # 随机等待时间
        time.sleep(random.uniform(0.5, 2.5))

        # 随机鼠标移动
        x_offset = random.randint(-100, 100)
        y_offset = random.randint(-50, 50)
        ActionChains(driver).move_by_offset(x_offset, y_offset).perform()
        ActionChains(driver).move_by_offset(-x_offset, -y_offset).perform()


def setup_driver():
    """配置浏览器驱动"""
    chrome_options = Options()

    # 设置随机User-Agent
    user_agent = ua.random
    chrome_options.add_argument(f'user-agent={user_agent}')

    # 启用无头模式（可选）
    # chrome_options.add_argument('--headless')

    # 禁用自动化特征
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)

    # 禁用图片加载加速
    prefs = {"profile.managed_default_content_settings.images": 2}
    chrome_options.add_experimental_option("prefs", prefs)

    # 初始化浏览器
    driver = webdriver.Chrome(options=chrome_options)

    # 隐藏自动化特征
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    return driver


def fetch_through_browser():
    """使用浏览器模拟人类操作获取文献数据"""
    results = []
    global  driver
    driver = setup_driver()

    try:
        # 打开Google Scholar
        driver.get("https://scholar.google.com")
        human_like_delay(3, 6)  # 初始页面加载等待

        for i, title in enumerate(paper_titles):
            try:
                print(f"\n🔍 开始处理: {title} ({i + 1}/{len(paper_titles)})")

                # 定位搜索框
                search_box = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.NAME, "q"))
                )

                # 清除搜索框
                search_box.clear()
                human_like_delay(0.5, 1.5)

                # 模拟人类输入
                simulate_human_typing(search_box, title)
                human_like_delay(1, 2)  # 输入后短暂停顿

                # 提交搜索
                search_box.submit()

                # 等待结果加载
                WebDriverWait(driver, 15).until(
                    EC.presence_of_element_located((By.ID, "gs_res_ccl"))
                )

                # 模拟人类浏览行为
                scroll_randomly()

                # 获取第一条结果
                try:
                    first_result = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, ".gs_r.gs_or.gs_scl"))
                    )

                    # 提取信息
                    result = extract_result_info(first_result, title)
                    results.append(result)
                    print(f"✅ 成功获取: {title}")

                except Exception as e:
                    print(f"❌ 结果解析失败: {str(e)}")
                    results.append({'title': title, 'error': '结果解析失败'})

                # 随机延时后返回首页
                human_like_delay(3, 8)
                driver.get("https://scholar.google.com")
                human_like_delay(2, 4)

            except Exception as e:
                print(f"🔥 处理失败 [{title}]: {str(e)}")
                results.append({'title': title, 'error': str(e)})

                # 错误后增加额外延时
                time.sleep(random.uniform(8, 15))

                # 刷新浏览器
                driver.refresh()
                human_like_delay(3, 6)

    finally:
        # 关闭浏览器
        driver.quit()

    return results


def extract_result_info(result_element, original_title):
    """从结果元素中提取信息"""
    # 标题
    title_elem = result_element.find_element(By.CSS_SELECTOR, "h3 a")
    title = title_elem.text

    # 作者和年份
    authors_year = result_element.find_element(By.CSS_SELECTOR, ".gs_a").text
    parts = authors_year.split("-")
    authors = parts[0].strip() if len(parts) > 0 else "N/A"
    year = parts[1].strip() if len(parts) > 1 else "N/A"

    # 引用量
    citations = "0"
    try:
        citations_elem = result_element.find_element(By.CSS_SELECTOR, ".gs_ri .gs_fl a:nth-child(3)")
        if "Cited by" in citations_elem.text:
            citations = citations_elem.text.split("Cited by ")[1]
    except:
        pass

    # 摘要片段
    abstract = "N/A"
    try:
        abstract_elem = result_element.find_element(By.CSS_SELECTOR, ".gs_rs")
        abstract = abstract_elem.text[:200] + '...'
    except:
        pass

    # 相似度检查
    similarity = calculate_title_similarity(original_title, title)

    return {
        'title': title,
        'original_title': original_title,
        'similarity': f"{similarity:.1f}%",
        'authors': authors,
        'year': year,
        'citations': citations,
        'abstract': abstract,
        'source': 'selenium'
    }


def calculate_title_similarity(title1, title2):
    """计算标题相似度"""
    # 简化实现，实际应用中可使用更复杂的算法
    set1 = set(title1.lower().split())
    set2 = set(title2.lower().split())
    intersection = set1 & set2
    union = set1 | set2
    return (len(intersection) / len(union)) * 100 if union else 0


# 主执行逻辑
if __name__ == "__main__":
    # 记录开始时间
    start_time = time.time()

    # 使用浏览器模拟方案
    scholarly_data = fetch_through_browser()

    # 保存结果到Excel
    save_path = Path(save_dir) / "scholar_results.xlsx"
    df = pd.DataFrame(scholarly_data)

    try:
        df.to_excel(save_path, index=False)
        print(f"\n🎉 数据已保存至: {save_path}")
    except Exception as e:
        print(f"\n❌ 文件保存失败: {str(e)}")
        # 尝试创建父目录后重试
        os.makedirs(save_path.parent, exist_ok=True)
        df.to_excel(save_path, index=False)
        print(f"✅ 重试后保存成功: {save_path}")

    # 计算总耗时
    total_time = time.time() - start_time
    mins, secs = divmod(total_time, 60)

    # 添加完成提示
    print("\n" + "=" * 50)
    print(f"任务完成! 共处理 {len(paper_titles)} 篇论文")
    success_count = len([x for x in scholarly_data if 'error' not in x])
    failed_count = len(paper_titles) - success_count
    print(f"成功获取: {success_count} 篇")
    print(f"获取失败: {failed_count} 篇")
    print(f"总耗时: {int(mins)}分{int(secs)}秒")
    print(f"平均每篇耗时: {total_time / len(paper_titles):.1f}秒")
    print("=" * 50)

    # 保存详细日志
    log_path = Path(save_dir) / "crawl_log.json"
    with open(log_path, 'w') as f:
        json.dump({
            "date": time.strftime("%Y-%m-%d %H:%M:%S"),
            "papers_processed": len(paper_titles),
            "success_count": success_count,
            "failed_count": failed_count,
            "total_time": total_time
        }, f, indent=2)
    print(f"📝 详细日志已保存至: {log_path}")