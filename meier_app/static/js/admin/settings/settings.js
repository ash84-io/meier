
var vm = new Vue({
    el: '#vue-section',
    data: {
        blog_title: "",
        blog_desc: "",
        post_per_page: "",
        theme: ""
    },
    mounted: function () {
        var self = this;
        axios({
            method:'get',
            url:'/admin/settings/api/blog_info',
            responseType:'application/json'
        }).then(function (res) {
            self.blog_title = res.data.data.blog_title;
            self.theme = res.data.data.theme;
            self.blog_desc = res.data.data.blog_desc;
            self.post_per_page = res.data.data.post_per_page;
            showNotification('top', 'center', 'ok');
        }).catch(function (err) {
            // todo : erorr
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
                    alert("Save Changed.");
                })
                .catch(function (err) {
                    alert("Save Error.");
                });
        },
        showNotification : function (from, align) {
            color = 'primary';

            $(jQuery).notify({
                icon: "now-ui-icons ui-1_bell-53",
                message: "test"
            },{
                type: color,
                timer: 8000,
                placement: {
                    from: from,
                    align: align
                }
            });
        }
    }
});

