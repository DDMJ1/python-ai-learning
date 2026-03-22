import os


def batch_rename_files(folder_path, prefix, file_ext=".txt"):
    """
    批量重命名文件
    :param folder_path: 文件夹路径
    :param prefix: 新文件名前缀
    :param file_ext: 要重命名的文件后缀
    """
    # 遍历文件夹
    for idx, filename in enumerate(os.listdir(folder_path), 1):  # 列出指定文件夹路径下的所有文件和子文件夹的名称（仅名称，不是完整路径）
        # 只处理指定后缀的文件
        if filename.endswith(file_ext):
            # 拼接旧路径和新路径
            old_path = os.path.join(folder_path, filename)  # 路径拼接函数，核心作用是安全地将文件夹路径和文件名拼接成一个完整的文件路径，而且能自动适配不同操作系统的路径分隔符
            new_name = f"{prefix}_{idx}{file_ext}"
            new_path = os.path.join(folder_path, new_name)
            # 重命名
            os.rename(old_path, new_path)  # 将文件 / 文件夹从旧路径（old_path）重命名 / 移动到新路径（new_path）
            print(f"重命名：{filename} → {new_name}")


# 用法示例（替换成你的文件夹路径）
if __name__ == "__main__":
    batch_rename_files("./back", "文档", ".txt")
