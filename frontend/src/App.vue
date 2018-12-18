<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
export default {
  components: {

  }
};
</script>


<style lang="scss">
* {
  box-sizing: border-box;
  font-size: 14px;
}

body {
  padding: 0;
  margin: 0;
}

#app {
  font-family: Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
