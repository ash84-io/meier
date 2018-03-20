var vm;
vm = new Vue({
    el: '#vue-section',
    data: {
        email: "",
        password: ""
    },
    methods: {
        login: function (event) {
            var data;
            data = {
                email: this.email,
                password: this.password
            };
            axios.post('/admin/user/login',
                JSON.stringify(data), {
                    headers: {
                        'Content-Type': 'application/json'
                    }
                })
                .then(function (res) {
                    console.log(res.data.data.next);
                    location.href = $SCRIPT_ROOT + res.data.data.next;
                })
                .catch(function (err) {
                    alert("Retry Sign in");
                });
        }
    }
});

