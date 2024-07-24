$(function () {
    function bindCodeBtnClick() {
        $('#email-code-btn').click(function (event) {
            let $this = $(this)
            let email = $("input[name='email']").val();
            if (!email) {
                alert('Please input your email address!');
                return;
            }
            $this.off('click');

            // Send ajax request
            $.ajax('/auth/verification/?email=' + email, {
                method: 'GET',
                success: function (result) {
                    if (result['code'] === 200) {
                        alert('Verification code sent successfully!');
                    } else {
                        alert(result['message']);
                    }
                    console.log(result);
                },
                fail: function (error) {
                    console.log(error);
                }
            })

            // Countdown
            let countdown = 6;
            let timer = setInterval(function () {
                if (countdown <= 0) {
                    $this.text('get code');
                    clearInterval(timer);
                    bindCodeBtnClick();
                } else {
                    countdown--;
                    $this.text(countdown + 's');
                }
            }, 1000);
        })
    }

    bindCodeBtnClick();
});

