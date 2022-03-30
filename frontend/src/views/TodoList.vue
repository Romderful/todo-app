<template>
  <div v-for="todo in todoList" :key="todo.id" class="container">
    <div class="card mb-3">
      <div class="card-body">
        <div class="form-check">
          <input
            class="form-check-input"
            @click="updateCurrentState(todo.id)"
            type="checkbox"
            value
            id="flexCheckDefault"
          />
          <p v-if="todo.state == true" class="mb-0">
            <strike>{{ todo.title }}</strike>
          </p>
          <p v-else class="mb-0">{{ todo.title }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: 'TodoList',
  data() {
    return {
      todoUrl: "http://127.0.0.1:8000/api-v1/todos/",
      todoList: [],
      currentState: null,
    }
  },

  methods: {
    async getTodoList() {
      const response = await axios.get(this.todoUrl);
      this.todoList = response.data;
    },

    async updateCurrentState(todo_id) {
      const response = await axios.get(`${this.todoUrl}${todo_id}/`);
      this.currentState = response.data["state"]
      if (this.currentState == true) {
        await axios.patch(`${this.todoUrl}${todo_id}/`, {
          state: false
        });
        this.currentState = false;
      } else {
        await axios.patch(`${this.todoUrl}${todo_id}/`, {
          state: true
        })
        this.currentState = true;
      }
      this.getTodoList();
    },
  },

  created() {
    this.getTodoList();
  }

}
</script>
