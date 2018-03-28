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
    computed: {
        compiledMarkdown: function () {
            let converted_html = marked(this.content, {sanitize: true, gfm:true, tables:true});
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
