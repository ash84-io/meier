var vm = new Vue({
    el: '#vue-section',
    data:{
        email:'',
        user_name:'',
        twitter_profile:'',
        facebook_profile:'',
        website:'',
        user_desc:''
    },
    mounted: function () {
        axios({
            method:'get',
            url:'/admin/user/api/user_info',
            responseType:'application/json'
        }).then(function (res) {
            let payload = res.data.data;
            vm.email = payload.email;
            vm.user_name = payload.user_name;
            vm.twitter_profile= payload.twitter_profile;
            vm.facebook_profile= payload.facebook_profile;
            vm.website= payload.website;
            vm.user_desc= payload.user_desc;
        }).catch(function (err) {
            console.log(err);
        });
    },
    methods: {
        update: function (event) {
            console.log("update");
            let params = {
                email:vm.email,
                user_name:vm.user_name,
                twitter_profile:vm.twitter_profile,
                facebook_profile:vm.facebook_profile,
                website:vm.website,
                user_desc:vm.user_desc
            };

            axios.put('/admin/user/api/user_info',
                JSON.stringify(params), {
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

