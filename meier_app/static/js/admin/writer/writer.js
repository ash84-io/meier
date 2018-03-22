
var vm;
vm = new Vue({
    el: '#vue-section',
    mounted: function () {
        var editor = new tui.Editor({
            el: document.querySelector('#editor'),
            initialEditType: 'markdown',
            previewStyle: 'vertical',
            height: '600px',
            codeBlockLanguages: ['python', 'javascript'],
            useCommandShortcut: true,
            exts: ['scrollSync', 'colorSyntax', 'uml', 'chart', 'mark', 'table', 'taskCounter']
        });
    },
    methods: {
        save: function (event) {
            console.log("save");
        },
        delete: function(event){
            console.log("delete");
        }
    }

});
