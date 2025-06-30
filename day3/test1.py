import requests
from bs4 import BeautifulSoup


def get_douban_hot_top10():
    url = "https://movie.douban.com/chart"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    try:
        # 发送请求并解析页面
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        # 提取电影信息
        movies = []
        for movie_div in soup.find_all('div', class_='pl2')[:10]:  # 限制前10部
            title = movie_div.find('a').get_text(strip=True)
            # 处理标题中的无关内容（如“可播放”标签）
            title = title.split('/')[0].strip()
            rating_tag = movie_div.find('span', class_='rating_nums')
            rating = float(rating_tag.text) if rating_tag else 0.0
            movies.append((title, rating))

        # 按评分降序排序
        movies.sort(key=lambda x: x[1], reverse=True)
        return [movie[0] for movie in movies]  # 只返回标题

    except Exception as e:
        print(f"获取数据失败: {e}")
        return []


# 执行并打印结果
top10_titles = get_douban_hot_top10()
print("豆瓣实时热榜评分前十电影：")
for i, title in enumerate(top10_titles, 1):
    print(f"{i}. {title}")