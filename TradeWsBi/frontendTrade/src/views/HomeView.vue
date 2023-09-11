<template>
  <div class="home">
    <div v-if="projects.length">
      <div v-for="project in projects" :key="project.id">
<!--        @star="handelStar"-->
        <SingleProject :project="project" @delete="handleDelete"  />
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src

import axios from "axios";
import SingleProject from "@/components/SingleProject.vue";

export default {
  name: 'HomeView',
  components: {SingleProject},
  data(){
    return {
      projects: [],
    }
  },
  mounted(){
    axios
        .get("http://127.0.0.1:8000//portfolio/api/")
        .then(response => {
          this.projects = response.data
          console.log(this.projects)
        })
  },
    methods: {
      handleDelete(id) {
        this.projects = this.projects.filter(item => {
          return item.id !== id
        })
      },
    }
}
</script>

