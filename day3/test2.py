import requests
from lxml import etree
import os
import time
import random
from urllib.parse import urljoin


def download_images():
    # 增强反爬配置
    url = "http://pic.netbian.com/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
        'Referer': url,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive'
    }
    save_dir = r"D:\shixun\图片爬取"  # 原始字符串修复路径问题

    # 自动创建目录
    os.makedirs(save_dir, exist_ok=True)

    try:
        # 获取网页源码（带超时重试）
        for _ in range(3):  # 最多重试3次
            try:
                response = requests.get(url, headers=headers, timeout=15)
                response.encoding = 'gbk'
                response.raise_for_status()
                break
            except requests.exceptions.RequestException:
                time.sleep(random.uniform(2, 5))  # 指数退避重试
        else:
            print("❌ 多次请求失败，请检查网络连接")
            return

        # 调试：保存网页源码（可选）
        with open(os.path.join(save_dir, "page_source.html"), "w", encoding="gbk") as f:
            f.write(response.text)

        # 解析HTML（使用备用XPath策略）
        html = etree.HTML(response.text)

        # 方案1：使用更通用的图片选择器
        img_elements = html.xpath("//img[@src and contains(@src, 'uploads')]")

        # 方案2：如果方案1失败，尝试匹配图片容器
        if not img_elements:
            img_elements = html.xpath("//div[contains(@class, 'list')]//img")

        # 方案3：终极回退方案
        if not img_elements:
            img_elements = html.xpath("//img[@src]")
            print("⚠️ 使用通用选择器，可能包含非目标图片")

        if not img_elements:
            print("⛔ 未找到图片元素！可能原因：")
            print("- 网站结构已更新 [6](@ref)")
            print("- 触发反爬机制 [5](@ref)")
            print("- 动态加载内容（需改用Selenium）")
            return

        print(f"✅ 发现{len(img_elements)}张图片，开始下载...")

        # 下载每张图片
        for i, img in enumerate(img_elements, 1):
            # 获取相对路径并修复特殊字符
            relative_path = img.xpath('./@src')[0].replace('\\', '/')
            full_url = urljoin(url, relative_path)

            # 生成安全文件名
            file_name = f"{i}_{os.path.basename(full_url).split('?')[0]}"
            save_path = os.path.join(save_dir, file_name)

            try:
                # 图片请求添加Referer
                img_headers = headers.copy()
                img_headers['Referer'] = full_url

                img_response = requests.get(full_url, headers=img_headers, timeout=20)
                img_response.raise_for_status()

                # 验证图片有效性
                if len(img_response.content) < 1024:
                    print(f"⚠️ 图片过小可能无效: {file_name}")
                    continue

                with open(save_path, 'wb') as f:
                    f.write(img_response.content)
                print(f"✅ [{i}/{len(img_elements)}] 已保存: {file_name}")

                # 智能延时（根据图片大小调整）
                delay = max(1, len(img_response.content) / (1024 * 50))  # 每50KB延迟1秒
                time.sleep(delay + random.uniform(0.5, 1.5))

            except Exception as e:
                print(f"❌ 下载失败: {file_name} | 错误: {str(e)}")

    except Exception as e:
        print(f"🔥 全局异常: {str(e)}")


if __name__ == "__main__":
    download_images()
    print("=" * 50)
    print(f"任务执行完毕！保存目录: {r'D:\shixun\图片爬取'}")