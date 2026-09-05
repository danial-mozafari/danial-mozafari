"""
پنجره‌ی شناور دسکتاپ
=====================
همون داشبورد وب (قیمت، نمودار، هشدارها) رو در یک پنجره‌ی کوچیک، بدون کادر
و همیشه-روی-بقیه نشون می‌ده.

اجرا:
    ترمینال ۱:  python app.py
    ترمینال ۲:  python desktop_widget.py
"""

import webview

if __name__ == "__main__":
    webview.create_window(
        title="قیمت دلار",
        url="http://127.0.0.1:5000/",
        width=380,
        height=640,
        resizable=True,
        frameless=True,
        easy_drag=True,
        on_top=True,
    )
    webview.start()
