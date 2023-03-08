<script src="https://unpkg.com/axios/dist/axios.min.js"></script>


var app = new Vue({
    el: '#app',
    data: {
        tasks: []
    },
    mounted: function() {
        axios.get('/tasks')
            .then(response => {
                this.tasks = response.data;
                console.log(tasks)
            })
            .catch(error => {
                console.log(error);
            });
    }
});