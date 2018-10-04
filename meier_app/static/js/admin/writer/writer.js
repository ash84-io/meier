
if (!String.prototype.splice) {
    String.prototype.splice = function(start, delCount, newSubStr) {
        return this.slice(0, start) + newSubStr + this.slice(start + Math.abs(delCount));
    };
}

let mark_to_html=null;

let vm = new Vue({
    el: '#vue-section',
    data: {
        postId:null,
        title:'',
        content: '### title',
        tags:'',
        postPageURL:'',
        status:'0',
        visibility : '0',
        featured_image:'',
        isExpand:false
    },
    mounted: function () {
        let url = location.href;
        let queryString = url.substring( url.indexOf('?') + 1 );
        let parsedQs = queryString.split('=');
        let postId = null;
        if(parsedQs.length === 2){
            postId = parseInt(parsedQs[1]);
        }
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

        document.getElementById('admin-mk-writer').addEventListener('scroll', this.syncPreviewScroll);
        document.getElementById('admin-mk-preview').addEventListener('scroll', this.syncWriterScroll);

    },
    beforeDestory: function(){
        document.getElementById('admin-mk-writer').removeEventListener('scroll', this.syncPreviewScroll);
        document.getElementById('admin-mk-preview').removeEventListener('scroll', this.syncWriterScroll);

    },
    computed: {
        compiledMarkdown: function () {
            let converted_html = marked(this.content, {sanitize: false, gfm:true, tables:true, pedantic:true, langPrefix:'language-'});
            mark_to_html = converted_html;
            return converted_html;
        }
    },
    methods: {
        syncPreviewScroll: function(){
            let mkPreview = document.getElementById('admin-mk-preview');
            let mkWriter = document.getElementById('admin-mk-writer');
            mkPreview.scrollTop = mkWriter.scrollTop;
        },
        syncWriterScroll: function(){
            let mkPreview = document.getElementById('admin-mk-preview');
            let mkWriter = document.getElementById('admin-mk-writer');
            mkWriter.scrollTop = mkPreview.scrollTop;
        },
        update: _.debounce(function (e) {
            this.content = e.target.value
        }, 100),
        toggleExpand:function(){
            if(this.isExpand === false){
                $("#admin-main-panel").css('width', '100%');
                setTimeout(function(){
                    $("#admin-sidebar").css('display','none'); }, 280);

                $("#admin-mk-writer").css('width', '100%');
                $("#admin-mk-preview").css('display', 'none');

                this.isExpand = true;
            }else{
                $("#admin-sidebar").css('display','block');
                $("#admin-main-panel").css('width', '');
                $("#admin-mk-preview").css('display', 'block');
                $("#admin-mk-writer").css('width', '');

                this.isExpand = false;
            }
        },
        save:function () {
            let tags = this.tags;
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
                        location.href = "/admin/contents";
                    })
                    .catch(function (err) {
                        showNotification('danger', 'Save Error');
                    });
            }
        },
        draft:function () {

        },
        bold:function () {
            var pos = this.get_cursor_pos(document.getElementById('admin-mk-writer'));
            if(pos.start === pos.end) {
                this.content = this.content.splice(pos.start, 0, "** **");
            } else {
                this.content = this.content.splice(pos.start, 0, "**");
                this.content = this.content.splice(pos.end+2, 0, "**");
            }
        },
        gist:function () {
            var pos = this.get_cursor_pos(document.getElementById('admin-mk-writer'));
            this.content = this.content.splice(pos.start, 0, "<script src='GIST_URL'></script>");
        },
        italic:function () {
            var pos = this.get_cursor_pos(document.getElementById('admin-mk-writer'));
            if(pos.start === pos.end) {
                this.content = this.content.splice(pos.start, 0, "* *");
            } else {
                this.content = this.content.splice(pos.start, 0, "*");
                this.content = this.content.splice(pos.end+1, 0, "*");
            }

        },
        table:function () {
            let tableMarkdown='\nFirst Header | Second Header\n' +
                '------------ | -------------\n' +
                'Content from cell 1 | Content from cell 2\n' +
                'Content in the first column | Content in the second column';

            var pos = this.get_cursor_pos(document.getElementById('admin-mk-writer'));
            this.content = this.content.splice(pos.start, 0, tableMarkdown);
        },
        image:function () {
            var pos = this.get_cursor_pos(document.getElementById('admin-mk-writer'));
            this.content = this.content.splice(pos.start, 0, " ![Alt text](http://path/to/img.jpg)");
        },
        file_code:function(){
            var pos = this.get_cursor_pos(document.getElementById('admin-mk-writer'));
            this.content = this.content.splice(pos.start, 0, "\n```python\n```");
        },
        code:function () {
            var pos = this.get_cursor_pos(document.getElementById('admin-mk-writer'));
            if(pos.start === pos.end) {
                this.content = this.content.splice(pos.start, 0, " `code`");
            } else {
                this.content = this.content.splice(pos.start, 0, "`");
                this.content = this.content.splice(pos.end+1, 0, "`");
            }
        },
        link:function () {
            var pos = this.get_cursor_pos(document.getElementById('admin-mk-writer'));
            this.content = this.content.splice(pos.start, 0, "[Title](link)");
        },
        quote:function () {
            var pos = this.get_cursor_pos(document.getElementById('admin-mk-writer'));
            this.content = this.content.splice(pos.start, 0, "\n> ");

        },
        get_cursor_pos: function(input) {
            if ("selectionStart" in input) {
                return {
                    start: input.selectionStart,
                    end: input.selectionEnd
                };
            }
            else if (input.createTextRange) {
                var sel = document.selection.createRange();
                if (sel.parentElement() === input) {
                    var rng = input.createTextRange();
                    rng.moveToBookmark(sel.getBookmark());
                    for (var len = 0; rng.compareEndPoints("EndToStart", rng) > 0; rng.moveEnd("character", -1)) {
                        len++;
                    }
                    rng.setEndPoint("StartToStart", input.createTextRange());
                    for (var pos = { start: 0, end: len }; rng.compareEndPoints("EndToStart", rng) > 0; rng.moveEnd("character", -1)) {
                        pos.start++;
                        pos.end++;
                    }
                    return pos;
                }
            }
            return -1;
        }
    }
});
