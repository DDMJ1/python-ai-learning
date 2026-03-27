import time
import sys


def countdown(minutes):
    """
    倒计时器（分钟）
    :param minutes: 倒计时分钟数
    """
    seconds = minutes * 60
    while seconds > 0:
        # 格式化时间：分:秒
        mins = seconds // 60
        secs = seconds % 60
        sys.stdout.write(f"\r倒计时：{int(mins):02d}:{int(secs):02d}")
        sys.stdout.flush()
        time.sleep(1)
        seconds -= 1
    # 倒计时结束提醒
    print("\n⏰ 倒计时结束！")
    # 播放提示音（Windows）
    import winsound
    winsound.Beep(1000, 1000)


# 用法示例
if __name__ == "__main__":
    countdown(0.5)  # 测试：10秒倒计时
