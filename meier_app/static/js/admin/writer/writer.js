let mark_to_html=null;

Vue.component('input-tag', InputTag);

let vm = new Vue({
    el: '#vue-section',
    data: {
        input: '### title',
        tagsArray:''
    },
    updated:function () {
        console.log('mounted');
    },
    computed: {
        compiledMarkdown: function () {
            let converted_html = marked(this.input, {sanitize: true, gfm:true, tables:true});
            mark_to_html = converted_html;
            return converted_html;
        }
    },
    methods: {
        update: _.debounce(function (e) {
            this.input = e.target.value
        }, 100),
        publish:function () {

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