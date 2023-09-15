<template>
  <div class="main-nav">
    <router-link :to="{name: 'home'}">Portfolio</router-link>
    <router-link :to="{name: 'AddProject'}">Add a new Position</router-link>
  </div>
</template>

<script>
export default {

}

</script>


<style >

.main-nav{
  text-align: center;
  margin: 40px auto;
}
.main-nav a{
  display: inline-block;
  text-decoration: none;
  margin: 0  10px;
  color: #999;
  font-size: 22px;

}
a.router-link-active{
  border-bottom: 2px solid green;
  padding-bottom: 4px;
}
</style>