import os
import re
import sys


def natural_sort_key(s: str) -> list:
    """
    增强版自然排序函数：完全模拟Windows资源管理器的排序逻辑
    1. 分割数字和非数字部分
    2. 数字部分转换为(类型标记, (数值, 原始字符串))元组
    3. 非数字部分转换为小写
    """
    parts = re.split(r'(\d+)', s)
    processed = []
    for part in parts:
        if part == '':  # 跳过空字符串
            continue
        if part.isdigit():
            # 数字部分：类型标记0 + (数值, 原始字符串小写)
            processed.append((0, (int(part), part.lower())))
        else:
            # 非数字部分：类型标记1 + 小写字符串
            processed.append((1, part.lower()))
    return processed


def batch_rename_images(img_folder: str, txt_file: str):
    # 1. 读取TXT文件中的新名称（跳过空行）
    with open(txt_file, 'r', encoding='utf-8') as f:
        new_names = [line.strip() for line in f if line.strip()]

    # 2. 获取图片文件并按Windows自然顺序排序
    img_files = [
        f for f in os.listdir(img_folder)
        if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp'))
    ]
    img_files.sort(key=natural_sort_key)  # 强制按Windows顺序排序

    # 3. 检查数量一致性
    if len(img_files) != len(new_names):
        print(f"⚠️ 警告：图片数量 ({len(img_files)}) ≠ 名称数量 ({len(new_names)})")
        min_count = min(len(img_files), len(new_names))
        img_files = img_files[:min_count]
        new_names = new_names[:min_count]
        print(f"⚠️ 仅处理前 {min_count} 个文件")

    # 4. 批量重命名（处理冲突和非法字符）
    rename_log = []
    for i, (old_name, new_base) in enumerate(zip(img_files, new_names)):
        _, ext = os.path.splitext(old_name)  # 保留原扩展名
        safe_name = re.sub(r'[\\/*?:"<>|]', '', new_base)  # 移除Windows非法字符
        new_name = f"{safe_name}{ext}"
        new_path = os.path.join(img_folder, new_name)

        # 处理文件名冲突（自动添加 _1, _2 后缀）
        counter = 1
        while os.path.exists(new_path):
            new_name = f"{safe_name}_{counter}{ext}"
            new_path = os.path.join(img_folder, new_name)
            counter += 1

        # 执行重命名
        old_path = os.path.join(img_folder, old_name)
        try:
            os.rename(old_path, new_path)
            rename_log.append(f"{old_name} → {new_name}")
            print(f"✅ 成功: {old_name} → {new_name}")
        except Exception as e:
            print(f"❌ 失败: {old_name} → {new_name} | 错误: {e}")

    # 5. 保存重命名日志
    log_path = os.path.join(img_folder, "rename_log.txt")
    with open(log_path, 'w', encoding='utf-8') as log_file:
        log_file.write("\n".join(rename_log))
    print(f"📝 重命名日志已保存至: {log_path}")


if __name__ == "__main__":
    img_folder = r"C:\Users\Lenovo\Desktop\作业\新建文件夹"  # 替换为图片目录
    txt_file = r"C:\Users\Lenovo\Desktop\作业\新建文本文档.txt"  # 替换为TXT文件路径
    batch_rename_images(img_folder, txt_file)
    print("🎉 批量重命名完成！")