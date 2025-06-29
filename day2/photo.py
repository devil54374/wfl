import rasterio
import numpy as np
from PIL import Image, ImageEnhance
import os


def process_sentinel2_image(input_path, output_path, brightness_factor=1.0):
    """
    处理哨兵2号遥感图像并调整亮度
    参数：
    - input_path: 输入图像路径
    - output_path: 输出图像保存路径
    - brightness_factor: 亮度调整系数 (>1增亮, <1减暗)
    """
    # 1. 安全处理Windows路径
    input_path = input_path.replace("\\", "/")
    output_path = output_path.replace("\\", "/")

    # 2. 验证文件存在
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"文件不存在: {input_path}")

    # 3. 读取遥感图像数据
    with rasterio.open(input_path) as src:
        # 3.1 读取5个波段（假设顺序：B2-蓝, B3-绿, B4-红, B8-近红外, B11-短红外）
        bands = [src.read(i) for i in range(1, min(src.count + 1, 6))]

        # 3.2 检查波段数量
        if len(bands) < 3:
            raise ValueError("文件缺少足够波段生成RGB图像，至少需要3个波段")

        # 4. 数据处理
        # 4.1 压缩数据范围 (0-10000 → 0-255)
        def scale_band(band):
            band = band.astype(np.float32)
            scaled = (band / 10000.0) * 255
            return np.clip(scaled, 0, 255).astype(np.uint8)

        # 4.2 处理每个波段
        blue_band = scale_band(bands[0])  # B2-蓝
        green_band = scale_band(bands[1])  # B3-绿
        red_band = scale_band(bands[2])  # B4-红

        # 5. 创建RGB图像
        rgb_image = np.dstack((red_band, green_band, blue_band))

        # 6. 亮度调整（新增功能）[9](@ref)
        # 6.1 将NumPy数组转为PIL图像
        pil_img = Image.fromarray(rgb_image)

        # 6.2 创建亮度增强器并应用调整
        enhancer = ImageEnhance.Brightness(pil_img)
        adjusted_img = enhancer.enhance(brightness_factor)

        # 7. 保存结果
        # 7.1 确保输出目录存在
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        # 7.2 保存调整后的图像
        adjusted_img.save(output_path)

        print(f"成功生成图像: {output_path}")
        print(f"亮度调整系数: {brightness_factor}")

        return np.array(adjusted_img)


# 使用示例
if __name__ == "__main__":
    # 输入文件路径
    input_tiff = r"D:\shixun\2020_0427_fire_B2348_B12_10m_roi.tif"

    # 输出文件路径
    output_jpg = r"D:\shixun\processed\rgb_adjusted.jpg"

    # 处理图像（亮度系数1.5表示增加50%亮度）
    try:
        processed = process_sentinel2_image(input_tiff, output_jpg, brightness_factor=1.5)
        print(f"输出图像尺寸: {processed.shape[1]}×{processed.shape[0]}像素")
    except Exception as e:
        print(f"处理失败: {str(e)}")