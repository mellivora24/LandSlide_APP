import gettext

# Load ngôn ngữ (file .mo)
locale_path = './locales'  # Đường dẫn chứa file ngôn ngữ
lang = gettext.translation('messages', localedir=locale_path, languages=['vi'])
lang.install()
trans = lang.gettext  # Sử dụng _() để dịch

# Sử dụng
print(trans("Hello, World!"))  # Dịch câu "Hello, World!" sang tiếng Việt
