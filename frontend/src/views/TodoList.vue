<template>
  <form @submit.prevent="createTodo">
    <div class="container mb-5 row" style="max-width: 50rem; margin: auto;">
      <div class="container col-12 col-lg-4 mb-3">
        <div class="input-group">
          <input type="text" class="form-control" placeholder="Todo's title" v-model="todoTitle" />
        </div>
      </div>
      <div class="container col-12 col-lg-5 mb-3">
        <div class="input-group">
          <input
            type="text"
            class="form-control"
            placeholder="Todo's description"
            v-model="todoDescription"
          />
        </div>
      </div>
      <div class="container col-12 col-lg-3">
        <button type="submit" class="btn btn-primary">Add a new todo!</button>
      </div>
    </div>
  </form>
  <div v-for="todo in todoList" :key="todo.id" class="container row mb-3">
    <div class="container col-2 col-lg-1" style="margin: auto">
      <div class="form-check" style="margin-left: 80%">
        <input
          v-if="todo.state == false"
          class="form-check-input"
          @click="updateCurrentState(todo.id)"
          type="checkbox"
          value
          id="flexCheckDefault"
        />
        <input
          v-else
          class="form-check-input"
          @click="updateCurrentState(todo.id)"
          type="checkbox"
          value
          id="flexCheckDefault"
          checked
        />
      </div>
    </div>
    <div class="container col-8 col-lg-10">
      <router-link
        class="router-link"
        :to="{
          name: 'TodoDetail',
          params: { id: todo.id },
        }"
      >
        <div class="card">
          <div class="card-body">
            <p v-if="todo.state == true" class="mb-0">
              <s>{{ todo.title }}</s>
            </p>
            <p v-else class="mb-0">{{ todo.title }}</p>
          </div>
        </div>
      </router-link>
    </div>
    <div class="container col-2 col-lg-1" style="margin: auto;">
      <button
        type="submit"
        class="btn-close"
        @click="deleteTodo(todo.id)"
        aria-label="Close"
        style="margin-right: 80%;"
      ></button>
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
      todoTitle: "",
      todoDescription: "",
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
      await this.getTodoList();
    },

    async createTodo() {
      await axios.post(this.todoUrl, {
        title: this.todoTitle,
        description: this.todoDescription,
        state: false,
      }),
        this.todoTitle = "";
      this.todoDescription = "";
      this.getTodoList();
    },

    async deleteTodo(todo_id) {
      await axios.delete(`${this.todoUrl}${todo_id}/`);
      this.getTodoList();
    },
  },

  created() {
    this.getTodoList();
  }

}
</script>

<style>
.router-link,
.router-link:hover {
  text-decoration: none;
  color: black;
}
</style>
