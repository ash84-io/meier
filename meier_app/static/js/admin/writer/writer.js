let mark_to_html=null;

Vue.component('input-tag', InputTag);

let vm = new Vue({
    el: '#vue-section',
    data: {
        title:'',
        content: '### title',
        tagsArray:'',
        postPageURL:''
    },
    mounted: function () {
        let url = location.href;
        let queryString = url.substring( url.indexOf('?') + 1 );
        let parsedQs = queryString.split('=');
        let postId = null;
        if(parsedQs.length === 2){
            postId = parseInt(parsedQs[1]);
        }
        console.log(postId);
        if(postId){
            let self = this;
            axios({
                method:'get',
                url:'/admin/contents/api/posts/' + postId,
                responseType:'application/json'
            }).then(function (res) {
                console.log(res);
                let payload = res.data;
                self.title = payload.data.post.title;
                self.content = payload.data.post.raw_content;
                self.postPageURL = payload.data.post.post_name;
                self.tagsArray =payload.data.tag_list;
            }).catch(function (err) {
                alert('error');
            });
        }
    },
    computed: {
        compiledMarkdown: function () {
            let converted_html = marked(this.content , {sanitize: true, gfm:true, tables:true});
            mark_to_html = converted_html;
            return converted_html;
        }
    },
    methods: {
        update: _.debounce(function (e) {
            this.content = e.target.value
        }, 100),
        publish:function () {
            let tags = this.tagsArray;
            if (tags ===''){
                tags = [];
            }
            let data = {
                title:this.title,
                content:this.content,
                html:mark_to_html,
                tags:tags,
                post_name:this.postPageURL
            };
            console.log(data);
            if(!data.post_name){
                alert('required post or page uRL');
            }
            else{
                axios.post('/admin/writer/api/post',
                    JSON.stringify(data), {
                        headers: {'Content-Type': 'application/json'}
                    })
                    .then(function (res) {
                        alert("Save Changed.");
                    })
                    .catch(function (err) {
                        alert("Save Error.");
                    });
            }
        },
        draft:function () {

        },
        bold:function () {

        },
        gist:function () {

        },
        italic:function () {

        },
        table:function () {

        },
        image:function () {

        },
        code:function () {

        },
        link:function () {

        },
        quote:function () {

        }
    }
});
