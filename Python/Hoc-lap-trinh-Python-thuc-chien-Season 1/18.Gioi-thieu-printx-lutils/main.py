# ----------------------------
# Bài: Giới thiệu printx() và lutils
# Kênh youtube: youtube.com/tranducloi
# pipenv install lutils
# pip install lutils
# ----------------------------
# import printx()
from lutils.lutils import printx, yesterdaystr

# using printx. If file not exist
# printx("abc", "test.log")
# printx("this is log file from youtube.com/tranducloi", "test.log")
printx(yesterdaystr(), "test.log")
