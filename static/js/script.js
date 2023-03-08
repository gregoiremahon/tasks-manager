<script src="https://unpkg.com/axios/dist/axios.min.js"></script>

var app = new Vue({
  el: '#app',
  data: {
    tasks: [],
    newTaskTitle: '',
    newTaskDescription: '',
    newTaskDueDate: ''
  },
  mounted: function() {
    axios.get('/tasks')
      .then(response => {
        this.tasks = response.data;
        console.log(this.tasks);
      })
      .catch(error => {
        console.log(error);
      });
  },
  methods: {
    addNewTask: function() {
      const self = this;
      axios.post('/new_task', {
        title: self.newTaskTitle,
        description: self.newTaskDescription,
        due_date: self.newTaskDueDate
      })
      .then(function(response) {
        const newTask = response.data;
        self.tasks.push(newTask);
        self.newTaskTitle = '';
        self.newTaskDescription = '';
        self.newTaskDueDate = '';
        console.log(self.tasks);
      })
      .catch(function(error) {
        console.log(error);
      });
    },

    deleteTask: function(taskId) { // delete task from database when button is clicked
        const self = this;
        axios.get('/delete_task/' + taskId)
          .then(function(response) {
            self.tasks = self.tasks.filter(task => task.id !== taskId);
            console.log("Task deleted!");
          })
          .catch(function(error) {
            console.log(error);
          });
      }



  }
});
