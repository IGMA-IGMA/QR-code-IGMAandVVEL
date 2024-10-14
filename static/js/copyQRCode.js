function copyQRCode() {
        // Получаем путь изображения QR-кода
        var qrImage = document.getElementById('qrImage');
        var imagePath = qrImage.src;

        // Получаем изображение с помощью fetch
        fetch(imagePath)
            .then(response => response.blob())
            .then(blob => {
                var item = new ClipboardItem({'image/png': blob});
                navigator.clipboard.write([item]).then(function() {
                    // Показать уведомление при успешном копировании
                    var notification = document.getElementById('copyNotification');
                    notification.style.display = 'block';
                    setTimeout(function() {
                        notification.style.display = 'none';
                    }, 2000); // Уведомление отображается 2 секунды
                }).catch(function(error) {
                    alert('Ошибка при копировании: ' + error);
                });
            }).catch(error => {
                console.error('Ошибка получения изображения:', error);
            });
    }