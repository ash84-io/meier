
var vm = new Vue({
    el: '#vue-section',
    data: {
        blog_title: "",
        blog_desc: "",
        post_per_page: "",
        theme: ""
    },
    mounted: function () {
        let self = this;
        axios({
            method:'get',
            url:'/admin/settings/api/blog_info',
            responseType:'application/json'
        }).then(function (res) {
            self.blog_title = res.data.data.blog_title;
            self.theme = res.data.data.theme;
            self.blog_desc = res.data.data.blog_desc;
            self.post_per_page = res.data.data.post_per_page;
            showNotification('primary', 'Load Complete');
        }).catch(function (err) {
            showNotification('warning', 'Load Error');
        });
    },
    methods: {
        save: function (event) {
            var data;
            data = {
                blog_title: this.blog_title,
                blog_desc: this.blog_desc,
                post_per_page: this.blog_title,
                theme: this.theme
            };

            if(!data.blog_title){
                showNotification("top", "center");
            }
            axios.post('/admin/settings/api/blog_info',
                JSON.stringify(data), {
                    headers: {
                        'Content-Type': 'application/json'
                    }
                })
                .then(function (res) {
                    showNotification('primary', 'Save Changed');
                })
                .catch(function (err) {
                    showNotification('danger', 'Save Error');
                });
        }
    }
});

