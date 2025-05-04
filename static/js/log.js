document.getElementById('loginForm').addEventListener('submit', async function (event) {
    event.preventDefault();

    // دریافت مقادیر ورودی‌ها
    const username = document.getElementById('username').value.trim();
    const password = document.getElementById('loginPassword').value.trim();
    const usernameError = document.getElementById('usernameError');
    const passwordError = document.getElementById('passwordError');
    const successMessage = document.getElementById('successMessage');

    // ریست کردن پیام‌های خطا و موفقیت
    usernameError.textContent = "";
    passwordError.textContent = "";
    usernameError.style.display = "none";
    passwordError.style.display = "none";
    successMessage.style.display = "none";

    // بررسی خالی بودن فیلدها
    if (!username) {
        usernameError.textContent = "لطفاً نام کاربری خود را وارد کنید.";
        usernameError.style.display = "block";
        return;
    }
    if (!password) {
        passwordError.textContent = "لطفاً رمز عبور خود را وارد کنید.";
        passwordError.style.display = "block";
        return;
    }

    // داده‌ها برای ارسال به سرور
    const data = new URLSearchParams();
    data.append('username', username);
    data.append('password', password);
    console.log(data);

    try {
        const response = await fetch('http://127.0.0.1:8000/users/login/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
            body: data,
        });

        // بررسی وضعیت پاسخ سرور
        if (!response.ok) {
            throw new Error(`خطای سرور: ${response.status}`);
        }

        const result = await response.json();

        // پردازش پاسخ سرور
        if (result.status === "success") {
            successMessage.textContent = "با موفقیت وارد شدید!";
            successMessage.style.display = "block";

            // هدایت به صفحه جدید
            setTimeout(() => {
                window.location.href = result.redirect_url || "../pa/slideshow.html";
            }, 3000);
        } else {
            if (result.error && Array.isArray(result.error)) {
                result.error.forEach(err => {
                    if (err.path === "username") {
                        usernameError.textContent = err.msg;
                        usernameError.style.display = "block";
                    }
                    if (err.path === "password") {
                        passwordError.textContent = err.msg;
                        passwordError.style.display = "block";
                    }
                });
            } else if (result.message) {
                passwordError.textContent = result.message;
                passwordError.style.display = "block";
            }
        }
    } catch (error) {
        console.error('خطا در ارتباط با سرور:', error);
        passwordError.textContent = "خطا در ارتباط با سرور. لطفاً دوباره تلاش کنید.";
        passwordError.style.display = "block";
    }
});
