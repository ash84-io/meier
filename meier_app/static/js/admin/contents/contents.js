
var Grid = tui.Grid;
// DRAFT GRID
var draftGrid = new Grid({
    el: $('#draft-grid'),
    scrollX: false,
    scrollY: false,
    pagination:true,
    rowHeaders: ['checkbox'],
    columns: [
        {
            title: 'created_at',
            name: 'created_at',
            width:100
        },
        {
            title: 'modified_at',
            name: 'modified_at',
            width:100
        },
        {
            title: 'title',
            name: 'title'
        },
        {
            title: 'post-name',
            name: 'post_name'
        },
        {
            title: 'visibility',
            name: 'visibility',
            width:100,
            editOptions: {
                type: 'select',
                listItems: [
                    { text: 'PRIVATE', value: '0' },
                    { text: 'PUBLIC', value: '1' }
                ],
                useViewMode: true
            },
            formatter: function(value, rowData) {
                if(rowData.visibility === 0){
                    return "PRIVATE"
                }else{
                    return "PUBLIC"
                }
            }

        },
        {
            title: 'status',
            name: 'status',
            width:100,
            formatter: function(value, rowData) {
                if(rowData.status === 0){
                    return "DRAFT"
                }else{
                    return "PUBLISH"
                }
            }
        }

    ]
});

draftGrid.use('Net', {
    perPage: 15,
    readDataMethod: 'GET',
    api: {
        readData: 'api/draft'
    }
});

draftGrid.on('dblclick', function(data){
    if(data.hasOwnProperty('rowKey')) {
        let row = data.rowKey;
        let postId = draftGrid.getRow(row)['id'];
        location.href = "/admin/writer?post_id="+postId;
    }
});

// CONTENT-GRID
var contentGrid = new Grid({
    el: $('#content-grid'),
    scrollX: false,
    scrollY: false,
    pagination:true,
    rowHeaders: ['checkbox'],
    columns: [
        {
            title: 'created_at',
            name: 'created_at',
            width:100
        },
        {
            title: 'title',
            name: 'title'
        },
        {
            title: 'post-name',
            name: 'post_name'
        },

        {
            title: 'visibility',
            name: 'visibility',
            width:100,
            editOptions: {
                type: 'select',
                listItems: [
                    { text: 'PRIVATE', value: '0' },
                    { text: 'PUBLIC', value: '1' }
                ],
                useViewMode: true
            },
            formatter: function(value, rowData) {
                if(rowData.visibility === 0){
                    return "PRIVATE"
                }else{
                    return "PUBLIC"
                }
            }

        },
        {
            title: 'status',
            name: 'status',
            width:100,
            formatter: function(value, rowData) {
                if(rowData.status === 0){
                    return "DRAFT"
                }else{
                    return "PUBLISH"
                }
            }
        }

    ]
});

contentGrid.use('Net', {
    perPage: 15,
    readDataMethod: 'GET',
    api: {
        readData: 'api/posts'
    }
});

contentGrid.on('dblclick', function(data){
    if(data.hasOwnProperty('rowKey')) {
        var row = data.rowKey;
        var postId = contentGrid.getRow(row)['id'];
        location.href = "/admin/writer?post_id="+postId;
    }
});

let vm_draft = new Vue({
    el: '#vue-draft-section',
    data:{q:''},
    methods: {
        searchDraft: function(event){
            net = draftGrid.getAddOn('Net');
            net.readData(1, {'q':this.q}, true);
        },
        deleteDraft: function (event) {
            let willDeletePostIDList = [];
            let rows = draftGrid.getCheckedRows();
            for (let i in rows){
                willDeletePostIDList.push(rows[i].id);
            }
            deletePosts(willDeletePostIDList);
        }
    }
});

let vm_posts = new Vue({
    el: '#vue-posts-section',
    data:{q:''},
    methods: {
        searchPosts: function(event){
            net = contentGrid.getAddOn('Net');
            net.readData(1, {'q':this.q}, true);
        },
        deletePosts:function (event) {
            let willDeletePostIDList = [];
            let rows = contentGrid.getCheckedRows();
            for (let i in rows){
                willDeletePostIDList.push(rows[i].id);
            }
            deletePosts(willDeletePostIDList);
        }
    }
});

function deletePosts(postIdList) {
    let delFunctionList = [];
    for (let i in postIdList) {
        function getUserAccount() {
            return axios.delete('/admin/contents/api/posts/' + (postIdList[i].toString()));
        }
        delFunctionList.push(getUserAccount());
    }

    axios.all(delFunctionList)
        .then(axios.spread(function (acct, perms) {
            showNotification('primart', 'Delete Complete');
            location.href="/admin/contents";
        })).catch(function (err) {
        showNotification('warning', 'Delete Error');
    });
}

