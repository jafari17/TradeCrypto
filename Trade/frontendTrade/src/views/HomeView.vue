<template>
  <div class="home">
    <div v-if="projects.length">
<!--        @star="handelStar"-->
        <table>
            <div class="project" >
              <div class="actions">
                <tr>
                  <th>entry date</th>
                  <th>type</th>
                  <th>currency</th>
                  <th>entry price</th>
                  <th>dollar value</th>
                  <th>coin value</th>
                </tr>
            </div>
          </div>


          <tr>
            <div v-for="project in projects" :key="project.id">
              <SingleProject :project="project" @delete="handleDelete"  />
            </div>
          </tr>
          <RowCalculation :projects="projects"/>
        </table>

    </div>
  </div>
</template>

<script>
// @ is an alias to /src

import axios from "axios";
import SingleProject from "@/components/SingleProject.vue";
import RowCalculation from "@/components/RowCalculation.vue";

export default {
  name: 'HomeView',
  components: {SingleProject, RowCalculation},
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

