const app = Vue.createApp({
  data() {
    return {
      tasks: [],
      
      newTaskTitle: '',
      newTaskDescription: '',
      newTaskDueDate: '',
      completed: 0,
    }
  },
  mounted() {
    axios.get('/tasks')
      .then(response => {
        this.tasks = response.data;
        console.log(this.tasks);
      })
      .catch(error => {
        console.log(this.tasks, error);
      });
  },
  methods: {
    addNewTask() {
      axios.post('/new_task', {
        newTaskTitle: this.newTaskTitle,
        newTaskDescription: this.newTaskDescription,
        newTaskDueDate: this.newTaskDueDate,
          completed: 0,
        }, { headers: { 'Content-Type': 'application/json' } })
        .then(response => {
          const newTask = response.data;
          this.tasks.push(newTask);
          this.newTaskTitle = '';
          this.newTaskDescription = '';
          this.newTaskDueDate = '';
          console.log(this.tasks);
        })
        .catch(error => {
          console.log(error);
        });
    },
  
    deleteTask(taskId) { // delete task from database when button is clicked
      const self = this;
      axios.get('/delete_task/' + taskId)
        .then(function(response) {
          self.tasks = self.tasks.filter(task => task.id !== taskId);
          console.log("Task deleted!");
        })
        .catch(function(error) {
          console.log(error);
        });
    },

    updateTask(task) {
      axios.patch(`/update_task/${task.id}`, {completed: task.completed})
        .then(response => {
          console.log(response.data);
        })
        .catch(error => {
          console.log(error);
        });
    },
  }
});

app.mount('#app');
