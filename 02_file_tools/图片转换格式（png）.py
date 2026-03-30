from PIL import Image
import os


def convert_image_format(folder_path, target_format="PNG"):
    """
    批量转换图片格式
    :param folder_path: 图片文件夹路径
    :param target_format: 目标格式（PNG/JPG）
    """
    # 支持的源格式
    support_formats = (".jpg", ".jpeg", ".png", ".bmp")
    target_format = target_format.upper()

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(support_formats):
            file_path = os.path.join(folder_path, filename)
            # 分离文件名和后缀
            name, ext = os.path.splitext(filename)
            # 新文件名
            new_name = f"{name}.{target_format.lower()}"
            new_path = os.path.join(folder_path, new_name)

            # 转换格式
            try:
                with Image.open(file_path) as img:
                    # JPG需要处理透明通道
                    if target_format == "JPG" and img.mode in ("RGBA", "P"):
                        img = img.convert("RGB")
                    img.save(new_path, target_format)
                print(f"转换完成：{filename} → {new_name}")
            except Exception as e:
                print(f"转换失败 {filename}：{e}")


# 用法示例
if __name__ == "__main__":
    convert_image_format("imgs", "PNG")
