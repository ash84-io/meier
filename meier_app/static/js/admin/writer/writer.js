let mark_to_html=null;

Vue.component('input-tag', InputTag);

let vm = new Vue({
    el: '#vue-section',
    data: {
        postId:null,
        title:'',
        content: '### title',
        tags:'',
        postPageURL:'',
        status:'1',
        visibility : '0',
        featured_image:''
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
                self.postId = payload.data.post.id;
                self.title = payload.data.post.title;
                self.content = payload.data.post.raw_content;
                self.postPageURL = payload.data.post.post_name;
                self.tags = payload.data.tags;
                self.status = payload.data.post.status.toString();
                self.visibility = payload.data.post.visibility.toString();
                self.featured_image = payload.data.post.featured_image;
                showNotification('primary', 'Load Complete');
            }).catch(function (err) {
                showNotification('warning', 'Load Error');
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
        save:function () {
            let tags = this.tags;
            if (tags ===''){
                tags = [];
            }
            let data = {
                title:this.title,
                content:this.content,
                html:mark_to_html,
                tags:tags,
                post_name:this.postPageURL,
                status:parseInt(this.status),
                visibility:parseInt(this.visibility),
                featured_image:this.featured_image
            };
            console.log(data);
            if(!data.post_name){
                alert('required post or page URL');
            }
            else if(this.postId !== null) {
                //update
                axios.put('/admin/writer/api/post/'+this.postId.toString(),
                    JSON.stringify(data), {
                        headers: {
                            'Content-Type': 'application/json'
                        }
                    })
                    .then(function (res) {
                        showNotification('primary', 'Update Complete');
                    })
                    .catch(function (err) {
                        showNotification('primary', 'Update Error');
                    });
            }
            else {
                // new
                axios.post('/admin/writer/api/post',
                    JSON.stringify(data), {
                        headers: {'Content-Type': 'application/json'}
                    })
                    .then(function (res) {
                        showNotification('primary', 'Save Changed');
                        let payload = res.data;
                        this.postId = payload.id;
                    })
                    .catch(function (err) {
                        showNotification('danger', 'Save Error');
                    });
            }
        },
        draft:function () {

        },
        bold:function () {
            this.content += ' ** **';
        },
        gist:function () {
            this.content += "<script src='GIST_URL'></script>";
        },
        italic:function () {
            this.content += ' * *';
        },
        table:function () {
            let tableMarkdown='\nFirst Header | Second Header\n' +
                '------------ | -------------\n' +
                'Content from cell 1 | Content from cell 2\n' +
                'Content in the first column | Content in the second column'

            this.content +=tableMarkdown;
        },
        image:function () {
            this.content += " ![Alt text](http://path/to/img.jpg)";
        },
        file_code:function(){
            this.content += "\n```python\n```";
        },
        code:function () {
            this.content += " `code`";
        },
        link:function () {
            this.content += " [Title](link)";
        },
        quote:function () {
            this.content += "\n> ";
        }
    }
});
