<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Form Gửi Dữ Liệu</title>
</head>
<body>
    <h2>Form Gửi Dữ Liệu</h2>
    <form id="dataForm">
        <label for="name">Họ và Tên:</label>
        <input type="text" id="name" required><br><br>
        <label for="email">Email:</label>
        <input type="email" id="email" required><br><br>
        <button type="submit">Gửi</button>
    </form>

    <script>
        const form = document.getElementById('dataForm');
        form.addEventListener('submit', async (e) => {
            e.preventDefault();

            const data = {
                name: document.getElementById('name').value,
                email: document.getElementById('email').value
            };

            // Gửi dữ liệu đến webhook trên Replit
            await fetch('https://your-username.repl.co/webhook', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data)
            });

            alert("Dữ liệu đã gửi thành công!");
        });
    </script>
</body>
</html>
