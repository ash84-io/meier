
var Grid = tui.Grid;
var grid = new Grid({
    el: $('#grid'),
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

grid.use('Net', {
    perPage: 15,
    readDataMethod: 'GET',
    api: {
        readData: 'api/posts'
    }
});

grid.on('response', function(data) {
    var pagination = grid.getPagination();
    grid.setData(data.responseData.data.items);
    pagination.setTotalItems(data.responseData.data.total);
    pagination._currentPage = data.responseData.data.page;
    pagination.reset();

}).on('dblclick', function(data){
    console.log(data);
    var row = data.rowKey;
    var postId = grid.getRow(row)['id'];
    console.log(postId);

});