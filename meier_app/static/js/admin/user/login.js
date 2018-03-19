
(function () {
    $("#login").click( function () {
        var data;
        data = {
            email: $("#email").val(),
            password: $("#password").val()
        };
        axios.post('/admin/user/login',
            JSON.stringify(data), {
                headers: {
                    'Content-Type': 'application/json'
                }
            })
            .then(function (res) {
                console.log(res.data.data.next);
                location.href=$SCRIPT_ROOT + res.data.data.next;
            })
            .catch(function (err) {
                alert("Retry Sign in");
            });
    });
})();